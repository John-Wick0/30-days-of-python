# Tomorrows Goal: Start Day 7 exersises because you finished taking notes on it.
# Suggestions For The future: review your notes and read them like they are a book. 
# Review, but always look to make progress, nothing wrong with a littel set back. 
# Goal: Read, Understand, Review, Practice, Review, Review, Understand, Practice, Practice.  

# sets 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Keep in mind set is undordered.  
# 1. Find the length of the set it_companies
print(len(it_companies))
# 2. Add 'Twitter' to it_companies 
it_companies.add('Twitter')
print(it_companies)
# 3. Insert multiple IT companies at once to the set it_companies 
it_companies.update(['Reddit', 'X', 'Upwork']) # If you are going to insert multiple companies at once you must use [] within it. It keeps the set clean, but without the [] in it it wil give you an output like this:  {'w', 'Oracle', 'IBM', 'Twitter', 't', 'Amazon', 'e', 'Microsoft', 'r', 'R', 'U', 'Apple', 'i', 'p', 'o', 'Google', 'X', 'Facebook', 'k', 'd'}
print(it_companies)
# 4. Remove one of the it_companies from the set it_companies
it_companies.remove('X')
print(it_companies)
# 5. What is the difference between remove() and discard()?
# For me: The difference between remove and discard is; -> Remove() method: raises an error if the item you are trying to locate and remove is not found wihtin the set, always check to see if what you are trying to remove is there first. Discard method(): Does not raise any errors.  
# 6. Join A and B/ Two Options: union method and update methods. They both do the same thing(capable of joining sets and remove any duplicated items)
C = A.union(B)  
D = A.update(B)
print(C)
# 7. Find A intersetion B 
print(A.intersection(B)) # I understood the assingment, but did not print it so I was getting 'None'. But I found my mistake.  
# 8. Is A subset of B 
print(A.issubset(B)) # Yes A is a subset of B after i found the answer by printing it out. Which comes out as a boolean.    
# 9. Are A and B disjoint sets
print(A.isdisjoint(B)) # No A is not a disjoint set
print(B.isdisjoint(A)) # No B is not a disjoint set 
# 10. Join A with B and B with A 
print(A.update(B))
print(B.union(A))
# 11. What is the symmetric difference between A and B 
print(A.symmetric_difference(B)) # The symmetric difference between A and B is: {27, 28} two extra digits within the B set.  
# 12. Delete the sets completely 
del A # deleted set A
del B # deleted set B
# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?  set: 5 - list: 8. So list is bigger.  
# In python list are unhashable type.  
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(list(age))) # I forgot that if i want to turn or compare a list to a set and vice versa I must enter (set) or (list) within the items after (len). I am still getting used to set but tuple and list can't help but be around haha.   
# 14. Explain the difference between the following data types: string, list, tuple, set 

# The difference between a string and a list:
#   . A string is an immutable sequence of Unicode characters.  
#   . A list is mutable sequence that can hold elements of any data type.  

# The difference between a tuple and a set:
#   . A tuple is an ordered, immutable collection that allows duplicate elements.  
#   . A set is an unordered, mutable collection of unique, hashable elements.  

# The difference between a set and a string:
#   . A set is an unordered collection of unique, hashable elements.  
#   . A string is an ordered, immutable sequence of characters (duplicate allowed)

# The difference between a tuple and a list:
#   . A tuple is immutable and usually used for fixed collection of items.  
#   . A list is mutable and intended for dynamic collections where items can change.  
# 15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
print(len(set("I am a teacher and I love to inspire and teach people.")))
#  18 unique words have been used in the sentence.   