import sys
lines = open(sys.argv[1], encoding="utf-8").read().split("\n")
stack = []
for ln, line in enumerate(lines, 1):
    in_s = None
    esc = False
    for ch in line:
        if in_s:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == in_s:
                in_s = None
            continue
        if ch == '"' or ch == "'":
            in_s = ch
        elif ch in "([{":
            stack.append((ch, ln))
        elif ch in ")]}":
            if not stack:
                print("extra", ch, "line", ln)
            else:
                o, l = stack.pop()
                if o + ch not in ("()", "[]", "{}"):
                    print("mismatch", o, l, ch, ln)
print("unclosed", stack[-10:])
