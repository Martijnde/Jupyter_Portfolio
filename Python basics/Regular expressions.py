#A regular expression is a sequence of characters that describes a search pattern.

#In practice, we say that certain strings match a regular expression if the pattern can be found anywhere within those strings (as a substring). 
#The simplest example of regular expressions is an ordinary sequence of characters. Any string that contains that sequence of characters, 
#all adjacent and in the proper order, is said to match that regular expression. Here are a couple examples:

#Assign a regular expression that is 4 characters long and matches every string in strings to the variable regex
strings = ["data science", "big data", "metadata"]
regex = ""
regex = "data"


#We assign a regular expression (3 characters long) that matches every string in strings to the variable regex
strings = ["bat", "robotics", "megabyte"]
regex = "."
regex = "b.t"


#We can use "^" to match the start of a string and "$" to match the end of string.
#"^a" will match all strings that start with "a".
#"a$" will match all strings that end with "a".
#You can use any combination of special characters in a regex. Let's combine what we've learned so far to create some more advanced regular expressions



#Assign a regular expression that is 7 characters long and matches every string in strings, but not bad_string, to the variable regex
strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"