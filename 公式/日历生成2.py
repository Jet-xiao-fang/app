# -*- coding: utf-8 -*-
"""
一键生成中国节假日维表 + 时间维度表（输出 txt，\t 分隔）
- week_id = 该日期所在周的周一~周日（ISO 8601，周一为首日）
- week_workday_cnt = 该周内的工作日天数
"""
import json
import urllib.request
import csv
import os
from datetime import date, timedelta
from collections import Counter, defaultdict

# ========== 配置 ==========
START_DATE = date(2023, 1, 1)
END_DATE   = date(2026, 12, 31)
YEARS      = list(range(START_DATE.year, END_DATE.year + 2))
OUT_DIR    = "./output"
os.makedirs(OUT_DIR, exist_ok=True)

# 表头风格: "mixed"=中英混合(默认)  "en"=纯英文(入库)  "cn"=纯中文(报告)
HEADER_STYLE = "mixed"

URL_TEMPLATES = [
    "https://cdn.jsdelivr.net/gh/NateScarlet/holiday-cn@master/{year}.json",
    "https://fastly.jsdelivr.net/gh/NateScarlet/holiday-cn@master/{year}.json",
    "https://raw.githubusercontent.com/NateScarlet/holiday-cn/master/{year}.json",
]

# ========== 字段定义 ==========
HOLIDAY_FIELDS = [
    ("date_id", "日期"),
    ("type",    "类型:1-节假日,2-调休补班"),
    ("name",    "节日名称"),
]

DATE_FIELDS = [
    ("date_id",           "日"),
    ("week_id",           "周ID(周一~周日)"),
    ("week_day",          "周几"),
    ("day",               "每月的第几天"),
    ("month",             "第几月"),
    ("quarter",           "第几季度"),
    ("year",              "年"),
    ("is_workday",        "是否是工作日"),
    ("holiday_name",        "节假日"),
    ("week_workday_cnt",  "本周工作日天数"),
]

def make_header(fields):
    if HEADER_STYLE == "en":
        return [en for en, _ in fields]
    if HEADER_STYLE == "cn":
        return [cn for _, cn in fields]
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

# ========== 2. 写节假日维表 TXT ==========
holiday_txt = os.path.join(OUT_DIR, "dim_holiday_info.txt")
with open(holiday_txt, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(make_header(HOLIDAY_FIELDS))
    for row in sorted(holiday_rows):
        w.writerow(row)
print(f"[OK] 节假日维表已写出: {holiday_txt}")

# ========== 3. 构造 Map ==========
holiday_map = {r[0]: r[2] for r in holiday_rows if r[1] == "1"}
workday_map = {r[0]: r[2] for r in holiday_rows if r[1] == "2"}

# ========== 4. 第一遍：生成每天基础数据（week_workday_cnt 先占位）==========
date_rows = []   # 每行：[date_id, week_id, week_day, day, month, quarter, year, is_workday, holiday_id, None]
d = START_DATE
while d <= END_DATE:
    date_id = d.strftime("%Y-%m-%d")

    # week_id: 该周周一~周日
    monday = d - timedelta(days=d.weekday())
    sunday = monday + timedelta(days=6)
    week_id = f"{monday.strftime('%Y-%m-%d')}~{sunday.strftime('%Y-%m-%d')}"

    iso_weekday = d.isoweekday()       # 1=周一 ... 7=周日
    is_weekend  = iso_weekday >= 6

    holiday_name = holiday_map.get(date_id)
    makeup_name  = workday_map.get(date_id)

    if makeup_name:
        is_workday, holiday_id = "1", makeup_name
    elif holiday_name:
        is_workday, holiday_id = "0", holiday_name
    elif is_weekend:
        is_workday, holiday_id = "0", ""
    else:
        is_workday, holiday_id = "1", ""

    date_rows.append([
        date_id,
        week_id,
        str(iso_weekday),
        str(d.day),
        str(d.month),
        str((d.month - 1) // 3 + 1),
        str(d.year),
        is_workday,
        holiday_id,
        None,             # week_workday_cnt 待回填
    ])
    d += timedelta(days=1)

# ========== 5. 第二遍：按 week_id 统计工作日数量并回填 ==========
week_workday_cnt = defaultdict(int)
for r in date_rows:
    if r[7] == "1":
        week_workday_cnt[r[1]] += 1

for r in date_rows:
    r[9] = str(week_workday_cnt[r[1]])

print(f"[OK] 共生成 {len(date_rows)} 条日期记录，"
      f"涉及 {len(week_workday_cnt)} 个自然周")

# ========== 6. 写时间维度表 TXT ==========
date_txt = os.path.join(OUT_DIR, "dim_date_info.txt")
with open(date_txt, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(make_header(DATE_FIELDS))
    for row in date_rows:
        w.writerow(row)
print(f"[OK] 时间维度表已写出: {date_txt}")

# ========== 7. 校验统计 ==========
year_cnt = Counter(r[6] for r in date_rows if r[7] == "1")
print("\n各年工作日天数：")
for y in sorted(year_cnt):
    print(f"  {y}: {year_cnt[y]} 天")

print("\n每周工作日天数分布（前 10 周）：")
week_seen = []
for r in date_rows:
    if r[1] not in week_seen:
        week_seen.append(r[1])
    if len(week_seen) >= 10:
        break
for wk in week_seen:
    print(f"  {wk}: {week_workday_cnt[wk]} 天")

print("\n完成 ✅  输出目录:", os.path.abspath(OUT_DIR))