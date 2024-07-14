"""Release the latest monthly issue."""

import os
from datetime import datetime

parent_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
draft_dir = os.path.join(parent_dir, "drafts")
issue_dir = os.path.join(parent_dir, "issues")

files = [
    file
    for file in os.listdir(draft_dir)
    if file.endswith(".md") and not file.startswith(".") and file != "TEMPLATE.md"
]
assert len(files) == 1

file = os.path.join(draft_dir, files[0])

os.system(f"mv {file} {issue_dir}")
