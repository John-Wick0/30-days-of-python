import math

num_one = 5
num_two = 4

_total = num_one + num_two
num_one - num_two
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

# Example solution

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

## Printing the values stored in the variables

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
