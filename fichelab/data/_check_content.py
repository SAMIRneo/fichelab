import re, sys
for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    bad = re.findall(r"[\u4e00-\u9fff\u3040-\u30ff]", s)
    print(path, "CJK:", len(bad), sorted(set(bad)))
    for i, line in enumerate(s.split("\n"), 1):
        if re.search(r"[\u4e00-\u9fff\u3040-\u30ff]", line):
            print("  line", i, line.strip()[:180])
