# Exercises 

# 1. Create an empty tuple 
empty_tuple = ()
print(empty_tuple)
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine) 
brothers = ('Messi', 'Mario', 'Ted', 'Bond')
sisters = ('Cardi', 'Lexy', 'Melbourne', 'Plum')
# 3. Join brothers and sisters tuples and assign it to siblings.  
siblings = (brothers + sisters)
# 4. How many siblings do you have? 
print(len(siblings))
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members 
siblings_list = list(siblings)  
print(siblings_list)
siblings_list.append('mother')
siblings_list.append('father')
family_members = tuple(siblings_list)
print(family_members)
# 6. Unpack siblings and parents from family_members 
siblings = tuple(siblings_list[0:8])
family_members = tuple(siblings_list[-2:])
print("parents:", family_members)
print("siblings:", siblings)
# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a varible called food_stuff.  
fruits = ('strawberry', 'mango', 'banana', 'blueberry')
vegetables = ('lettuce', 'Cabbage', 'Tomato', 'Carrot') 
animals = ('dog food', 'treats', 'toys', 'bowls') 
food_stuff = fruits + vegetables + animals 
print(food_stuff)

# 8. Slice out the first, the middle item or items from the food_stuff list  
print(food_stuff[0])
print(food_stuff[5])
print(food_stuff[-6])
print(len(food_stuff))
# 9. Slice out the first three items and the last three items from food_stuff list
print(food_stuff[0:3]) 
print(food_stuff[-3:])
# 10. Delete the food_staff list completely  
food_stuff = ('fruits', 'vegetables', 'animals')
del food_stuff
print('food_stuff has been deleted.')
# 11. Check if an item exist in a tuple: 
#   . Check if 'Estonia' is a nordic country 
#   . Check if 'Iceland' is a nordic country 
#       nordic_coutries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweeden')
fruits = ('banana', 'mango', 'strawberry', 'blueberry')
print('banana' in fruits)

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)