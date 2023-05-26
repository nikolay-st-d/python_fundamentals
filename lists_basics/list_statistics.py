number_of_inputs = int(input())

negatives = []
positives = []
negatives_count = 0
positives_count = 0

for _ in range(number_of_inputs):

    number = int(input())

    if number < 0:
        negatives.append(number)
        negatives_count += 1
    else:
        positives.append(number)
        positives_count += 1

print(positives)
print(negatives)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {sum(negatives)}")


