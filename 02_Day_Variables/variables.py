import math

# Day 2: 30 Days Python Programming
#----------------------------------
# What you need to do for Day 2 exercise that's needed to be done in order to move on
# - Compare the length of your first name and your last name
# - Declare 5 as num_one and 4 as num_two
# - Add num_one and num_two and assign the value to a variable _total
# - Subtract num_two from num_one and assign the value to a variable _diff
# - Multiply num_two and num_one and assign the value to a variable _product
# - Divide num_one by num_two and assign the value to a variable _division
# - Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
# - Calculate num_one to the power of num_two and assign the value to a variable _exp
# - Find floor division of num_one by num_two and assign the value to a variable _floor_division
# - The radius of a circle is 30 meters.
# - Calculate the area of a circle and assign the value to a variable area_of_circle
# - Take radius as user input and calculate the area.
# - Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# - Run help('keywords') in python shell or in your file to check for the reserved words

# Example solution

num_one = 5
num_two = 4

_total = num_one + num_two
num_two - num_one
_diff = num_one - num_two
product = num_two * num_one
_division = num_one / num_two
_remainder = num_two % num_one
_exp = num_one ^ num_two
_floor_division = num_one // num_two

print("Total:", _total)
print("Differenve:", _diff)
print("Dividion:", _division)
print("Remainder:", _remainder)
print("Floor division:", _floor_division)
print("Exponent:", _exp)

# Circle

def circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = 30
area, circumference = circle_properties(radius)
print(f"Area: {area:.2f}")
int(f"Circumference: {circumference:.2f}")

# Name

first_name = 'Dr.anibal'
last_name = 'Lectoring'
country = 'Switzerland'
age = 35
year = 2077
is_married = False
is_true =  True
is_light_on = 'Yes'
skills = ['Python', 'HTML', ]
person_info = {
    'firstname':'',
    'lastname':'',
    'country':'Switzerland',
    'city':'Defiance'
    }

### Printing the values stored in the variables

first_name = input('First name: ')
print('First name length:', len(first_name))
area, circumference = circle_properties(radius)
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

last_name = input('Last name: ')
print('Last name length:', len(last_name))

while True:

    if len(first_name) < len(last_name):
        print(f"{first_name} is longer.")
    elif len(first_name) > len (last_name):
        print(f'{first_name} is longer.')
    else:
        print("Both names are of equal length.")
    break

print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


print(type(first_name))
print(type(last_name))


#-------------------

print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type([skills]))
print(type([person_info]))

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Dr.fanibal', 'Lectser', 'Defiance', 35, False

print(first_name, last_name, country, age, is_married)
print('First name: ', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)