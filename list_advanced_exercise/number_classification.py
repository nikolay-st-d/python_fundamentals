list_of_numbers = list(map(int, input().split(', ')))
positive_list = [str(num) for num in list_of_numbers if num >= 0]
negative_list = [str(num) for num in list_of_numbers if num < 0]
even_list = [str(num) for num in list_of_numbers if num % 2 == 0]
odd_list = [str(num) for num in list_of_numbers if num % 2 != 0]
print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")