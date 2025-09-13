# 1. Declare your age as integer variable
# 2. Declare your height as a float variable
# 3. Declare a complex number variable
# 4. Write a script that prompts the user to enter base and height of the triangle and
# calculate an area of this triangle (area = 0.5 x b x h)

# Exercises

#  Write a script that prompts the user to enter a base and height of a shape and calculate the area of that shape.
Age = 45 # int
Height = 4.2 # float
j = 3j # complex

base = input('Enter base: ')
height = input('Enter height: ')
area_of_triangle  = 0.5 * 20 * 10 
print(area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter_triangle = side_a + side_b + side_c
print(int(perimeter_triangle))

# 1. Get length and width of a rectangle using prompt/ Calculate its area (area = length X width) and perimeter (perimeter = 2 x (length + width))
# This is how you script for an area, width, perimeter of a rectangle

length = int(input('Enter length: '))
width = int(input('Enter width: '))
area_of_rectangle = length * width
perimeter = 2 * (length + width)
print('Area of a rectangle: ', area_of_rectangle)
print('Perimeter of a rectangle: ', perimeter)

# Get radius of a circle using prompt. Calculate the area(area = pi x r x r) and Circumference (c = 2 x pi x r) where pi = 3.14

radius = int(input('Radius: '))
circle = 2 * 3.14 * radius
circumference_of_circle = 3.14 * radius * radius
print(circumference_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y/x2-x1). Find the slope between point (2, 2) and point (6, 10)
# Compare the slopes

# First: Define the equation and extract slope and intercepts
    # . the equation is y = 2x - 2
    # . slope (m) is the coefficient of x, which is 2
    # . y-intercept is the constant term, which is -2
    # . x-intercept is found by setting y = 0 and solving for x
# Second: Calculate the slope between two points
    # . use the formula: m = (y2 - y1) / (x2 - x1)
    # . for points (2, 2) and (6, 10), substitute the values

# Before you move on since you got stuck on this part, here's a little definition of coefficient:

#   . In an equation like the one below, the coefficient is the number multiplying a variable.

# So 2 is the coefficient of x. It tells you how much y changes for each unit change in x.

# Why: . The coefficient determines the slope of the line (how steep it is).
#       . If the coefficient is positive, the line goes up as x increases. if it's negative the line goes down.

# How to spot it: . In y = mx + c, m is always the coefficient of x (the slope). Thr number without a variable (here -2) is the intercept (where the line crosses the y-axis).

# You can practice by changing the coefficient below etc....

# Equation:  y = 2x - 2

# Slope from the equation
slope_equation = 2 # coefficient

# y-intercept (when x = 0)
y_intercept = -2 # Constant term

# x-intercept (when y = 0). 
# So: 0 = 2x - 2 => 2x = 2 => x = 1
x_intercept = 1

print("Slope from equation:", slope_equation)
print("y_intercept:", y_intercept)
print("x_intercept:", x_intercept)

# Slope between two points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_points = (y2 - y1) / (x2 - x1)
print("Slope between points (2, 2) and (6, 10):", slope_points)


# Calculate the value of y (y = x^2 + 6x + 9)
# Try to use different x values and figure out at what x value y is 0.

# Equation y = x^2 + 6x + 9
# the above means for any value of x, you can calculate y by plugging x into the formula.

# To code it: . Choose a value for x 
#             . Use python's operator for exponentiation (x is written as x**2)
#             . Calculate y using the formula.
#             . Print the result
# At what x value does y = 0? 
# y = 0 on x value -6x.

x = 3

y = x**2 + -6*x + 9

print("x =", x, "y =", y)

# Find the length of 'python' and 'jargon' and make a falsy comparison statement:
print(len('python'))
print(len('jargon'))

if len ('python') == 'jargon':
    print(True)
elif len ('jargon') != 'python':
    print(True)

# Use and operator to check if 'on' is found in both 'python and 'jargon':
print('on' in 'python' and 'on' in 'jargon')

# Use 'in' operator to check if jargon is in the sentence:
print('in' in 'jargon')

# There is no 'on' in both dragon and python
print('There is no' 'on' in 'both' 'dragon' and 'python')

# Turn the text 'python' into a float
text = 'python'

try:
    print(float(text))
except ValueError:
    print("You cannot convert 'python' into a float")

# Find the length of the text python
text = 'python'
length = len(text)
print(text)

# Convert the value to float   
num = 6
# Convert the value to str
num_str = float(6)
print('num: ', num)

# Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

# This is how you check if a number is even or odd
even_number = 2
remainder = 0

if 2 % 2 == 0:
    print("Even")
else:
    print("Odd")

# The floor division of 7 by 3 is equal to the int converted value of 2.7:

# The floor division of 7 by 3 is 2. 
# The int converted value of 2.7 is also a 2.

floor_division = 7 // 3
print(floor_division)

# Check if '10' is equal to 10 & if '9.8' is equal to 10.
if '10' == 10:
    print("Yes '10' does equal to 10.")
else:
    print("No '10' does not equal to 10.")

if '9.8' == 10:
    print("Yes, it does equal to 10.")
else:
    print("No, it does not equal to 10.")

# Write a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person.
hours = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour: '))
pay = hours * rate_per_hour
print(f"Your pay is: ${pay}")


# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume someone lives up to hundred years.
age = int(input("Enter your current age: "))
years_left = age 
expected_lifespan = 80
years_left == expected_lifespan - age
seconds_left = years_left * 365 * 24 * 60 * 60
if age < expected_lifespan:
    print(f"You have approximately: {years_left} years left to live.")
if age > expected_lifespan:
	print(f"You have approximately: {seconds_left} seconds left to live.")

# Write a python script that displays the following table:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

table = [
    '1 1 1 1 1',
    '2 1 2 4 8',
    '3 1 3 9 27',
    '4 1 4 16 64',
    '5 1 5 25 125']

for  col in table:
    print(col)


total/price = 44
print(total/price)  