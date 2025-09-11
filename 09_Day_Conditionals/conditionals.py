# Come back tonight and continue with day 9 exercises from the github user, then move on to the next day.   
# I want to get more days done because I feel like I am slacking a bit which can't happen.  
# We must stay focus.  

# Get the user input unsing input("Enter your age:").   
# If user is 18 or older, give feedback: You are old enough to drive.  
# If below 18 give feedback to wait for the missing amount of years.  

# Output: 

# Enter your age: X 
# You are old enough to learn to drive.  

# Output:
# Enter your age: X 
# You need x more years to learn to drive.  

age = int(input("Enter your age:"))

if age >= 18:
        print("You are old enough to drive.")
else:
    year_left = 18 - age
    print(f"You need {year_left} more years to learn to drive.")

# Compare the values of my_age and your_age using if ... else. Who is older(me or you)?  
# Use input("Enter your age:") to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text 
# if my_age = your_age.

# Output:  
# You are X yearls older than me.  

my_age = int(input("Enter your age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
      diff = my_age - your_age
      print(f"I am {diff} years older than you.")
elif your_age > my_age:
      diff = your_age - my_age
      print(f"I am {diff} years older than me.")
else:
      print("We are the same age.")

# Get two numbers from the user using input prompt.  
# If a is greater than b return a is greater than b
# If a is less than b return a is less than b, else a is equal to b 

num_1 = int(input("Enter number: "))
num_2 = int(input("Enter number two: "))

if num_1 > num_2:
      print(f"{num_1} is bigger than {num_2}.")
      if num_1 < num_2:
            print(f"{num_1} is less than {num_2}.")
else:
      print(f"{num_1} is equal to {num_2}.")

# Write a code which gives grade to students according to their scores:

# 80-100 -> A
# 70-89 -> B
# 60-69 -> C
# 50-59 -> D
# 0-49 -> F 

# Two: options nested/cleaner version
students = int(input("Enter your score: "))

# Nested version
if students >= 50:
      if students >= 60:
            if students >= 70:
                  if students >= 80:
                        print("Grade: A")
                  else:
                        print("Grade: B")
            else:
                  print("Grade: C")
      else:
            print("Grade: D")
else:
      print("Grade: F")

# cleaner version 

if students >= 80 and students <= 100:
      print("Grade: A")
elif students >= 70 and students <= 89:
      print("Grade: B")
elif students >= 60 and students <= 69:
      print("Grade: C") 
elif students >= 50 and students <= 59:
      print("Grase: D")
else:
      print("Grade: F")

# Check if the season is Autumn, Winter, Spring or summer.  
# If the user input is: September, October or November, the season is Autumn.   
# If the user input is: December, January or February, the seaon is Winter.   
# If the user input is: March, April or May, the season is Spring.   
# If the user input is: June, July, or August, the season is Summer.   
user = input("Enter the month: ").capitalize()

seasons = {
      'September':'Autumn', 'October':'Autumn', 'November':'Autumn',
      'December':'Winter', 'January':'Winter', 'February':'Winter',
      'March':'Spring', 'April':'Spring', 'May':'Spring',
      'June':'Summer', 'July':'Summer', 'August':'Summer',
    
}

# This line of code will look up the user's input (user) in the dictionary seasons.   
if user in seasons:
      print(f"The season is {seasons[user]}")
else:
      print("Invalid month entered.")

# The following list contains some fruits:  
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.   
# If the fruit exists print('That fruit already exist in the list')

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
      print("That fruit already exist in the list.")
else:
      fruit.append(fruits) 
      print(f"{fruit} has been added to the list.")

print("Updated list:", fruits)

# Here we have a person dictionary. Feel free to modify it!    
person={
      'first_name':'Asabeneh',
      'last_name':'Yetayeh',
      'age':250,
      'country':'Finland',
      'is_married':True,
      'skills:':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
      'address':{
            'street': 'Space street',
            'zipcode':'02210'
      }
}

# check if the person dictionary has skills key, if so print out the middle skills in skills list.  
# check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.  
# if a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer')
# if the person skills, has React, Node, and MongoDB, Print('He is a fullstack developer'), else print('unknown tittle') - for more accurate results more conditions can be nested!  
# if the person is married and if he lives in Finland, print the information in the following format: 

    # Asabeneh Yetayeh lives in Finland. He is married.  

if 'skills' in person:
      skills = person['skills']
      middle = skills[len(skills//2)]
      print("Middle skills:", middle)
      
      if 'Python' in person['skills']:
            print("The person has Python skill.")

if 'Javascript' in person['skills'] and  'React' in person['skills']:
    print("He is a front end developer.")

elif all(skill in person['skills'] for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer.")

elif all(skills in person['skills'] for skull in ['Reacr', 'Node', 'MongoDB']):
    print('He is a fullstack developer.')
else:
    print('Unknown tittle')
    print(f"{person['first_name']} {person['last_name']} live in {person['country']}.")
if person['is_married']:
    print("He is married.")
else:
    print('He is not married.')
