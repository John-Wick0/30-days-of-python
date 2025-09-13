# Exercises

# 1. Concatenate the string 'Thirty','Days','Of','Python' to a single string, 'Thirty Days of Python'

word = 'Thirty', 'Days', 'Of', 'Python'
result = ' '.join(word )

#print(result)

# 2. Concaternate the string 'Coding','For','All' to a single string, 'Coding For All' 

second_word = 'Coding','For','All'
result = " ".join(second_word)
print(result)

# 3. Declare a variable named company and assign it to an initial value "Coding For All". 
company = "Coding For All"
# 4. Print the variable company using the print() method. 
print(company)
# 5. Print the length of the company string using the len() method and print() 
print(len(company))
# 6. Change all the characters to capital letters using upper() method. 
print(company.upper()) 
# 7. Change all the characters to lowercase letters using the lower() method.  
print(company.lower())
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.  
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Damn this is easier than I thought!
# 9. Cut(slice) out of the first word of 'Coding For All' string.  
text = 'Coding For All'
print(text[:-7])
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.  
company = 'Coding For All'
print(company.index(('Coding')))# This written code would not work because it is a tuple instead of a str.
print(text.index('Coding')) # index raises an error
print(text.find('Coding')) # find returns -1
# p.s: find and index returned 0 because substring 'Coding' starts at position 0 in 'Coding For All'. 
# 11. Replace the word coding in the string 'Coding For All' to Python.  
text = 'Coding For All'
print(text.replace('Coding', 'Python'))
# 12. Change Python for Everyone to Python For All using the replace or other methods.  
text = 'Python for Everyone'
print(text.replace('for Everyone', 'For All'))
# 13. Split the string 'Coding For All' using space as the separator (split()). 
# I just did some research and learned I could have also used split('') too. But split() is better for normal sentences.  
text = 'Coding For All'
words = text.split('Coding For All')
print(words)
# The split('') method variation
text =  'Coding For All.'
words = text.split(', ')
print(words)
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.  
web = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
web_goons = web.split(', ')
print(web_goons)
# 15. What is the character at index 0 in the string Coding For All
char = 'Coding For All.'
print(char[0]) 
# 16. What is the last index of the str Coding For All.  
last_index = 'Coding For All.'
print(last_index[-1])
# 17. What character is at index 10 in "Coding For All" str.  
char = "Coding For All"
print(char[10]) # there's no character at index 10 but a space, and also it depends where you start couting. In this case I seem to start counting on index 0.  
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.   
name = 'Python For Everyone'
abreviation = 'P.F.E'
print(abreviation)
# 19. Create an acronym or abbreviation for the name 'Coding For All'.
name = 'Coding For All.'
abreviation = 'C.F.A'
print(abreviation)
# 20. Use index to determine the position of the first occurence of C in Coding For All.  
text = 'Coding For All.'
print(text.index('C'))
# 21. Use index to determine the position of the first occurrence of F in Coding For All.  
text = 'Coding For All.'
print(text.index('F'))
# 22. Use rfind to determine the position of the last occurrence of L in Coding For All People.  
text = 'Coding For All People.'
print(text.rfind('l'))
# 23. Use rindex or find to find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is a
# conjunction'
# The last occurrence as in the last time the word or phrase etc comes up in a sentence or words.  
sentence = 'You cannot end a sentence with because because because is a conjunction'
#print(sentence.rindex('because'))
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot
# end a sentence with because because because is a conjunction'  
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'
start = sentence.find(phrase)
end = start + len(phrase)
sliced = sentence[start:end]
print(sliced)
# 26. Find the position of the first occurrence of the word 'because' in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction' 
sentence = 'You cannot end a sentence with because because because is a conjuntion'
word = 'because'
position = sentence.find('because')
print(position)
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot
# end a sentence with because because because is a conjunction'  
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'
start = sentence.find(phrase)
end = start + len(phrase)
sliced = sentence[start:end]
print(sliced)
# 28. Does "Coding For All" start with a substring Coding?
sentence = "Coding For All"
print(sentence.startswith('Coding'))
# 29. Does "Coding For All" end with a substring coding?
sententce = 'Coding For All'
print(sentence.endswith('Coding'))
# 30. ' Coding For All ' , remove the left and right trailing spaces in the given string.  
# Remember preffix and suffix have two different meanings.
sentence = ' Coding For All  '
cleaned = sentence.strip()
print(cleaned)
# 30. Which one of the following variables return True when we use the method isidentifier():
#   . 30DaysOfPython
#   . thirty_days_of_python
first_sentence = '30DaysOfPython'
second_sentence = 'thirty_days_of_python'
print(first_sentence.isidentifier())
print(second_sentence.isidentifier())
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask',
# 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string 
libraries = ['Django','Flask','Bottle','Pyramid','Falcon']
result = ' '.join(f'#{libraries}' for libraries in libraries)
print(result)
# 33. Use the new line escape sequence to separate the following sentences.  
#   I am enjoying this challenge.  
#   I just wonder what is next.   
sentences = 'I am enjoying this challenge. I wonder what is next.'
result = 'I am enjoying this challenge.\nI wonder what is next.'
print(result)
# 34. Use a tab escape sequence to write the following lines.  
# Name   Age  Country
# Fanibal 45  Iceland 
print("Name\tAge\tCountry")
print("Fanibal\t45\tIceland")
name = 'Fanibal'  
age = '45'     
country = 'Iceland'
print(f"{name}\t{age}\t{country}")
# 35. Use the string formating method to display the following:
radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius is 314 meters square.
#radius = 10 
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))
# 36. Make the following using string format methods:
8 + 6 = 14 
8 - 6 = 2
8 * 6 = 48 
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144 
# You can use .format() or f"{}
addition = (8 + 6)
a = 8 
b = 6 
print("{} + {}".format(a, b, result))


subtraction = (8 - 6)
a = 8 
b = 6 
result = 8 - 6 
print("{} - {}".format(a, b, result))


multiplication = 8 * 6 
a = 8 
b = 6 
result = a * b   
print("{} + {}".format(a, b, result))


Division = 8 / 6 
a = 8 
b = 6 
result = a / b   
print("{} / {}".format(a, b, result))

Modulus = 8 % 6  
a = 8 
b = 6  
result = a % b   
print("{} % {}".format(a, b, result))

Floor_division = 8 // 6
a = 8 
b = 6 
result = a // b   
print("{} // {}".format(a, b, result))

Exponentiation = 8 ** 6
a = 8 
b = 6  
result = a ** b   
print("{} ** {}".format(a, b, result))

# Comeback later tonight and continue... The Grind don't stop!
# For tonight finish: day5 -> day8. Then Get up early tomorrow (@7:30-8am) and continue....