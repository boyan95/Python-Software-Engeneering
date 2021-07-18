import re

data = input()

pattern = r"(^|(?<=\s))([a-z]+|[0-9]+)([\.-]?(\w+)?)?@(?P<host>[a-z]+([\.-]?[a-z]+?)([\.][a-z]+)?([\.][a-z]+)?([\.][a-z]+)?[\.][a-z]+)"

email = re.finditer(pattern, data)
email = [e.group() for e in email]
print(*email, sep='\n')