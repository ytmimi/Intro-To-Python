#!/usr/bin/env python
# coding: utf-8

# # Recap Last Week
# 
# **we covered:**
# * comments
# * variables
# * basic data types
# * mathematical operators
# * string formatting
# * and conditional logic

# In[ ]:


# print('hello')


# In[ ]:


hy = 8
print(hy)


# In[ ]:


my_string = 'this is a string'
type(my_string)


# In[ ]:


my_int = 8
type(my_int)


# In[ ]:


my_float = 8.8
type(my_float)


# In[ ]:


# if elif else


# In[ ]:


if 5 > 4:
    print('nice')


# In[ ]:


if 5 < 4:
    print('hey')
else:
    pass


# In[ ]:


if len('6') > 2:
    print('2')
elif 2 == 5:
    print('next')
elif 3 == 3:
    print('winner')
else:
   pass 


# ## What we missed (my bad)
# There are three other keywords Python allows you to use when determining the truth value of an expression
# 
# * and
#     * True if both expression being checked evaluate to True, otherwise it's False
# * or 
#     * True if either expression being checked is True. Flase when both expression are False
# * not
#     * Negate the truth value of an expression

# In[ ]:


# using and
print(f'True and True results in {True and True}')
print(f'True and False results in {True and False}')
print(f'False and True results in {False and True}')
print(f'False and False results in {False and False}')


# In[ ]:


# uisng or
print(f'True or True results in {True or True}')
print(f'True or False results in {True or False}')
print(f'False or True results in {False or True}')
print(f'False or False results in {False or False}')


# In[ ]:


# using not
false_expression = 53 < 2
print(f'Using "not" turns a {false_expression} expression into a {not false_expression} expression')

ture_expression = len('123') == 3
print(f'Using "not" turns a {ture_expression} expression into a {not ture_expression} expression')


# **You can combine these logical keywords as much as you want**
# 
# **Note: You can also add () to indicate to python how you want expression to be grouped**

# In[ ]:


today = 'Monday'
tomorrow = 'Wednesday'
weather = 'Sunny'

if (today == 'Monday' or tomorrow == 'Sunday') and weather == 'Sunny':
    print('Going for a walk in the park')
elif not tomrrow == 'Tuesday' or weather == 'cloudy':
    print('watching movies')
else:
    print('Gotta cook dinner')


# # Data Structures
# 
# There are 4 main data types in Python
# * List
# * Dictionary
# * Set
# * Tuple

# ## Lists
# Lists are one of the most commonly used data structures in Python. Lists can contain any Python object, and the elements within the list are comma seperated. One thing to note about lists is that they are ordered, and elements within a list can be referenced by there position (index) within the list. There are many ways to create a list, but the most common is using [] syntax.

# ### Creating a list

# In[ ]:


# using []
week_days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
print(week_days)


# In[ ]:


# Lists can also contain elements with different data types
mixed = [1, 3.5, True, 'end']
print(mixed)


# In[ ]:


# other data structures can also be contained inside of a list. A list within a list...listseption
matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
print(matrix)


# ### List Indexing
# 
# As previously mentioned, lists are an ordered data structure and the items within the list can be referenced by their index within the list. It's important to remember that indexing starts at zero.

# In[ ]:


subjects = ['English', 'Computer Science', 'Finance', 'Marketing', 'Biology', 'Music', 'Art']
print(subjects)


# In[ ]:


# accessing the first index in the list
print(subjects[-1])


# ### List Slicing

# Lists also support slicing notation to access subsets of the list

# In[ ]:


print(subjects[4::])


# Slicing also works with nested lists. To demonstate this we'll use the matrix we defined above

# In[ ]:


# Note that the first entry in matrix is a list [1, 2, 3]
print(matrix[0])


# you can slice as deep as the data strucure will allow

# In[ ]:


# so matrix[1] returns [4, 5, 6], and then we get the 2nd index from that list (6). remember that indexing starts at 0
first_index = matrix[1]
print(first_index)
second_index = first_index[2]
print(second_index)

matrix[1][2]


# ### Some List Methods

# You can add items to a list using the append method

# In[ ]:


week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(week_days)


# In[ ]:


week_days.append('day-8')
print(week_days)


# You can remove and return an item from a list with the pop method

# In[ ]:


last = week_days.pop()
print(last)


# In[ ]:


print(week_days)


# To find the index of an element in a list you can use index method

# In[ ]:


print(week_days.index('Tuesday'))


# You can remove and return a specific element by supplying the index as an argument to the pop method

# In[ ]:


tues = week_days.pop(week_days.index('Tuesday'))
print(tues)


# In[ ]:


# as you can see 'tue' is no longer in the week_days list
print(week_days)


# You can insert an item into a specific place using the insert method

# In[ ]:


week_days.insert(1, 'Tuesday')
print(week_days)


# You can find the lenght of a list using the built in len function

# In[ ]:


num_days = len(week_days)
print(num_days)


# ## Dictionaries
# Another really common data structure in Python is a dictionary (dict). Dictionaries represent mappings of key value pairs, where the value can be any python object. Although in later versions of Python the order that keys are inserted into the dictionary is maintained, dictionaries are an inherintly unordered data structure. Dictionareis are constrcuted using curly brackets -- { } -- and take the form: {key1:value1, key2:value2, ...}. Each key value pair in the dictionary is comma (,) seperated

# ### Creating a dictionary

# In[ ]:


birthday = {
    'Yacin':'Feb 2',
    'Andrew': 'Oct 29',
    'Brian': 'Jun 7',
    'Sarah': 'Aug 18',
}


# ### Accessing values from a dictionary

# Accessing elements in a dictionary can be done in two ways. The syntax for the first and most common way to access a value from a dictionary is as follows:
#         
#         dictionary[key]
# 
# This may resemble slicing notation, accept you can't access items based on an index. Instead you use the key associated with an item in the dictionary to access it.

# In[ ]:


birthday['Brian']


# Trying to access a value using a key that's not in the dictionary will raise a KeyError.

# In[ ]:


birthday['Mike']


# The second way to access the values stored in a dictionary is using the `get` method. This has the advantage of allowing you to return a default value if none is found

# In[ ]:


birthday.get('Andrew')


# the get method takes a second optional argument that defaults to None, which specifies the default value to return if the key doesn't exist. Using the get method you can ensure that a KeyError wont be raised

# In[ ]:


birthday.get('Sam', 'Sep 4')


# Similar to lists, the values of a dictionary can be any Python object. Dictionaries can get as nested and complex as you'd like

# In[ ]:


people = {
    'Josh':{
        'birthday': 'Mar 13',
        'height': 64,
        'age':25,
    },
    
    'Liz':{
        'birthday': 'Mar 13',
        'height': 70,
        'age':36,
    },
    
    'Dan':{
        'birthday': 'Dec 25',
        'height': 65,
        'age':15,
    }
    
}


# Again, the data structure can be nested. We access the value of a dictionary by referencing it's key

# In[ ]:


# As you might expect we get returned the nested dictionary for 'Liz'
people['Liz']


# You can traverse the dictionary in one line by continuing to reference keys till you've reached the value you want to get at

# In[ ]:


# we can get at Liz's height by using the [] notation twice
people['Liz']['height']


# In[ ]:


# you can also use the get method
people.get('Dan').get('birthday')


# In[ ]:


# you can combine the [] and get method
people['Josh'].get('age')


# ### Adding values to a dictionary

# In[ ]:


# create a new dictionary with two keys summer and spring
seasons = {
    'summer':1,
    'spring':2
}


# You can add values to a dictoinary in several wasy. First you can use the \[key\] syntax along with an = to assign a value to the key. If the key doesn't exist a new key value pair will be created in the dictionary. If the value already exists in the dictionary, you'll override the old value with the new one

# In[ ]:


seasons['fall'] = 3
print(seasons)


# You can also add values to a dictionay using the update method. where you supply a list of key word arguments to the function. The update method is more useful if you need to update many keys in a dictionary at once, otherwise you should use the [] syntax for assigning new values to a dictionary

# In[ ]:


seasons.update(winter=4, summer=5, spring=7)
seasons


# ### Removing values from a dictionary
# In order to remove a single element from a dictionary use Python's built in del keyword 

# In[ ]:


# remove spring from the dictionary
del seasons['spring']
seasons


# In[ ]:


# tyring to remove a key that does not exist in the dictionary will result in a KeyError
del seasons['spring']


# If you want to make a copy of a dictionary you can do so using the copy method, and if you want to remove all keys you can using the clear method

# In[ ]:


season_copy = seasons.copy()
print(f'Copy -- {season_copy}')
print(f'Original -- {seasons}')


# In[ ]:


season_copy.clear()
print(f'Copy -- {season_copy}')
print(f'Original -- {seasons}')


# ### Other useful Dict methods
# * keys
# * values
# * items

# In[ ]:


# return just the keys from a dictionary
seasons.keys()


# In[ ]:


# return just the values from a dictionary
seasons.values()


# In[ ]:


# return a Tuple of keys and values
seasons.items()


# In[ ]:


# return the number of keys in the dictionary
len(people)


# ## Sets
# 
# A set is another basic data type in Python. Sets are a unique collection of items. Sets are an unordered data type. Sets don't use keys, and they don't support indexing so you won't be able to access individual items within a set. Similar to dictionaries, sets are also contructed using {}
# 
# Although sets are a basic data type in Python I rarely use them, however they come in extreamly handy when you want to ensure that you're working with a unique group of items

# In[ ]:


fruit = {'apples', 'bananas', 'orange'}


# In[ ]:


# trying to access an element by its index raises an error
fruit['apples']


# In[ ]:


fruit[0]


# In[ ]:


# you can use the logical in operator to check if an item is contained in a list
'apples' in fruit


# Once a set is created you can't replace items in it. You can only ever add or remove items from the set

# ### add items to a set using the add method

# In[ ]:


fruit.add('pear')
fruit


# Because sets are unique trying to add the same item twice will have no effect

# In[ ]:


fruit.add('pear')
fruit


# ### remove items from a set using the remove method
# 
# **Note: trying to remove an item that doesn't exist will raise an error**

# In[ ]:


fruit.remove('orange')
fruit


# In[ ]:


fruit.remove('tomatoes')


# As I mentioned, sets are a data structure that you won't use that often. If you want to learn more about what you can do with sets check out this [link](https://www.w3schools.com/python/python_sets.asp)

# ## Tuples
# 
# Tuples are the fourth basic data structure in Python. They are similar to lists in that they are an ordered data structure that supports indexing, however once a tuple is created it can never be changed. Tuples are known as an immutable data structure. Actually you've already worked with immutable data structurs and you didn't even know it. Python's String object is an immutable data structure. Strings can never be altered directly, but they can be joined and sliced to create new strings. Tuples are constructed using ()

# In[ ]:


my_string = 'asdfasdf'
my_string[2] = 'y'


# In[ ]:


# create a new tuple object
zip_codes = (10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010)


# In[ ]:


# tuples supoort indexing. Remember, indexing starts at zero
zip_codes[1]


# In[ ]:


# tuples will throw an error if you try to reassign any of their objects


# In[ ]:


zip_codes[-1] = 10011


# ### Tuple methods
# 
# Tuples only have two methods 
# * index
# * count

# In[ ]:


# index return the index of the given value
zip_codes.index(10009)


# In[ ]:


# count returns the number of times the given object appears in the tuple
zip_codes.count(10001)


# In[ ]:


nums = (1, 2, 1, 2, 1, 2, 1, 2, 1,)
nums.count(1)


# In[ ]:





# # Looping
# 
# Looping is useful when you want to perform the same task multiple times

# ## For Loops
# 
# Use for loops when you know that you will only need to loop a finite number of time. So in cases where you have a collection of items
# For loop syntax is as follows:
#     
#     for item in colletion:
#         do something
# 
# **In the above example, "item" is a variable that you can name anything you want. you'll have access to this variable within the loop, similarly collection can be any collection of python objects**
# 
# **Note that the indentation matters. The code written in the indented block of the for loop will be evaluated on each iteration of the loop** 

# In[ ]:


# looping over a list of numbers
for num in [1, 2, 3, 4, 5, 6]:
    print(num)


# In[ ]:


# looping over a dictionary will loop over the keys
my_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six'}

for key in my_dict:
    print(my_dict[key])


# You can write whatever code you want in the body of the loop. You can change which code gets evaluated using conditional logic inside the loop

# In[ ]:


for num in [1, 2, 3, 4, 5, 6]:
    if num == 1:
        print('If block gets executed')
    elif 2 <= num <= 4:
        print('elif block gets executed')
    else:
        print('else block gets executed')


# In[ ]:


for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    if day in ['Friday', 'Saturday']:
        print(f'I love {day}')
    elif day in ['Wednesday', 'Thursday']:
        print(f'{day} is okay')
    else:
        print(f'I hate {day}')


# **you'll typically use lists in your for loops (or at least I typically do), but that doesn't mean that lists are the only thing you can iterate over. As you saw in one of the examples above we were also able to loop over a dictionary. We're able to loop over these objects becuase these objects are iterable. It's not supper important that you understnad what makes an object in Python iterable, but don't worry, we'll cover it in a futrue class. For now I just want you to realize that there are many objects that you can loop (or iterate) over. Another type of iterable in python is a generator. Again, not supper important that you understand what a generator is just yet, but know that you can loop over them.**

# You can easily create a generator using python's range function. The arguments that the range function takes are similar to the slice arguments (start, stop, and step)

# In[ ]:


# if only one argument is passed it is assuemed to be the end, start defaults to 0 and step defaults to 1. Just like slicing this is not inclusive of the stop
for num in range(5):
    print(num)


# In[ ]:


# if two arguments are passed the first is the start and the second is the stop
for num in range(3, 8):
    print(num)


# In[ ]:


# three arguments indicate start, stop, and step
for num in range(0, 10, 2):
    print(num)


# In[ ]:


for i in range(5):
    for j in range(5):
        print(i, j)


# ### Looping over other data structures

# In[ ]:


# looping over a dict
simple_dict = {'one':1, 'two':2, 'three':3}
for value in simple_dict:
    print(value)


# **Note: looping over a dictionary returns its keys**

# In[ ]:


# looping over a set
simple_set = {1, 2, 3,}
for value in simple_set:
    print(value)


# In[ ]:


# looping over a tuple
simple_tuple = (1, 2, 3)
for value in simple_tuple:
    print(value)


# ## While Loops
# 
# while loops are used when you don't know how many times you are going to iterate. The code in the while loop will continue to execute while the condition being checked by the while loop remains True. while loop syntax is as follws:
# 
#         While "some condition":
#             run some code
#             updat the condition
# 
# **It's important to note that if you set up a while loop with a condtion that will always evaluate to true then you will get stuck in an infinite loop. If this happens don't pannic, you'll just have to manually terminate the code being run. In jupyter you should be able to interrupt the kernel by clicking on kernel in the tool bar and selecting interupt kernal. Aleternatively go to the command line where the server is running and hit ctr + c. This will kill the jupyter server. You'll have to rerun the server using the Jupyter lab command, and rerun all the cells in the notebook to get back to where you were. Remember to fix the infine loop before rerunning all the cells**

# In[ ]:


# in this example we
num = 0
while num < 10:
    print(num)
    num +=1


# In[ ]:


text = 'Hello World'
index = 0
while text[index] != 'r':
    print(text[index])
    index += 1


# If you do set up a loop condition that will always evaluate to True, make sure that there is some code that will be executed that leads to a break keyword.
# The break keyword can be used to break out of the current block of code and continue execution of the program.

# In[ ]:


while True:
    break
print('outside the while loop')

