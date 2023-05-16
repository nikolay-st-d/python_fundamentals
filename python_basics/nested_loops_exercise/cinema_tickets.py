student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie = input()

while movie != 'Finish':

    free_places = int(input())
    movie_tickets_sold = 0

    while free_places > 0:
        ticket = input()

        if ticket == 'End':
            break

        free_places -= 1
        movie_tickets_sold += 1

        if ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'kid':
            kid_tickets += 1

    print(f'{movie} - {movie_tickets_sold / (free_places + movie_tickets_sold) * 100:.2f}% full.')

    movie = input()

total_tickets_sold = student_tickets + standard_tickets + kid_tickets

print(f'Total tickets: {total_tickets_sold}')
print(f'{student_tickets / total_tickets_sold * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets_sold * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets_sold * 100:.2f}% kids tickets.')
