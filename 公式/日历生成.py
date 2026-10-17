# -*- coding: utf-8 -*-
"""
一键生成中国节假日维表 + 时间维度表（带中文注释表头，ISO 8601 周编号）
"""
import json
import urllib.request
import csv
import os
from datetime import date, timedelta
from collections import Counter

# ========== 配置 ==========
START_DATE = date(2020, 1, 1)
END_DATE   = date(2025, 12, 31)
YEARS      = list(range(START_DATE.year, END_DATE.year + 2))
OUT_DIR    = "./output"
os.makedirs(OUT_DIR, exist_ok=True)

# 表头风格: "mixed"=中英混合(默认, 人读)  "en"=纯英文(入库)  "cn"=纯中文(报告)
HEADER_STYLE = "mixed"

URL_TEMPLATES = [
    "https://cdn.jsdelivr.net/gh/NateScarlet/holiday-cn@master/{year}.json",
    "https://fastly.jsdelivr.net/gh/NateScarlet/holiday-cn@master/{year}.json",
    "https://raw.githubusercontent.com/NateScarlet/holiday-cn/master/{year}.json",
]

# ========== 字段定义（英文名 + 中文注释）==========
HOLIDAY_FIELDS = [
    ("date_id", "日期"),
    ("type",    "类型:1-节假日,2-调休补班"),
    ("name",    "节日名称"),
]

DATE_FIELDS = [
    ("date_id",    "日"),
    ("week_id",    "周ID"),
    ("week_day",   "周几"),
    ("day",        "每月的第几天"),
    ("month",      "第几月"),
    ("quarter",    "第几季度"),
    ("year",       "年"),
    ("is_workday", "是否是工作日"),
    ("holiday_id", "节假日"),
]

def make_header(fields):
    """根据 HEADER_STYLE 生成表头"""
    if HEADER_STYLE == "en":
        return [en for en, _ in fields]
    if HEADER_STYLE == "cn":
        return [cn for _, cn in fields]
    # mixed
    return [f"{en}({cn})" for en, cn in fields]

# ========== 1. 拉取节假日数据 ==========
holiday_rows = []
seen = set()
for year in YEARS:
    data = None
    for tpl in URL_TEMPLATES:
        url = tpl.format(year=year)
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            print(f"[OK] 拉取 {year} 年数据，来源: {url}")
            break
        except Exception as e:
            print(f"[WARN] {url} 失败: {e}")
    if data is None:
        print(f"[ERROR] {year} 年数据全部拉取失败，跳过")
        continue

    for day in data["days"]:
        date_id = day["date"]
        h_type  = "1" if day["isOffDay"] else "2"
        name    = day["name"]
        if date_id in seen:
            continue
        seen.add(date_id)
        holiday_rows.append((date_id, h_type, name))

print(f"\n共获取 {len(holiday_rows)} 条节假日/调休记录\n")

# ========== 2. 写节假日维表 CSV ==========
holiday_csv = os.path.join(OUT_DIR, "dim_holiday_info.csv")
with open(holiday_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(make_header(HOLIDAY_FIELDS))     # ← 表头
    for row in sorted(holiday_rows):
        w.writerow(row)
print(f"[OK] 节假日维表已写出: {holiday_csv}")

# ========== 3. 构造 Map ==========
holiday_map = {r[0]: r[2] for r in holiday_rows if r[1] == "1"}
workday_map = {r[0]: r[2] for r in holiday_rows if r[1] == "2"}

# ========== 4. 生成时间维度表（ISO 8601 修正版）==========
date_rows = []
d = START_DATE
while d <= END_DATE:
    date_id = d.strftime("%Y-%m-%d")
    iso_year, iso_week, iso_weekday = d.isocalendar()   # (ISO周年, ISO周号, ISO周几)
    week_id = f"{iso_year}{iso_week:02d}"                # 例：202053、202401
    is_weekend = iso_weekday >= 6

    holiday_name = holiday_map.get(date_id)
    makeup_name  = workday_map.get(date_id)

    # 调休优先级最高
    if makeup_name:
        is_workday, holiday_id = "1", makeup_name
    elif holiday_name:
        is_workday, holiday_id = "0", holiday_name
    elif is_weekend:
        is_workday, holiday_id = "0", ""
    else:
        is_workday, holiday_id = "1", ""

    date_rows.append((
        date_id,
        week_id,
        str(iso_weekday),
        str(d.day),
        str(d.month),
        str((d.month - 1) // 3 + 1),
        str(d.year),
        is_workday,
        holiday_id,
    ))
    d += timedelta(days=1)

print(f"[OK] 共生成 {len(date_rows)} 条日期记录")

# ========== 5. 写时间维度表 CSV ==========
date_csv = os.path.join(OUT_DIR, "dim_date_info.csv")
with open(date_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(make_header(DATE_FIELDS))        # ← 表头
    for row in date_rows:
        w.writerow(row)
print(f"[OK] 时间维度表已写出: {date_csv}")

# ========== 6. 校验统计 ==========
year_cnt = Counter(r[6] for r in date_rows if r[7] == "1")
print("\n各年工作日天数：")
for y in sorted(year_cnt):
    print(f"  {y}: {year_cnt[y]} 天")

print("\n完成 ✅  输出目录:", os.path.abspath(OUT_DIR))