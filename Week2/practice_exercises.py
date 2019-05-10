#!/usr/bin/env python
# coding: utf-8

# ## The following questions cover week 1 material

# **1) What are the 4 basic data types in Python?**

# *write your response*

# **2 A) What does the % operator do?**

# *write your response*

# **2 B) Use the % operator in an expression that returns 7**

# In[5]:


# return 7 using %


# **3 A) Assign the string `"Actions speak louder than words."` to a variable**

# In[2]:


# assign to a variable


# **3 B) Use indexing to return the first character of the first word**

# In[3]:


#string indexing


# **3 C) Use negative string indexing to return the first character of the last word**

# In[4]:


#string indexing


# **3 D) Use string slicing to return the word `"louder"`, and use a built in string method to convert `"louder"` into `"LOUDER"`. Preferably perform both operations on one line**

# In[7]:


# return "LOUDER"


# **3 E) Using all the characters in the string above and string indexing, figure out how to create the word `"done"`. finaly print it out to the screen**
# 
# **BONUS: Use string concatenation, .format method, and f strings. print each solution out from the same cell**

# In[ ]:


# get word "done"


# **4 A) What are the two Python keywords used for boolean objects?**

# *write your response*

# **4 B) What are the three Python keywords used to evaluate boolean expressions, and what are there differences. Please indicate whether any of them are optional when using them together. HINT: one of them is `"if"`.**

# *write your response*

# **5 A) Use the if statement. Write any condition that evaluates to True. In the body of the if block print any text you'd like**

# In[10]:


# use the if statement


# **5 B) Use if and else. Check two conditions in the if statement using Python's `"and"` keyword. In the body of both the if and the else block print out any text you'd like. Make sure only the print statemnt in the else block is printed**

# In[ ]:


# use if and else 


# **5 C) Use the if, 2 elif's and an else statement.** 
# * Use the `"or"` keyword in the if
# * Use the `"and"` keyword in the first elif
# * Use the `"not"` keyword in the second elif
# **write any code you want in the body of each conditional block. Make sure that the code in the second elif is evaluated**

# ## The following questions cover week 2 material

# **6 A) How do you create a list in Python? Are there any restrictions on the objects that can be contained within a list?**

# *write your response*

# **6 B) Create a list containing the numbers 0-9, and store it in some variable, then print out the length of the list**

# In[11]:


# create the list


# **6 C) Are lists an ordered or unordered data structure? When indexing into a list where does indexing start?**

# *write your response*

# **6 D) Use the list from part B. Use slicing notation to return the numbers 0, 2, 4, 6, 8**

# In[12]:


# return [0, 2, 4, 6, 8]


# **7) Given the two following to do lists answer the following questions**
# 
# **IF you make a mistake at on any point in this problem just rerun all the cells starting from here**

# In[ ]:


#given to do lists
todays_list = []
tomorrows_list = []


# **7 A) Add the following strings to todays_list one at a time: `"Work"`, `"Python"`, `"Sleep"`, `"Repeat"`** 
# 
# **HINT: [append](https://www.programiz.com/python-programming/methods/list/append) would probably be a good idea**

# In[13]:


# add items to the list


# **7 B) Return the index of "Sleep" in the list**

# In[14]:


# find the index


# **7 C)You decide you can do without "Sleep", and would rather replace it with "More Python". Reassign the index of "Sleep" in the list to "More Python".**
# 
# **Note: I don't think I covered this in the notes but you can easily reassign values of an array with the following syntax**
# 
#     some_list[index] = value

# In[15]:


# reassign "Sleep"


# **7 D) You decide getting rid of `"Sleep"` was a bad idea and want to add it back where it was before. Use the [remove](https://www.programiz.com/python-programming/methods/list/remove) and [insert](https://www.programiz.com/python-programming/methods/list/insert) methods to add `"Sleep"` back to the list**

# In[1]:


# add "Sleep" again


# **7 E) As you start finishing tasks you move them from today's list to tomorrow's list. Use [pop](https://www.programiz.com/python-programming/methods/list/pop) and append. When you're done today's list should be empty, and tomorrow's list should look like the following:**
#     
#     ["Work", "Python", "Sleep", "Repeat"]
# 
# **BONUS: Solve it by hand (one item at a time), and then solve it using a while loop**

# In[2]:


# add item's to tomorrow's list


# **8) Given the following matrix, answer the next few questions**

# In[ ]:


matrix = [
    [10, 3, 13, 8],
    [5, 16, 2, 11],
    [4, 9, 7, 14],
    [15, 6, 12, 1],
]


# **8 A) Use list indexing to return the 3rd row of the matrix**

# In[ ]:


# return [4, 9, 7, 14]


# **8 B) Use double indexing to return the number 14 from the matrix**

# In[3]:


# return 14


# **8 C) Calculate the sum of each row in the matrix and print it to the screen**
# 
# **HINT: this will be easier using python's built in sum function and a for loop**

# In[4]:


# print the sum of each row


# **8 D) Calculate the sum of each column in the matrix and print out the result**

# In[7]:


# print the sum of the columns


# **8 E) Calculate the sum of each diagonal and print out the result**

# In[6]:


# print the sum of each diagonal


# **8 F) Is the matrix a [magic square](https://en.wikipedia.org/wiki/Magic_square)?**

# In[ ]:





# **9 A) How do you create a dictionary in Python?**

# *write your response*

# **9 B) Create a dictionary mapping 7 of the following [menu](http://www.houstonhallny.com/menu/) items to their prices store the dictionary in a variable called menu**

# In[9]:


# create the menu


# **9 C) You decide to order one of everything on the menu, and because you're a nice person you tip 20%. What do you end up paying?**

# In[10]:


# calculate the total amount spent


# **10) Use the same menu link and items you used from the previous question. You decide that you now want to also capture the category and descriptions for each item. Create a dictionary in the following form:**
# 
#     new_menu = {
#         'item1':{
#             'category':'appetizers',
#             'price':13.75,
#             'description':'Crispy...'
#         },
#         'item2:{
#             'category':'to share',
#             'price':21.40,
#             'description':'Lemon Garlic ...'
#         },...
#     }

# In[15]:


# create the new menu


# **10 A) write code to determine the unique number of categorys you selected**

# In[16]:


# determin the unique categories


# **10 B) write code to figure out which item has the longest description. Print out the length of the longest description as well as the description itself.**

# In[17]:


# find the longest description


# **11) Given the following list of data describing fortune cookies answer the following questions**

# In[18]:


fortune_cookies = [
    {
        "quote":"The fortune you seek is in another cookie.",
        "lucky numbers":[17, 15, 32, 6, 14, 9]
    },
    {
        "quote":"A foolish man listens to his heart. A wise man listens to cookies.",
        "lucky numbers":[66, 1, 20, 23, 5, 11]
    },
    {
        "quote":"It is a good day to have a good day.",
        "lucky numbers":[1, 2, 3, 5, 7]
    },
    {
        "quote":"This cookie contains 117 calories.",
        "lucky numbers":[46, 82, 13, 3, 15, 16]
    },
    {
        "quote":"Hard work pays off in the future. Laziness pays off now.",
        "lucky numbers":[22, 4, 5, 5, 74, 10]
    },
]


# **11 A) print the value of `"This cookie contains 117 calories"` from the fortune cookies list**

# In[ ]:





# **11 B) print the fortune where the sum of the lucky numbers is the largest** 

# In[ ]:





# **11 C) print each fortune where the last lucky number is even**

# In[ ]:





# **12 A) How do you create a set in Python? is a set an ordered or an unordered data structure?**

# In[ ]:





# **12 B) Look up the set [intersection](https://www.w3schools.com/python/ref_set_intersection.asp) method and use it in an example below**

# In[ ]:





# **13) How do you create a Tuple in Python?Is a Tuple an ordered or an unordered data structure?Cany you change a Tuple once it's been created?**
# 
# **BONUS: In what ways are strings similar to Tuples?**

# *write your response*

# **14) A useful built in function to use when looping in Python is [enumerate](https://docs.python.org/3/library/functions.html#enumerate). Once you've checked out the documentation use it in a for loop**

# In[19]:


# use enumerate


# **15) Given a string containing each letter of the alphabet, and a list of words how many times does each letter appear in the list of words? Ultimately produce a dictionary letters in the alphabet map to their count**
# 
# **HINT: It might be useful to use a nested four loop**

# In[ ]:


alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = []


# In[11]:


# find the count of each letter


# **16 A) Inspect the following code: Is this an infinite loop? Why or why not?**
#     
#     count = 7
#     while count > 8:
#         print count

# *write your response*

# **16 B) Inspect the following code: Is this an infinite loop? Why or why not?**
# 
#     weekdays = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
#     index = 0
#     while weekdays[0] != 'Sat':
#         if weekdays == 'Mon':
#             index += 2:
#         elif weedays == 'Fri':
#             index -= 1:
#         elif weekday == 'Wed':
#             index += 3

# *write your response*

# **16 C) Inspect the following code: is this an infinite loop? Why or why not?**
# 
#     while True:
#         user_input = input('continue? ')
#         if user_input == 'yes':
#             break
#         print('around we go...')
# 
# **HINT: check out python's built in [input](https://docs.python.org/3/library/functions.html#input) function**

# *write your response here*
