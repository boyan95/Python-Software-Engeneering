class Party:
    def __init__(self):
        self.people = []

    def go(self, name):
        self.people.append(name)

    def get_going(self):
        return f"Going: {', '.join(self.people)}"

    def get_counter(self):
        return f"Total: {len(self.people)}"


party = Party()

while True:
    command = input()
    if command == "End":
        break
    party.go(command)

print(party.get_going())
print(party.get_counter())
