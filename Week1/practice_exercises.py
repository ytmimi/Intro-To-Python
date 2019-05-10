#!/usr/bin/env python
# coding: utf-8

# **1) What command do you use to run a cell in a Jupyter Notebook?**

# write your answer in this cell

# **2) What command do you use to create a new cell above the current cell**

# write your answer in this cell

# **3) How do you create comments in Python?**

# write your answer in this cell

# **4) Look back at the variables section of the in class exercises. Describe the rules for creating legal variable names. Give two examples of legal variable names, and one illegal variable name**

# write your answer in this cell

# **5) What are the 4 basic data types in Python?**

# write your answer in this cell

# **6) What function can you use to find the type of a given object?**

# write your answer in this cell

# **7) What is the type of the variable a below?**

# In[ ]:


# write code to solve this problem
a = 5


# **8) What is the type of the variable b below?**

# In[ ]:


# write code to solve this problem
b = "what am I?"


# **9 A) list 5 mathematical operators and explain what they do.**

# In[ ]:





# **9 B) Do a little math using the 5 operators that you chose. Use the print function to display each result.**
# 
# *ex) print(5 + 5)*
# 
# **BONUS: use string formating to make the result look nice**

# In[ ]:


# write code to solve this problem


# In[ ]:





# **10) Given the following list of numbers find the min, max, and sum of the list**

# In[ ]:


nums = [1, 34, 8, 3, -3, 20, 99, -4, 77]
# write code to solve this problem


# **11 A) Head to the Python [Standard Library documentation](https://docs.python.org/3/library/functions.html) and find a built in function we didn't discuss in the first class and describe how it's used**

# write your answer in this cell

# **11 B) write code using the new function that you learned**

# In[ ]:


# write code to solve this problem


# **12) Explain why string concatenation isn't ideal for string formatting?**

# write your answer in this cell

# **13) concatenate the following two strings**

# In[ ]:


string1 = 'Hey '
string2 = 'there'
# write code to solve this problem


# **14) Adjust the following f string so the variable "word" is repeated 7 times**

# In[ ]:


word = "really "
# write code to solve this problem
f'I {word}like learning Python' 


# **15 A) What are the 3 arguments you can place between the [] when using slicing notation**

# write your answer in this cell

# **15 B) Use string slicing to get the 5th character of the following string**
# 
# **HINT: remember that indexing starts at zero**

# In[ ]:


company = "Horizon Media Search"
# write code to solve this problem


# **15 C) Use slicing notation to return the entire last word "Search"**

# In[ ]:


# write code to solve this problem


# **15 D) If you used positive slicing to return Search, trying returning search using negative numbers for the start and stop arguments**

# In[ ]:


# write code to solve this problem


# In[ ]:





# **Create a string that's 15 characters long. confirm that the string is the correct size using the built in len function**

# In[ ]:


# write code to solve this problem


# **16 A) Given the following string, break it up into a list of individual words. Store the new list in a varriable**
# 
# **HINT: look up how to split strings**

# In[ ]:


my_long_string = ''
# write code to solve this problem


# **16 B) How could you take the list you just created and turn it back into a single string?**

# In[ ]:


# write code to solve this problem


# In[ ]:





# **17 A) List 5 logical operators and explain what they do**

# write your answer in this cell

# **17 B) Use each of the 5 logical operators that you descirbed in part A in an expression that evaluates to True and print the result**
# 
# **ex) print(5 > 3)**

# In[ ]:


# write code to solve this problem


# **17 C) Use each of the 5 logical operators that you described in part A in an expression that evaluates to False and print the result**
# 
# **DON'T JUST DO THE OPPOSITE OF WHAT YOU DID IN PART B**

# In[ ]:


# write code to solve this proble


# **18) In this next set of problems I'm going to define a function. If you've made it this far, then you've already had plenty of experience working with some built in Python functions. You're goal is to figure out what the function does and call the function with the given argument to print the correct value**

# In[ ]:


def how_much_am_i_drinking(weekday, stress_level):
    """
    weekday: (str) 
    stress_level: (int) An integer from 1-10
    """
    possible_stress_levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if type(stress_level) != int :
        raise ValueError('stress_level must be of type int')
    
    possible_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if type(weekday) != str and weekday not in possible_days:
        raise ValueError(f'weekday must be one of the following: {possible_days}')
    
    if weekday == 'Monday':
        if stress_level < 7:
            print('I should be responsible')
        
        else:
            print('2 Beers')
        
    elif weekday == 'Tuesday':
        if stress_level == 1:
            print(f'{stress_level} marg on Tequila Tuesday')
        else:
            print(f'{stress_level} margs on Tequila Tuesday')
    
    elif weekday.startswith('S'):
        print('It\'s the weekend...', end='')
        if stress_level <= 6:
            print('Shots!')
        else:
            print('Double Shots!!')
        
    elif len(weekday) + stress_level >= 15:
        print('Too many to count')
    
    else:
        print('I think I\'ll take it easy')


# **18 A) Adjust the vlaues of `weekday1` and `stress_level1` to print out**: "I think I'll take it easy"

# In[ ]:


# write code to solve this problem
weekday1 = None
stress_level1 = None

how_much_am_i_drinking(weekday1, stress_level1)


# **18 B) Adjust the vlaues of `weekday2` and `stress_level2` to print out**: "9 margs on Tequila Tuesday"

# In[ ]:


# write code to solve this problem
weekday2 = None
stress_level2 = None

how_much_am_i_drinking(weekday2 stress_level2)


# **18 C) Adjust the vlaues of `weekday3` and `stress_level3` to print out**: "It's the weekend...Shots!!"

# In[ ]:


# write code to solve this problem
weekday3 = None
stress_level3 = None

how_much_am_i_drinking(weekday3 stress_level3)


# **18 D) Adjust the vlaues of `weekday4` and `stress_level4` to print out**: "2 Beers"

# In[ ]:


# write code to solve this problem
weekday4 = None
stress_level4 = None

how_much_am_i_drinking(weekday3 stress_level3)


# ## I'f you're feeling up to it, add a few more cells to the bottom of this notebook and try and print out the remaining combinations

# In[ ]:




