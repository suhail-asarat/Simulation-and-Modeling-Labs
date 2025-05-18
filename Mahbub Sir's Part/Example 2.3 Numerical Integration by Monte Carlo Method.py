# importing packages
import pandas as pd
from tabulate import tabulate
import sympy as sy

# existing random numbers
random_numbers_x = [22, 25, 18, 45, 25, 27, 48, 43, 40, 47, 38, 33, 24, 47, 42, 25, 33, 50, 34, 21]
random_numbers_y = [.57, .18, .00, .90, .05, .77, .66, .10, .76, .42, .78, .88, .03, .09, .77, .61, .27, .60, .29, .40]

# setting variables
A = 140 * 3 # 420 ## our experiment area
M = 0
N = 0
totalN = 20

# setting data arrays
x_values = [0] * totalN
y_values = [0] * totalN
f_x_values = [0] * totalN
M_values = [0] * totalN
N_values = [0] * totalN

# defining the equation
def f(x):
  return x*x*x

# calculating the actual value
b = 5
a = 2
x = sy.Symbol("x")
result = sy.integrate(f(x), (x, a, b))

# calculating
for i in range (totalN):
  x = random_numbers_x[i] / 10
  y = random_numbers_y[i] * 140
  f_x = f(x)
  if (y <= f_x):
    M += 1
  N += 1

  # inserting data into array
  x_values[i] = x
  y_values[i] = y
  f_x_values[i] = f_x
  M_values[i] = M
  N_values[i] = N

# building pandas DataFrame
df = pd.DataFrame({
  "Random Number (x)" : random_numbers_x,
  "x (0.1 * r)" : x_values,
  "Random Number (y)" : random_numbers_y,
  "y (140 * r)" : y_values,
  "x^3" : f_x_values,
  "M" : M_values,
  "N" : N_values
})

# tabulating from pandas DataFrame
table = tabulate(
  df,
  headers='keys',
  tablefmt='pipe'
)

# showing table
print(table)

# calculating and printing results
I = (M / N) * A
print(f"\nCalculated value of integral = {I:.2f} \nActual value of integral = {result:.2f} \nError = {(abs(I-result) / result) * 100:.2f} %")
