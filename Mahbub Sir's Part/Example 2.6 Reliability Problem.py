# importing packages
import pandas as pd
from tabulate import tabulate

# defining Random Digits
random_digits_bearing_1_life = [25, 82, 16, 14, 82, 45, 81, 80, 97, 62, 30, 31, 80, 72, 63, 59, 9, 25, 70, 64, 61, 92, 12]
random_digits_bearing_2_life = [65, 91, 30, 66, 32, 29, 11, 43, 40, 65, 82, 73, 15, 70, 65, 33, 54, 87, 27, 37, 99, 94, 12]
random_digits_bearing_3_life = [94, 87, 63, 66, 30, 69, 37, 1, 66, 51, 92, 36, 47, 80, 94, 31, 7, 9, 19, 29, 29, 94, 87]

random_digits_bearing_1_repairman_delay = [9, 8, 0, 5, 2, 3, 7, 3, 7, 4, 9, 5, 6, 7, 6, 0, 2, 3, 9, 8, 3, 3, 2]
random_digits_bearing_2_repairman_delay = [5, 0, 5, 6, 5, 3, 2, 8, 0, 8, 2, 4, 4, 6, 9, 9, 5, 7, 7, 4, 8, 4, 4]
random_digits_bearing_3_repairman_delay = [7, 0, 6, 2, 2, 7, 2, 8, 8, 3, 8, 3, 7, 0, 4, 7, 1, 6, 2, 3, 2, 5, 6]

# defining other variables
iter = 23
operation_runtime = 0
operation_simulation_time = 30000 + 1000
bearing_1_life_record = [0] * iter
bearing_2_life_record = [0] * iter
bearing_3_life_record = [0] * iter
bearing_1_clock = 0
bearing_2_clock = 0
bearing_3_clock = 0
bearing_1_clock_record = [0] * iter
bearing_2_clock_record = [0] * iter
bearing_3_clock_record = [0] * iter
bearing_1_delay = 0
bearing_2_delay = 0
bearing_3_delay = 0
bearing_1_delay_record = [0] * iter
bearing_2_delay_record = [0] * iter
bearing_3_delay_record = [0] * iter

bearing_1_delay_count = 0
bearing_2_delay_count = 0
bearing_3_delay_count = 0


# defining bearing life calculation (runtime)
def calc_bearing_time(random_digit):
  bearing_life = 0
  if (random_digit >= 1 and random_digit <= 10):
    bearing_life = 1000
  elif (random_digit >= 11 and random_digit <= 24):
    bearing_life = 1100
  elif (random_digit >= 25 and random_digit <= 48):
    bearing_life = 1200
  elif (random_digit >= 49 and random_digit <= 62):
    bearing_life = 1300
  elif (random_digit >= 63 and random_digit <= 74):
    bearing_life = 1400
  elif (random_digit >= 75 and random_digit <= 84):
    bearing_life = 1500
  elif (random_digit >= 85 and random_digit <= 90):
    bearing_life = 1600
  elif (random_digit >= 91 and random_digit <= 95):
    bearing_life = 1700
  elif (random_digit >= 96 and random_digit <= 98):
    bearing_life = 1800
  elif (random_digit == 99 or random_digit == 00):
    bearing_life = 1900
  
  return bearing_life

# defining repairman delay time
def calc_delay_time(random_digit):
  delay_time = 0
  if (random_digit >= 1 and random_digit <= 3):
    delay_time = 4
  elif (random_digit >= 4 and random_digit <= 9):
    delay_time = 6
  elif (random_digit == 0):
    delay_time = 8
  
  return delay_time


i = 0  # variable to iterate random numbers

# calculating 
while (operation_runtime <= operation_simulation_time and i < 23):

  bearing_1_life = calc_bearing_time(random_digits_bearing_1_life[i])
  if (i == 0):
    bearing_1_clock = bearing_1_life
  else:
    bearing_1_clock += bearing_1_life
  bearing_1_delay = calc_delay_time(random_digits_bearing_1_repairman_delay[i])
  bearing_1_delay_count += bearing_1_delay

  bearing_2_life = calc_bearing_time(random_digits_bearing_2_life[i])
  if (i == 0):
    bearing_2_clock = bearing_2_life
  else:
    bearing_2_clock += bearing_2_life
  bearing_2_delay = calc_delay_time(random_digits_bearing_2_repairman_delay[i])
  bearing_2_delay_count += bearing_2_delay
  
  bearing_3_life = calc_bearing_time(random_digits_bearing_3_life[i])
  if (i == 0):
    bearing_3_clock = bearing_3_life
  else:
    bearing_3_clock += bearing_3_life
  bearing_3_delay = calc_delay_time(random_digits_bearing_3_repairman_delay[i])
  bearing_3_delay_count += bearing_3_delay

  # recording values
  bearing_1_clock_record[i] = bearing_1_clock
  bearing_1_life_record[i] = bearing_1_life
  bearing_1_delay_record[i] = bearing_1_delay

  bearing_2_clock_record[i] = bearing_2_clock
  bearing_2_life_record[i] = bearing_2_life
  bearing_2_delay_record[i] = bearing_2_delay

  bearing_3_clock_record[i] = bearing_3_clock
  bearing_3_life_record[i] = bearing_3_life
  bearing_3_delay_record[i] = bearing_3_delay

  operation_runtime_i = min(bearing_1_life, bearing_2_life, bearing_3_life)
  operation_runtime += operation_runtime_i

  i += 1

# building pandas DataFrame
df = pd.DataFrame({
  "B1 RD Clock" : random_digits_bearing_1_life,
  "B1 Life" : bearing_1_life_record,
  "B1 Clock" : bearing_1_clock_record,
  "B1 RD Delay" : random_digits_bearing_1_repairman_delay,
  "B1 Delay" : bearing_1_delay_record,

  "B2 RD Clock" : random_digits_bearing_2_life,
  "B2 Life" : bearing_2_life_record,
  "B2 Clock" : bearing_2_clock_record,
  "B2 RD Delay" : random_digits_bearing_2_repairman_delay,
  "B2 Delay" : bearing_2_delay_record,
  
  "B3 RD Clock" : random_digits_bearing_3_life,
  "B3 Life" : bearing_3_life_record,
  "B3 Clock" : bearing_3_clock_record,
  "B3 RD Delay" : random_digits_bearing_3_repairman_delay,
  "B3 Delay" : bearing_3_delay_record
})

# tabulating from pandas DataFrame
table = tabulate(
  df,
  headers='keys',
  tablefmt='pipe'
)

# showing table
print(table)

# final calculation
replaced_bearing = 23 * 3
total_delay = bearing_1_delay_count + bearing_2_delay_count + bearing_3_delay_count
replacement_time = replaced_bearing * 20
total_downtime = total_delay + replacement_time
cost_of_bearings = replaced_bearing * 20  # BDT 5 per bearing
cost_of_downtime = total_downtime * 5
cost_of_repairman = ((replaced_bearing * 20) * (25 / 60))
total_cost = cost_of_bearings + cost_of_downtime + cost_of_repairman

# final report
print(f"\nReplaced Bearings = {iter} x 3 = {replaced_bearing}")
print(f"Total Delay (Bearing 1) = {bearing_1_delay_count} \nTotal Delay (Bearing 2) = {bearing_2_delay_count} \nTotal Delay (Bearing 3) = {bearing_3_delay_count} ")
print(f"Repairman Delay = {total_delay}")
print(f"Bearing Replacement Time = {replaced_bearing} x 20 = {replacement_time}")
print(f"Total Machine Downtime = {total_delay} + {replacement_time} = {total_downtime}")
print(f"Repairman's Wage = {replacement_time} x 20 = {replacement_time * 20}")

print(f"\nSo,\nCost of bearing = {replaced_bearing} x 20 = {cost_of_bearings:.2f}")
print(f"Cost of down time = {total_downtime} x 5 = {cost_of_downtime:.2f}")
print(f"Cost of repairman = {replacement_time} x (25/60) = {cost_of_repairman:.2f}")
print("-------------------------------------------------------------------------")
print(f"Total Cost = {total_cost:.2f}\n")