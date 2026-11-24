import glob, os
BASE = os.path.dirname(os.path.abspath(__file__))
for path in glob.glob(os.path.join(BASE, "lead-general-partie-*.py")):
    text = open(path, encoding="utf-8").read()
    stack, i, line, state = [], 0, 1, None
    pairs = {')':'(', ']':'[', '}':'{'}
    while i < len(text):
        c = text[i]
        if c == '\n':
            line += 1
        if state == '"':
            if c == '\\':
                i += 2; continue
            if c == '"':
                state = None
        elif state == "'":
            if c == '\\':
                i += 2; continue
            if c == "'":
                state = None
        else:
            if c == '#':
                while i < len(text) and text[i] != '\n': i += 1
                continue
            if c in ('"', "'"):
                state = c
            elif c in '([{':
                stack.append((c, line))
            elif c in ')]}':
                if stack and stack[-1][0] == pairs[c]:
                    stack.pop()
                else:
                    print(path, "MISMATCH", c, "line", line, "stack top", stack[-1] if stack else None)
                    break
        i += 1
    if state:
        print(os.path.basename(path), "UNTERMINATED STRING from line", line)
    if stack:
        print(os.path.basename(path), "UNCLOSED", stack[-5:])
    if not state and not stack:
        print(os.path.basename(path), "OK")
