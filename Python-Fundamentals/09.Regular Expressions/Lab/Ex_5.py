import re

data = input()
total = 0
products = []
pattern = r">>(?P<product>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d)"

print("Bought furniture:")
while not data == "Purchase":
    matches = (re.finditer(pattern, data))
    for m in matches:
        date = m.groupdict()
        print(f"{date['product']}")
        total += (float(date['price']) * float(date['quantity']))

    data = input()

print(f"Total money spend: {total}")
