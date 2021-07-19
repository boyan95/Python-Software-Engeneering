import re

line = input()
mails = []
pattern = r"(?P<www>^|w{3})\.(?P<name>[a-zA-Z0-9\-]+)(?P<domain_block>\.[a-z]+)+\b"

while line:
    email = [e.group() for e in re.finditer(pattern, line)]
    mails.extend(email)
    line = input()

for mail in mails:
    print(mail)
