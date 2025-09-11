# Exercises

# 1. Create a an empty dictionary called dog 
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'first_name':'Juneau',
    'color':'Brownish',
    'breed':'Lab',
    'legs':4,
    'age':5,
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.   
student = {
    'first_name':'Ilo',
    'last_name':'Clementine',
    'gender':'male', 
    'age':24,
    'marital_status':'single',
    'skills':['Car repair', 'Reader', 'Car brands', 'Mechanic'],
    'country':'USA',
    'city':'RI',
    'address':{
        'street': 'Space Street',
        'zipcode':'02210'
    }
}

# 4. Get the length of the student dictionary 
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list.   
skills = student['skills']

print(skills)
print(type(skills))

# 6. Modify the skills values by adding one or two skills 
skills = student['skills']

student['skills'].append('Motocycle engines')    # so apparently the .append in this example stays white because it came from python's built-in classes. Same goes for .keys() and .values().   
print(skills)

# 7. Get the dictionary keys as a list 
student = {
    'first_name':'Ilo',
    'last_name':'Clementine',
    'gender':'male', 
    'age':24,
    'marital_status':'single',
    'skills':['Car repair', 'Reader', 'Car brands', 'Mechanic'],
    'country':'USA',
    'city':'RI',
    'address':{
        'street': 'Space Street',
        'zipcode':'02210'
    }
}

keys = student.keys()
print(keys)
# 8. Get the dictionary values as a list
values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples using items() method
student = {
    'first_name':'Ilo',
    'last_name':'Clementine',
    'gender':'male', 
    'age':24,
    'marital_status':'single',
    'skills':['Car repair', 'Reader', 'Car brands', 'Mechanic'],
    'country':'USA',
    'city':'RI',
    'address':{
        'street': 'Space Street',
        'zipcode':'02210'
    }
}

print(student.items())

# 10. Delete one of the items in the dictionary 
student = {
    'first_name':'Ilo',
    'last_name':'Clementine',
    'gender':'male', 
    'age':24,
    'marital_status':'single',
    'skills':['Car repair', 'Reader', 'Car brands', 'Mechanic'],
    'country':'USA',
    'city':'RI',
    'address':{
        'street': 'Space Street',
        'zipcode':'02210'
    }
}

del student['address']
print(student)

# 11. Delete one of the dictionaries
dog = {
    'first_name':'Juneau',
    'color':'Brownish',
    'breed':'Lab',
    'legs':4,
    'age':5,
}

del dog
print(dog)