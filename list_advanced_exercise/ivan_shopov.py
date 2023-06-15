# 1

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)

# 1.1

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = [first_word for first_word in first_sequence
              if any(first_word in second_word for second_word in second_sequence)]
print(substrings)

# 2
version = [int(number) for number in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9 and index != 0:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1
print(".".join(str(number) for number in version))

# 3

words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))

# 4
numbers = input().split(", ")
positive = [number for number in numbers if int(number) >= 0]
negative = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")


# 4.1

def positive_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if int(number) >= 0]


def negative_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if int(number) < 0]


def even_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if int(number) % 2 == 0]


def odd_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if int(number) % 2 != 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")


# 5

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    needed_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
            needed_chairs += abs(difference)
        else:  # difference >=0:
            free_chairs += difference

    return free_chairs, needed_chairs


count_of_rooms = int(input())
total_free_chairs, total_needed_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")


# 5.1 - Sabina

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
            free_chairs += difference
        else:  # difference >=0:
            free_chairs += difference

    return free_chairs


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

# 7

numbers = [int(s) for s in input().split(", ")]
current_group_of_numbers = 10
while numbers:  # while len(numbers) >0
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group_of_numbers]
    # filtered_list_for_current_group = []
    # for current_number in numbers:
    #     if current_number <= current_group_of_numbers:
    #         filtered_list_for_current_group.append(current_number)
    print(f"Group of {current_group_of_numbers}'s: {filtered_numbers_for_current_group}")
    current_group_of_numbers += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]


# 11

def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if "Exercise" in list_of_lessons[title_index + 1]:
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)
    return list_of_lessons


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_index = list_of_lessons.index(first_lesson)
        second_index = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(list_of_lessons)):
            first_has_exercise = "Exercise" in list_of_lessons[first_index + 1]
        if second_index + 1 in range(len(list_of_lessons)):
            second_has_exercise = "Exercise" in list_of_lessons[second_index + 1]
        list_of_lessons[first_index], list_of_lessons[second_index] = \
            list_of_lessons[second_index], list_of_lessons[
                first_index]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_index + 1], list_of_lessons[second_index + 1] = \
                list_of_lessons[second_index + 1], list_of_lessons[first_index + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_index + 1, list_of_lessons.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_index + 1, list_of_lessons.pop(first_index + 1))
    return list_of_lessons


def exercise(list_of_lessons, title):
    if title in list_of_lessons and f"{title}-Exercise" not in list_of_lessons:
        title_index = list_of_lessons.index(title)
        list_of_lessons.insert(title_index + 1, f"{title}-Exercise")
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f"{title}-Exercise")
    return list_of_lessons


lessons = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input()
for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")