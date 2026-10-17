import re

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def _format_path(path):
    return " > ".join(f"{'#' * level} {title}" for level, title in path)


def _split_long(heading, content, max_chars, overlap):
    prefix = f"{heading}\n" if heading else ""
    budget = max(1, max_chars - len(prefix))
    step = max(1, budget - overlap)
    start = 0
    while start < len(content):
        piece = content[start:start + budget]
        yield prefix + piece
        if start + budget >= len(content):
            break
        start += step


def markdown_to_chunks(markdown_text, max_chars=600, overlap=100):
    lines = markdown_text.splitlines()
    chunks = []
    path = []
    buffer = []

    def emit(heading, content):
        full = f"{heading}\n{content}" if heading else content
        if len(full) <= max_chars:
            chunks.append({
                "heading_path": heading,
                "content": content,
                "text": full,
            })
        else:
            for text in _split_long(heading, content, max_chars, overlap):
                chunks.append({
                    "heading_path": heading,
                    "content": content,
                    "text": text,
                })

    def flush():
        nonlocal buffer
        if not buffer:
            return
        content = "\n".join(buffer).strip()
        buffer = []
        if not content:
            return
        emit(_format_path(path), content)

    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            title = m.group(2).strip()
            path = [h for h in path if h[0] < level]
            path.append((level, title))
        else:
            buffer.append(line)

    flush()
    return chunks
