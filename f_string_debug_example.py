# Traditional f-strings
title = "Learn Python"
priority = 3
tags = ["async", "python"]

print(f"Title: {title}")
print(f"Priority: {priority}")
print(f"Tags: {tags}")

print("\n=== F-String Debug Syntax (=) ===")
# New Python 3.10+ feature: f"{variable=}"
# Shows BOTH the variable name AND the value!

print(f"{title=}")        # Shows: title='Learn Python'
print(f"{priority=}")     # Shows: priority=3
print(f"{tags=}")         # Shows: tags=['async', 'python']

print("\n=== Expression Debug ===")
# Works with expressions too!
count = len(tags)
print(f"{count=}")        # Shows: count=2
print(f"{len(tags)=}")    # Shows: len(tags)=2