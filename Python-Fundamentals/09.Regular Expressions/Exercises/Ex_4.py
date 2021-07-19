import re

data = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\.-]?[a-zA-Z0-9]+@[a-zA-z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+($|(?=\s))"

email = re.finditer(pattern, data)
email = [e.group() for e in email]
print(*email, sep='\n')