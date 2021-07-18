import re

data = input()
pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
matches = re.finditer(pattern, data)

for match in matches:
    date = match.groupdict()
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")