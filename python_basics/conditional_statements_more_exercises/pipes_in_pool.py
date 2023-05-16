pool_volume = int(input())
debit_p1 = int(input())
debit_p2 = int(input())
time_pipes_on = float(input())

p1_total_lt = debit_p1 * time_pipes_on
p2_total_lt = debit_p2 * time_pipes_on
total_lt_in = p1_total_lt + p2_total_lt

if total_lt_in <= pool_volume:
      percent_full = 100 / (pool_volume / total_lt_in)
      percent_p1 = 100 / (total_lt_in / p1_total_lt)
      percent_p2 = 100 / (total_lt_in / p2_total_lt)
      print(f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
      print(f"For {time_pipes_on:.2f} hours the pool overflows with {total_lt_in - pool_volume:.2f} liters.")
