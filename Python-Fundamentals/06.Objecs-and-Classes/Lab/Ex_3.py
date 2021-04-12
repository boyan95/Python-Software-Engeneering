class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


class EmailManager:
    def __init__(self):
        self.emails = []

    def add(self, email):
        self.emails.append(email)

    def send(self, index):
        self.emails[index].send()

    def print(self):
        for email in self.emails:
            print(email.get_info())


email_manager = EmailManager()
#Read Emails
while True:
    command = input()
    if command == "Stop":
        break
    [sender, receiver, content] = command.split()
    email = Email(sender, receiver, content)
    email_manager.add(email)

# send Emails
indices_of_mails_to_send = [int(el) for el in input().split(", ")]

# print the email_manager
for index in indices_of_mails_to_send:
    email_manager.send(index)

email_manager.print()
