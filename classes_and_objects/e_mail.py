class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.mail_sent = False

    def send(self):
        self.mail_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.mail_sent}'


emails = []
line = input()
while line != "Stop":
    input_data = line.split(' ')
    email = Email(input_data[0], input_data[1], input_data[2])
    emails.append(email)
    line = input()

sent_emails_indexes = [int(x) for x in input().split(', ')]
for x in sent_emails_indexes:
    emails[x].send()
for email in emails:
    print(email.get_info())