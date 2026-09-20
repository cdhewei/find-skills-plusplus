import io

p = r"C:\Users\win\.workbuddy\skills\find-skills-plusplus\README.md"
s = open(p, encoding="utf-8").read()

ci_line = "[![CI](https://github.com/cdhewei/find-skills-plusplus/actions/workflows/ci.yml/badge.svg)](https://github.com/cdhewei/find-skills-plusplus/actions)"
license_badge = "[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](#许可证与署名)"
if ci_line not in s:
    s = s.replace(license_badge, ci_line + "\n" + license_badge, 1)
else:
    print("CI badge already present")

# Tests badge: normalize 100+ -> 140 (idempotent)
s = s.replace(
    "[![Tests](https://img.shields.io/badge/tests-100%2B%20passing-brightgreen.svg)](#测试)",
    "[![Tests](https://img.shields.io/badge/tests-140%20passing-brightgreen.svg)](#测试)",
)

# Updated badge: 09-19 -> 09-21
s = s.replace(
    "[![Updated](https://img.shields.io/badge/last%20updated-2026--09--19-brightgreen.svg)](#)",
    "[![Updated](https://img.shields.io/badge/last%20updated-2026--09--21-brightgreen.svg)](#)",
)

with open(p, "w", encoding="utf-8") as f:
    f.write(s)

t = open(p, encoding="utf-8").read()
print("HAS_CI_BADGE:", ci_line in t)
print("HAS_140_TESTS:", "tests-140%20passing" in t)
print("HAS_UPDATED_21:", "2026--09--21" in t)
print("STILL_0919:", "2026--09--19" in t)
