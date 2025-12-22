"""Make a new draft."""

import os
from datetime import datetime

parent_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
draft_dir = os.path.join(parent_dir, "drafts")
issue_dir = os.path.join(parent_dir, "issues")

with open(os.path.join(draft_dir, "TEMPLATE.md")) as f:
    content = f.read()

now = datetime.now()
next = datetime(
    year=now.year + 1 if now.month == 12 else now.year,
    month=1 if now.month == 12 else now.month + 1,
    day=1
)

date_filename = next.strftime("%Y-%m")
date_str = next.strftime("%B %Y")

number = 0
files = [
    file
    for file in os.listdir(issue_dir)
    if file.endswith(".md") and not file.startswith(".")
]
for file in files:
    with open(os.path.join(issue_dir, file)) as f:
        pre = True
        for line in f:
            line = line.strip()
            if pre:
                assert line == "---"
                pre = False
                continue
            if line.startswith("number:"):
                number = max(int(line[7:]), number)
                break
            assert line != "---"

content = content.replace("{date}", date_str)
content = content.replace("{issue_number}", f"{number + 1}")

assert not os.path.isfile(os.path.join(draft_dir, f"{date_filename}.md"))
with open(os.path.join(draft_dir, f"{date_filename}.md"), "w") as f:
    f.write(content)
