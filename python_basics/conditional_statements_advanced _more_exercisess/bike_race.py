juniors = int(input())
seniors = int(input())
trace = input()  # trail", "cross-country", "downhill", "road"
collected_sum = 0

if trace == 'trail':
    collected_sum = juniors * 5.5 + seniors * 7
elif trace == 'cross-country':
    collected_sum = juniors * 8 + seniors * 9.5
    if juniors + seniors >= 50:
        collected_sum *= 0.75
elif trace == 'downhill':
    collected_sum = juniors * 12.25 + seniors * 13.75
elif trace == 'road':
    collected_sum = juniors * 20 + seniors * 21.50

collected_sum *= 0.95

print(f'{collected_sum:.2f}')