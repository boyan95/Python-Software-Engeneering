import re

data = input()
pattern = r"(^_|(?<=\s_))([a-zA-Z0-9]+)($|(?=\s))"

names = [n.group() for n in re.finditer(pattern, data)]
print(','.join(names))