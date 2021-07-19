import re

line = input()
pattern = r"(^>{2})(?P<product>\w+)<{2}(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)$"
total_price = 0
names = []

while not line == "Purchase":
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        names.append(obj["product"])
        total_price += float(obj["price"]) * int(obj["quantity"])
    line = input()


print("Bought furniture:")
for name in names:
    print(name)
print(f"Total money spend: {total_price:.2f}")
