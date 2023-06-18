from math import floor

biscuits_per_worker_per_day = int(input())
workers_number = int(input())
competition_production_per_30_days = int(input())
total_production = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_production += floor(biscuits_per_worker_per_day * workers_number * 0.75)
    else:
        total_production += biscuits_per_worker_per_day * workers_number

print(f"You have produced {total_production} biscuits for the past month.")

production_difference = abs(total_production - competition_production_per_30_days)
production_difference_percent = production_difference / competition_production_per_30_days * 100

if total_production > competition_production_per_30_days:
    print(f"You produce {production_difference_percent:.2f} percent more biscuits.")
elif total_production < competition_production_per_30_days:
    print(f"You produce {production_difference_percent:.2f} percent less biscuits.")