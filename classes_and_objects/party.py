class Party:
    def __init__(self):
        self.people = []

party = Party()

while True:
    name = input()
    if name == 'End':
        break
    party.people.append(name)

people = ', '.join(party.people)
total_people_going = len(party.people)

print(f'Going: {people}')
print(f'Total: {total_people_going}')