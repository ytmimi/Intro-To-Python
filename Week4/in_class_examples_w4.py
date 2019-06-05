#!/usr/bin/env python
# coding: utf-8

# # Recap Last Week
# 
# We covered:
# * Comprehensions
# * Functions
# * Reading and Writing to (text) files
# * Error Handling

# # This Week
# 
# what we will cover:
# 
# * How to import python modules
# * Useful modules in the Python Standard library
# * Python Classes

# ## How to import python modules
# 
# There are several different ways to import modules / packages in Python.
# 
# To demonstrate, we'll use Python's built in math module

# You can use the **import** keyword followed by the name of a python module to make it availabe in the current program. Any Python Functions or Classes defined within the imported module are available by using the modules name 

# In[ ]:


import math

math.sqrt(4)


# You can use the **import** and **as** keywords to alias the name of a Python module. Anything defined within the file is available by referencing the knewly assigned alias

# In[ ]:


import math as m

m.sqrt(4)


#  You can use the **from** and **import** keywords to import specific names from a module

# In[ ]:


from math import sqrt

sqrt(25)


# You can also import everything from a package using the **\*** (wildcard). However, **I would highly recommend that you avoid doing this as it's generally bad practice**. Your code will be much more clear when you're quickly able to identify where your imports are coming from.

# In[ ]:


from math import *

radians(30)


# ## Useful modules in the Python Standard Library
# 
# There are a ton of convenient packages writen in the Python Standard Library that will help you solve most of the problems you're working on. Getting to know what tools are available out of the box is a great way to level up your Python efficiency. Here are a list of some of the libraries I think you'll get the most out of learning about first
# 
# * pathlib - High level abstraction on File system paths
# * datetime - handling dates, times, and calculations
# * csv - csv file reading and writing
# * collections - adds new datastructures besides lists, dicts, tuples, and sets for handling collections of objects
# * re - regular expression patter matching

# ## Working with path objects helps you easily get around your filesystem, open files for reading and writing, and much more.

# In[ ]:


import pathlib


# In[ ]:


# '.' refers to the current directory
path = pathlib.Path('.')
type(path)
print(path)


# In[ ]:


# expand the path to be absolute.
path.absolute()


# Easily join paths together in a system agnostic way. Windows Paths and Unix-like Paths (linux + Mac) use different conventions for seperating each item in a path string. Using Pathlib helps you avoid worrying about these inconsistencies

# In[ ]:


file = path / 'output.txt'
file.absolute()
print(file)


# In[ ]:


# inspect if a file exists or not
file.exists()


# In[ ]:


# inspect if a path points to a file or a directory
print(file.is_dir())
print(file.is_file())

# inspect if a path is absolute
print(file.is_absolute())


# In[ ]:


# easily write to text files
file.write_text('hello world!')

# checking if the file exists now returns True
file.exists()


# In[ ]:


# easilty read from files
file.read_text('utf-8')


# In[ ]:


# path objects can also be passed into the open function

with open(file, mode='a') as f:
    f.write('A new line')
    
file.read_text('utf-8')


# **A helpful hint when working with new objects. Use the dir builtin function to return a list of all attributes and methods**
# 
#     ex) dir(some_object)

# In[ ]:


dir(file)


# ## Working with dates and times in Python is made easy with the datetime module

# In[ ]:


# it's common convention to import datetime as dt
import datetime as dt


# In[ ]:


# we can create a date object by providing a year, month and day
some_date = dt.date(1995, 2, 2)
print(some_date)
another_date = dt.date(year=2019, month=2, day=2)
print(another_date)


# In[ ]:


# you can easilty get the current date based on your system time
today = dt.date.today()
print(today)
print(repr(today))
print(type(today))


# In[ ]:


# accessing the different attributes of the date object
print(today.year)
print(today.month)
print(today.day)


# user the strftime -- string format time -- method to change how the string gets printed. Here's a cheatsheet containing other [format codes](http://strftime.org/)

# In[ ]:


today.strftime('%m-----%d-----%Y')


# In[ ]:


# Check out what you can do with date objects
dir(today)


# In[ ]:


# date time objects are just like date objects except they contain timestamps as well
now = dt.datetime.now()
print(now)


# In[ ]:


# you can perform mathematical operations on time objects using timedelta objects
result = today - dt.timedelta(days=7)
print(today)
print(result)
print(type(result))
print(repr(result))


# In[ ]:


def hours_from_days(some_timedelta):
    return some_timedelta.days * 24


print(today - result)

hours_from_days(today - result)


# # Classes

# ## Defining a class
# 
# You can think of a class as a blueprint. It defines the **attribures** and **methods** that a Python object has. It creates some basic structure that each instance of the class has in common. Thinking about a class as a blueprint is a good anology. Think about an archetect drafting the floorplan for a building. It's likely that each differnt floors of the sam building will have the same layout. That floor plan isn't the physical space that you can live in, but instead describes where all the rooms will be, and how the large the space is. Each room / floor can be thought of as an instance of that floor plan. They follow the design specified in the floor plan, but are unique in the way that they are furnished.
# 
# Another anaology you might use is a recepie for a cake. Although the recepie describes and defines all the things that are in the cake, we can all agree that it isn't actually the cake. You can think of baking the cake as instantiating the cake, and the final cake that comes out as the final cake object or instance.
# 
# 
# You define a class using the **class** keyword followed by the name of the class. Generally the name should be in **Pascal Case**, which means the first letter of each word is capitalized. **If** your class inherits from another class you'll add the name of the parent class in parenthases. Like other things in Python, you'll also end the class definition with **:**  
#     # a class that doesn't inherit from another class
#     class SomeClass:
#         pass
#        
#     
#     # a class that inherits from SomeClass
#     class AnotherClass(SomeClass):
#         pass

# In[ ]:


# The simplist class is an empty class
class Person:
    pass


# ## Instantiating a class
# 
# Instantiating a class just means creating a unique member of that class. We've already instantiated datetime and pathlib objects earlier in this lecture. Instantiating a class is similar to calling a function in the sense that all we need to do is give the class definition everything it needs to know in order to create a particular version of the object it represents.
# 
# 

# In[ ]:


# We instantiate a person with zero arguments because none were defined
person1 = Person()
print(type(person1))

# Here are some default methods that a blank class has
print(dir(person1))


# If your class allows it, it's possible to arbitrarily assign new attributes and methods on the fly

# In[ ]:


person1.first_name = "Yacin"

print(person1.first_name)


# Typically it's not a good idea to arbitrarily assign attributes after an object has been instantiated becuase it means that you two objects of the same type will have different behavior, and this can easily lead to errors in your code. Take the following example

# In[ ]:


bob = Person()
bob.first_name = 'Bob'

tom = Person()
tom.first_name = 'Tom'
tom.last_name = 'Smith'


print(tom.first_name, )
print(tom.last_name)

print(bob.first_name)
print(bob.last_name)


# As you see trying to access an attribute on an instance / object that doesn't exists raises an error, and this is the type of problem that you can run into if you arbitrarily add new attributes to an object

# ## Instantiating with attributes
# 
# instead of assigning attributes on the fly, it's better to create each object with all the attributes that it needs. You define these attributes on a special method called **\_\_init\_\_**.
# 
# **IMPORTANT: ALL CLASS METHODS TAKE THE INSTANCE AS THE FIRST ARGUMENT, AND IN PYTHON IT IS TYPICALLY REFERED TO AS SELF**

# In[ ]:


# here we redefine the Person class and give it an __init__ method
class Person:
    def __init__(self, first_name, age, height, weight):
        self.name = first_name
        self.age = age
        self.height = height
        self.weight = weight

# we define two different Person objects that have unique characteristics
person2 = Person('Yacin', 24, '5-10', 195)
person3 = Person('Amin', 24, '5-10', 175)

print(person2.name)
print(person3.name)
print(person3.weight)


# The **\_\_init\_\_** method describes all the values that an object needs to be instantiated.Similarly to calling a function, Failing to provide each required argument will cause an error to be thrown. 

# In[ ]:


# leaving out the weight argument

bad_person = Person('Donald', 71, '6-3')
bad_person.weight


# ## self
# 
# As mentioned before, all normal methods implicitly take the instance as the first argument. Having access to the current instance through **"self"** means that we can access all the unique values set on that instance. This allows us to work with a common interface for each object of a given class, but return unique results based on the attributes of the specific object. 
# 
# 
# **IMPORTANT: self is just a common convention. you can technically call that varibale whatever you want, but other people reading your code will hate you for it**

# In[ ]:


class Person:
    def __init__(self, first_name, age, height, weight):
        self.name = first_name
        self.age = age
        self.height = height
        self.weight = weight
    
    def describe_myself(self):
        return f'Hi, my name is {self.name} and I\'m {self.age} years old.'


yacin = Person('Yacin', 24, '5-10', 195)
amin = Person('Amin', 24, '5-10', 175)

tom = Person('Tom', 45, '6-0', 200)

print(yacin.describe_myself())
print(amin.describe_myself())
print(tom.describe_myself())


# ## Methods vs Functions
# 
# Both methods and functions are callables in Python. What that means is that they can be called on to execute code. The difference is that a function is not defined within a class, whereas a method is defined on a class and can access instance attributes and methods internally.

# In[ ]:


def two_times_age(animal):
    if not isinstance(animal, Animal):
        raise ValueError('Must be of type Animal')
    return animal.age * 2


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def twice_as_old(self):
        return self.age * 2


dog = Animal('puppy', 1, 'dog')
cat = Animal('kitten', 2, 'cat')

# Here we call a method off an object, and the instance is passed explicitly
print(dog.twice_as_old())

# Here we call a function and explicitly pass the instance
print(two_times_age(cat))

# print(two_times_age(yacin))

print(dog)


# ## Extending Python's Object Model
# 
# remember back to the **Instantiating a Class** section of the notes where we used **dir** on the empty **Person** class. There were all the names that had double underscores. These are commonly refered to as dunder methods (double underscore). Most of these dunder methods correspond to some top level functionality in Python. For example **\_\_str\_\_** is what gets called when you try to print an object to the screen. It might be helpful to know that **\_\_repr\_\_** is used as a fallback if **\_\_str\_\_** isn't defined. Of coarse that means that **\_\_repr\_\_** would need to be defined.

# In[ ]:


# lets dine two classes, one with a __str__ and another without it

class Fruit:
    def __init__(self, name):
        self.name = name
        

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def __str__(self):
        return f'({self.x1}, {self.y1}), ({self.x2}, {self.y2})'

    
apple = Fruit('apple')

line = Line(0,0, 22, 7)

print(f'no __str__: {apple}')
print(f'has __str__: {line}')


# As you can see, when you don't define an **\_\_str\_\_** on an object, all you get is the memory location where the object is stored. However, when you do define an **\_\_str\_\_** you can return an appropriate representation of that object

# ## Inheritance
# 
# Inheritance is when one class gets attributes and methods from a parent class. This means that whatever methods are defined on the parent class will also be available to the child class. If both the child and the parent class define a method with the same name, then the child method will alwasy be called.

# In[ ]:


# we inherit from the Animal class defined above
class Dog(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age, 'dog')
        self.fur_color = fur_color
    
    def __str__(self):
        return self.name
    
    def noise(self, is_excited):
        if is_excited:
            return 'Woof Woof'.upper()
        else:
            return 'Woof Woof Woof'.lower()
    
        
dog1 = Dog('Max', 1, 'brown')
dog2 = Dog('Tj', 3, 'white')

# If it wasn't clear, methods can also take as many parameters as you define
print(f'{dog1}: {dog1.noise(True)}')

# Note that twice_as_old is not defined on this class, yet it still has access to the method becuause it is defined on the 
# parent class
print(f'{dog1}: {dog1.twice_as_old()}')


print(f'{dog2}: {dog1.noise(False)}')
print(f'{dog2}: {dog1.twice_as_old()}')


# ## Time permitting we'll cover some more built in python modules that you can use

# In[ ]:





# # Additional Resources
# 
# * [More on Python Modules and Packages](https://realpython.com/python-modules-packages/)
# * [Python Standard Library](https://docs.python.org/3/library/). Learn more about the Python packages we discussed in class.
# * [Python Class Video](https://www.youtube.com/watch?v=apACNr7DC_s). Minus the robotic voice, it's a pretty good video on classes
# * [Dunder Methods](https://dbader.org/blog/python-dunder-methods)

# In[ ]:




