type_of_fuel = input()
liters_in_tank = int(input())

if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    if liters_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
else:
    print("Invalid fuel!")