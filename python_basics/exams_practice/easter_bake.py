from math import ceil

e_breads = int(input())

sugar_spent = 0
flour_spent = 0

max_sugar = 0
max_flour = 0

while e_breads > 0:
    sugar = int(input())
    flour = int(input())

    sugar_spent += sugar
    flour_spent += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

    e_breads -= 1

sugar_packets = ceil(sugar_spent / 950)
flour_packets = ceil(flour_spent / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")