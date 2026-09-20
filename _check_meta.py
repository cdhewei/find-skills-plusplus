import sys
sys.path.insert(0, r"C:\Users\win\.workbuddy\skills\find-skills-plusplus\scripts")
import security_scan as ss

base = r"C:\Users\win\.workbuddy\skills\find-skills-plusplus"
txt = open(base + r"\SKILL.md", encoding="utf-8").read()
ok, fm = ss.parse_frontmatter(txt)
with open(base + r"\_check.txt", "w", encoding="utf-8") as f:
    f.write("ok=%s\n" % ok)
    f.write("metadata type: %s\n" % type(fm.get("metadata")).__name__)
    f.write("metadata: %r\n" % (fm.get("metadata"),))
    f.write("top-level slug: %r\n" % (fm.get("slug"),))
    f.write("top-level displayName: %r\n" % (fm.get("displayName"),))
