p = r"C:\Users\win\.workbuddy\skills\find-skills-plusplus\README.md"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("TOTAL LINES:", len(lines))
for i in range(11, min(20, len(lines))):
    print(f"[{i+1}] {lines[i].rstrip()}")
# markers
txt = "".join(lines)
print("HAS_CI_BADGE:", "actions/workflows/ci.yml/badge.svg" in txt)
print("HAS_140_TESTS:", "tests-140%20passing" in txt)
print("HAS_UPDATED_21:", "2026--09--21" in txt)
print("STILL_100PLUS:", "tests-100%2B%20passing" in txt)
print("STILL_0919:", "2026--09--19" in txt)
