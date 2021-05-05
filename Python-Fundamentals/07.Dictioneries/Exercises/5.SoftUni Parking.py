data = int(input())
cars = {}
for _ in range(data):
    order = input().split()
    command = order[0]
    user_name = order[1]
    if command == "register":
        license_plate_number = order[2]
        if not user_name in cars:
            cars[user_name] = license_plate_number
            print(f"{user_name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command == "unregister":
        if not user_name in cars:
            print(f"ERROR: user {user_name} not found")
        else:
            cars.pop(user_name)
            print(f"{user_name} unregistered successfully")

for car,license_plate_number in cars.items():
    print(f"{car} => {license_plate_number}")