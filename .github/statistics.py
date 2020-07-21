import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List
import yaml


@dataclass
class Question:
    id: int
    lang: str

    submits: List[dict]
    labels: List[str]
    comment: str


def parse_header(lang: str, file_lines: str):
    if lang == "py":
        header_from = header_end = '"""'
    elif lang == "go":
        header_from = "/*"
        header_end = "*/"
    else:
        raise Exception("unknow lang: " + lang)

    from_line_index = file_lines.index(header_from)
    to_line_index = file_lines.index(header_end, from_line_index + 1)
    header_lines = file_lines[from_line_index + 1 : to_line_index]
    header_text = "\n".join(header_lines)
    header = yaml.load(header_text, Loader=yaml.Loader)

    return {
        "submits": header.get("submits", []),
        "labels": header.get("labels", []),
        "comment": header.get("comment", ""),
    }


def walk_questions():
    root = Path(__file__).absolute().parent.parent
    for dirname, _, filenames in os.walk(root):
        if dirname.startswith("."):
            continue
        for filename in filenames:
            # print(repr(filename))
            matched = re.match(r"^([0-9]+)\..+\.(py|go)$", filename)
            if matched:
                id = int(matched[1])
                lang = matched[2]
                print("reading", filename)
                lines = Path(dirname).joinpath(filename).read_text().splitlines()
                q = Question(id=id, lang=lang, **parse_header(lang, lines))
                yield q


if __name__ == "__main__":
    qs = list(walk_questions())
    qs.sort(key=lambda q: q.id)
    for q in qs:
        print(q)
