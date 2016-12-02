#In the last mission, we worked with with legislators.csv, which contains information on every historical US Congressperson. 
#In the last mission, we cleaned up some missing data and added an additional birth year column.
#We'll continue to work with the same dataset in this mission. Here's the beginning of the dataset, in csv format:
last_name -- the last name of the Congressperson.
•first_name -- the first name of the Congressperson.
•birthday -- the birthday of the Congressperson.
•gender -- the gender of the Congressperson.
•type -- whether the Congressperson was in the Senate (sen), or in the House of Representatives (rep).
•state -- the state the Congressperson represents.
•party -- the party affiliation of the Congressperson.
•birth_year -- the year the Congressperson was born. This column is an integer value.

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
#Enumerate the ships list using a for loop and the enumerate() function.
#In each iteration of the loop:Print the item from ships at the current index
#Print the item from cars at the current index.
for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

	
things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
#Loop through each row in things using the enumerate() function.
#Append the item in trees with the same index to the end of each row in things.
#At the end, things should have an extra column
for i, thing in enumerate(things):
    thing.append(trees[i])


apple_prices = [100, 101, 102, 105]
#Create a new list called apple_prices_doubled where each item in apple_prices is multiplied by 2
apple_prices_doubled = [(price * 2) for price in apple_prices]
#Create a new list called apple_prices_lowered where 100 is subtracted from each item in apple_prices
apple_prices_lowered = [(price - 100) for price in apple_prices]


#Create an empty dictionary called name_counts.
#Loop through each row in legislators.
#If the gender column of the row equals F and the year column of the row is greater than 1940:
#Assign the first_name column of the row to the variable name.
#If name is in name_counts:◾Add 1 to the value associated with name in name_counts.
#If name isn't in name_counts:◾Set the value associated with name in name_counts to 1.
#When the loop finishes, name_counts should contain each unique name in the first_name column of legislators 
#as a key, and the corresponding number of times it appeared as the value.
name_counts = {}
for row in legislators :  
    gender = row[3]
    year = row[7]
    if gender == "F" and year > 1940 :
        name = row[1]
        if name in name_counts :
            name_counts[name] = name_counts[name] + 1
        else :
            name_counts[name] = 1
			
print(name_counts)


#Loop through each value in values. Check to see if the value is not None and the value is greater than 30.
#Append the result of the check to checks.
#At the end, checks should be a list of Booleans that indicate whether or not the corresponding item in values
#is not None and greater than 30.
values = [None, 10, 20, 30, None, 50]
checks = []
checks = [x is not None and x > 30 for x in values]


#Set max_value to None
#Loop through the keys in name_counts
#Assign the value associated with the key to count
#If max_value is None, or count is greater than max_value:Assign count to max_value.
#At the end of the loop, max_value will contain the largest value in name_counts
max_value = None
for k in name_counts:
    count = name_counts[k]
    if max_value is None or count > max_value:
        max_value = count
return(max_value)


#Use the items() method to iterate through the keys and values in plant_types.
#Print each key in plant_types. Print each value in plant_types
plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for k,v in plant_types.items():
    print(k)
    print(v)
return(plant_types)

#Loop through the keys in name_counts.
#If any value in name_counts equals 2, append the key to top_female_names.
#At the end, top_female_names will be a list of the most common names of female legislators.
top_female_names = [k for k in name_counts if name_counts[k] == 2]

Same trick, for male names:

top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1

highest_value = None
for name,count in male_name_counts.items():
    if highest_value is None or count > highest_value:
        highest_value = count

for name,count in male_name_counts.items():
    if count == highest_value:
        top_male_names.append(name)

