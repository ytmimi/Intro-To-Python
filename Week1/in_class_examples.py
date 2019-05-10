#!/usr/bin/env python
# coding: utf-8

# # Comments
# Comments in Python are simple.
# Single line comments use a # and multi line comments use ''' '''.

# In[ ]:


# sigle or double quotes work just fine
"""
Multi
Line
comment
"""

# Single line comment


# # Variables
# 
# The excerpt from the following [article](https://realpython.com/python-variables/) does a good job of explaining some of the restrictions when it comes to choosing variable names:
# 
#     "Officially, variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), 
#     digits (0-9), and the underscore character (_). An additional restriction is that, although a variable name can contain 
#     digits, the first character of a variable name cannot be a digit."
# 
# The equal sign ( = ) is the assignment opperator in Python.
# a = 8 means that we're assigning the value 8 to the variable "a"
# Python is a dynamically typed language, which means we never have to declare the "type" of our variables

# In[ ]:


a = 8


# In[ ]:


print(a)


# # Data Types
# There are 4 basic data types in Python
# * Integers (int)
# * Floating-Point Numbers (float)
# * Strings (str)
# * Booleans (bool)

# You can check the type of an object with the built in type function

# In[ ]:


type(45)


# In[ ]:


type(22.7)


# In[ ]:


type('Python is awesome')


# In[ ]:


type(True)


# ## Numbers (Ints and Floats)
# The main difference between floats and ints is that integers are whole numbers and floats have decimals

# ### Mathematical Operators
# * add (+)
# * subtract (-)
# * multiply (*)
# * divide (/)
# * floor division (//)
# * modul (%)
# * power (**)

# In[ ]:


# + adds two numbers together
5 + 5


# In[ ]:


# - is used for subtraction
5 - 6


# In[ ]:


# * is used to mutiply two numbers together
8 * 9


# In[ ]:


# / is used for division. In python 3 this will always return a Float even if the numbers strat with are both integers
16 / 4


# In[ ]:


# // is used for floor division and will throw away any remainder


# In[ ]:


9 / 5


# In[ ]:


9 // 5


# In[ ]:


# % is used to return the remainder of after dividing (is useful for determining whether a number is even or odd)


# In[ ]:


5 % 2


# In[ ]:


# ** is used to raise numbers to a certain power
2 ** 3


# It might not be immideately obvious, but each of these mathematical operations returned a value. For example 16 / 4 returned 4. If you wanted to you could store the result in a variable

# In[ ]:


b = 8 + 7


# In[ ]:


b


# ### [Standard Library Functions](https://docs.python.org/3/library/functions.html)
# One of the things that makes Python so great is the Standard Library. This is a set of Packages and functions that you get for free once you install Python. Python is sometimes referred to as having batteries included and it's largely due to the awesome (and useful) tools in the Standard Library.
# 
# Some useful function for mathematical operations and comparisons include:
# * min 
# * max
# * sum
# * round

# In[ ]:


# as you would expect, min returns the smallest number in a collection
min(4, 6, 99, 32, -7, 2)


# In[ ]:


# similarly, max returns the largest number in a collection
max(5, 6, 99, 32, -7, 2)


# In[ ]:


# sum will return the sum of numbers in a collection, here we sum a list of numbers
sum([5, 6, 99, 32, -7, 2])


# In[ ]:


# round will round a decimal number to a specified amount of digits
round(4.59421, 2)


# ## Strings
# Strings are another basic data type in Python and can either be created using single or double quotes
# 
# for example, 'this is a string' and "this is also a string"
# 
# it doesn't matter whether you use single or double quotes, but for styling it's a good idea to stay consistent

# In[ ]:


'this is a string'


# In[ ]:


"This is also a string"


# ### Strings and Operators
# surprisingly, strings also use the + and * operator

# In[ ]:


# using the + operator will concatenate two strings
'hello' + ' world!'


# In[ ]:


# variables that are strings can also be used when concatenating strings
flower = 'rose'
'the '+ flower +' is red' 


# **Note that using concatenation to format strings isn't advised because the syntax is clunky.You have to manually add spaces between the things you want to combine, and it only becomes harder to reason about once you start adding many variables. Don't worry, there is a better way**

# In[ ]:


# trying to concatenate something that isn't a string with a string will result in an error

'I am '+ 24 + ' years old!'


# In[ ]:


# you'll have to cast the object to a string for concatenation to work
# Again, this is another reason why string concatenation isn't great for formating strings. It's error prone.

'I am ' + str(24) + ' year old'


# In[ ]:


# using the * operator the string will be repeated

'%' * 50


# ### String Slicing
# 
# String slicing if a useful feature  that helps us get single characters from a string, or entire chuncks of a string.
# It's important to note that indexing starts at zero
# 
# Slicing syntax uses brackst [] and takes 3 colon seperated arguments [start:stop:step] where start is the first character of the slice, stop is where slicing stops but is not included in the slice, and step is the frequency of the slice
# 
# excluding stop and step arguments will return a single character at the index position specified

# In[ ]:


my_string = "Some really long and really random string"


# In[ ]:


# Again remember that indexing starts at zero, so slicing the string on the first (zeroth index) will return "S"
my_string[0]


# In[ ]:


# Adding the stop argument will return a slice up to, but not including, the stop argument
my_string[5:10]


# In[ ]:


# adding the step argument will determin the frequency of the characters that are returned, for example 3 will return every 3rd character
my_string[0:24:3]


# In[ ]:


# if stop is left blank the slice will continue to the end of the string
my_string[16:]


# In[ ]:


# stop can also be left blank while providing a step frequency
my_string[16::2]


# In[ ]:


# You can also leave the start argument blank and it will continue to the stop
my_string[:10]


# In[ ]:


# Another really convenient feature of slicing is that you can perform negative slicing to return values from the end of the string
my_string[-1]


# In[ ]:


# you can also take slices using negative indexing
my_string[-12:-3]


# In[ ]:


# you can also step using a negaitve number to reverse the string
my_string[::-1]


# ### String Formatting
# 
# Way better alternatives to string concatenation

# string objects have a built in `format` method. placeholders can be placed using {} and a list of objects can be provided to the fromat method

# In[ ]:


weekday = 'Monday'

'{} is the worst'.format(weekday)


# As of Python 3.6, "f" strings were introduced. you create them by prepending f to the front of a string. Similarly to the format method you can add placeholders with {}, but you place the object directly into the placeholder

# In[ ]:


f'{weekday} is the worst'


# expressions can also be evaluated in "f" strings

# In[ ]:


f'32 + 4 = {32 + 4}'


# ### String Methods
# 
# We've already seen that strings have a format method that can be called on them. There are other methods you can call on strings.
# 
# * replace
# * endswith
# * startswith
# * join
# * lower
# * upper
# * ...etc

# In[ ]:


# replace is used to replace a set of characters in a string
best_day = 'Thursday'
best_day.replace('Thurs', 'Fri')


# In[ ]:


# endswith returns True or False whether a string ends with the specified characters
url = 'yahoo.com'
url.endswith('.com')


# In[ ]:


# similarly starts with returns True or False if a string starts with some specified character
man = 'Mr. Smith'
man.startswith('Mrs.')


# In[ ]:


# join takes a list of strings as an argument and joins them together on the given characters
colors = ['red', 'blue', 'green', 'yellow']
' -- '.join(colors)


# In[ ]:


# lower returns the same string all in lower case. Good for case insensitive checks
upper_case_words = 'JUST A BUNCH OF UPPER CASE WORDS'
upper_case_words.lower()


# In[ ]:


# upper returns the same string all in upper case. Also, good for case insensitve checks
lower_case_words = 'all lower case'
lower_case_words.upper()


# ### Some usefull built in functions that you can use with strings
# 
# * print
# * len

# In[ ]:


# print will print the string to the console. By default the Jupyter Notebook will display the value of the last value in the cell
print('Hey there')


# In[ ]:


# len will return the length of the string, it actually works with other objects as well, but we'll get into that later
len('some reallllllllllyyyyyyyyyyyyyy loooooooonnnnnnnnggggggg  sssssttttrrrrriiiiiinnnnngggg')


# ## Booleans
# A boolean is either True or False

# ### Logical (comparison) Operators
# 
# * equal ==
# * not equal !=
# * greater than >
# * greater than or equal >=
# * less than <
# * less than or equal <=
# 
# **We'll cover these later**
# * is -- checks if two objects are the same
# * in -- checks if an object is in a collection of objects 

# In[ ]:


# to check if 2 objects are equal
2 == 4


# In[ ]:


# to check if 2 objects are not equal
'one' != 'two'


# In[ ]:


# Strings compares the first character in alphabetical order
'400' > '7'


# In[ ]:


400 > 7


# In[ ]:


45 >= 44


# In[ ]:


# Some operators don't work when trying to compare objects of different types
a = 7
b = '23'
a >= b


# In[ ]:


# But you can often check equality
a == b


# In[ ]:





# ### if else, elif
# You can use comparison operators with if else and elif keywords to control the flow of your program and execute differnt code when different conditions are met

# In[ ]:


# The code in the if block if the check evaluates to True
if True:
    print('It must be true')


# In[ ]:


# When including an else block the code will only run if the if check evaluates to False
if len('34') > 7:
    print('What a long number')
else:
    print('eh')


# In[ ]:


# you can extend the number of checks that are performed before reaching the else block by adding elif (else if)
email = 'something@horizonmedia.com'
if email.endswith('gmail.com'):
    print('GOOGLE')
elif email[4:9] == 'thing':
    print('something')
else:
    print('nothing')


# In[ ]:


# you can add as many elif checks that you want
if 1 + 5 > 10:
    print('one')
elif bool(0):
    print('two')
elif True:
    print('three')
else:
    print('four')


# It's important to note that if the "if" check evaluates to True, no other elif statements will be checked
# Similarly, the first elif to evaluate to True will prevent any following elif statements from being checked
