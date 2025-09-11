# List Exercises
import statistics

# 1. Declare an empty list
lst = ['BMW', 'Cadillac', 'Porche', 'Audi']
empty = []
print(empty)
# 2. Declare a list with more than 5 items 
hardware = ['router', 'switch', 'modem', 'fiber-optic', 'laptop', 'phone', 'Ethernet-cable']
print(len(hardware))
# 4. Get the first item, the middle item and the last item of the list 
print(hardware[0])
print(hardware[len(hardware)//2]) # I know how to fetch the first and last items, but this how you fetch the middle item.  
print(hardware[-1])
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Fanibal", 45 , "5'10", "Married", "744 Val Way"]
print(mixed_data_types)
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon.  
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7. Print the list using print()
print(it_companies)
# 8. Print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company 
print(it_companies[0])
print(it_companies[len(it_companies)//-2])
print(it_companies[-1])
# 10 Print the list after modifying one of the companies 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Amazon']
it_companies[0] = 'Scam' 
print(it_companies)
# 11. Add an IT company to it_companies 
it_companies = ['Facebook', 'Google', 'Amazon', 'Apple', 'Spotify']
it_companies.insert(6, 'Dell') 
print(it_companies)
# 12. Insert an IT company in the middle of the companies list.  
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Dell', 'Spotify', 'Amazon']
it_companies.insert(3, 'Facebook' )
print(it_companies)
# 13. Change one of the it_companies names to uppercase (IBM excluded)
it_companies = ['Facebook', 'Google', 'Amazon', 'IBM', 'Apple', 'Spotify', 'Dell', 'Microsoft']
it_companies[1] = it_companies[1].upper()
print(it_companies)
# 14. Join the it_companies with a string '#; '
it_companies =['Facebook', 'Google', 'Amazon', 'IBM', 'Apple', 'Spotify', 'Dell', 'Microsoft']
it_companies = '#; '.join(it_companies)
print(it_companies)
# 15. Check if a certain company exists in the it_companies list.  
it_companies = ['Facebook', 'Google', 'Amazon', 'IBM', 'Apple', 'Spotify', 'Dell', 'Microsoft']
for it_companies in it_companies: 
        print(f"Yes{it_companies} does exitst in the it_companies list.")
# 16. Sort the list using sort() method 
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Spotify', 'Amazon', 'Microsoft']
it_companies.sort()
print(it_companies)
# 17. Reverse the list in descending order using reverse() method 
it_companies = ['Facebook', 'Google', 'Apple', 'Microsoft', 'Amazon', 'Spotify']
it_companies.sort(reverse=True)
print(it_companies)
# 18. Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies = it_companies[:3]
print(it_companies)
# 19. Slice out the last 3 companies from the list 
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies = it_companies[-3:]
print(it_companies)
# 20. Slice out the middle IT company = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies[-4] = it_companies
print(it_companies)
# 21. Remove the first IT company from the list 
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies.remove 
it_companies.remove('Facebook')
print(it_companies)
# 22. Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies.remove('Dell')
print(it_companies)
# 23. Remove the last IT company from the list 
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies.remove
print(it_companies.remove('spotify'))
# 24. Remove all IT companies from the list 
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies = ['']
print(it_companies)
# 25. Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Apple', 'Dell', 'Microsoft', 'Amazon', 'Spotify']
it_companies.clear() 
print(it_companies)
# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
result = '#; '.join(front_end + back_end)
print(result)
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.  
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end 
full_stack = joined_list.copy()
redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print(full_stack)
# 28. The following is a list of 10 students ages:
# . sort the list and find the min and max age 
# . Add the min age and the max age again to the list
# . Find the median age (one middle item or two middle items divided by two)
# . Find the average age (sum of all items divided by their number)
# . Find the range of the ages (max minus min)
# . Compare the value of (min - average) and (max - average), use abs() method
# To find the mean(average) from a list think of the math formula:
#        sum of all items
# mean = -----------------
#        number of items
#
# sum: add the int you. Ex; 19, 22, 19, 24, 20, 25, 26, 24, 25, 24 add them up to get the sum.  

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages = sorted(ages) 
median_age = statistics.median(ages) # Just learned about the statistics.median() method. I struggled to finish day 5.    
age_range = max(ages) - min(ages)
average_age = sum(ages) / len(ages)

min_diff = abs(min(ages) - average_age)
max_diff = abs(max(ages) - average_age)

print("Sorted ages:", ages)
print(ages)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
print("Min vs average:", round(min_diff, 1))
print("Max vs average:", round(max_diff, 1))   

# List slicing
# 29. Find the middle country(ies) in the countries list. 
# 30. Divide the countries list into two equal lists if it is even if not one more country for the first half.  
countries =['Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
  ]
# Python uses 0-based indexed keep that in mind.  
num_countries = len(countries)

# find the middle country(0-based index)
middle_index = num_countries // 2
middle_country = countries[middle_index]

print(f"Total countries: {num_countries}")
print(f"Middle country: {middle_country}")

# split into halves
if num_countries % 2 == 0:
        # even -> equal halves
        first_half = countries[middle_index + 1]
        second_half = countries[:middle_index]
else:
        # odd -> first half gets one more country
        first_half = countries[:middle_index + 1]
        second_half = countries[:middle_index]

print(f"First half count: {len(first_half)}")
print(f"Second half count: {len(second_half)}")

# Debugging trick: preview contents
print("\nPreview of first half:", first_half[:5], "...")
print("\nPreview of the second half:", second_half[:5], "...")

# 31. # 31. ['China','Russian','USA','Finland','Sweden','Norway','Denmark']. 
# Unpack the first three countries and the rest as scandic countries.

first_country, second_country, third_country, *scandic_countries = countries 

print("First country:", first_half)
print("Second country:", second_half)
print("Third country:", third_country)
print("Scandic countries (the rest):", *scandic_countries[:5], "...") # preview 
print(f"Total scandic countries: {len(scandic_countries)}")

# Valuable pointer: So, if I have a file that has a list of data [], {}, () inside of it and keep it as bare and dynamically read it but I want to just read the data themselves and not modify the data in anyway: means- that file only contains list literal but does not assign it to a variable. Python can't import a bare list, it requires a named object(variable, function, class)
# But if you have a file with a list of data [], {}, () and want to assign the list to a variable: static import.