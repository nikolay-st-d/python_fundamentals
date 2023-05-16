movie_budget = float(input())
statists_number = int(input())
costume_price = float(input())
decor = movie_budget * 0.1
costumes_total = costume_price * statists_number
if statists_number > 150:
    costumes_total -= costumes_total * 0.1
movie_total = costumes_total + decor
if movie_total > movie_budget:
    money_needed = movie_total - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = movie_budget - movie_total
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
