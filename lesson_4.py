
# Week 4

# What if we want to use large chunks of code again?

# Well, we have this handy bit of code that counts how many
#       times we added "apples" to our grocery list

grocery_list = ["apples", "bananas", "apples", "carrots", "apples", "apples"]

count = 0

for item in grocery_list:
    if item == "apples":
        count = count + 2

# Great! What if we want to do it on another grocery list?
# Copy-paste?

grocery_list = ["apples", "apples", "apples", "apples"]

count = 0

for item in grocery_list:
    if item == "apples":
        count = count + 2

# Perfect! What if we want to count the number of bananas instead?
# Copy-paste?

grocery_list = ["bananas", "apples", "apples", "bananas", "porcupines"]

count = 0

for item in grocery_list:
    if item == "bananas":
        count = count + 2

# Sensational!
# Not exactly. None of this code works because of a typo.
# We've counted twice as many grocery items as we wanted to.

# Alright, better go back and change all 3 occurrences!
# Actually, we have a better way to do this.



# A function takes some input and produces some output.
# Sound familiar? It sounds like our definition of a computer!
# Do you know exactly how computers work?
# No.

# That means we don't have to know how functions work to use them!
# print, input, and range are all functions we've used already

# abs is a function that takes the absolute value of a number
print(abs(0))  # prints 0
print(abs(1))  # prints 1
print(abs(-1)) # prints 1

# Do we have to know how it works to use it? No!

# We can make our own functions. Let's try abs!

def my_abs(num):
    if num >= 0:
        return num
    else:
        return -1 * num

# def says we're making our own function (stands for "define")
# my_abs is the name of the function
# num is the "argument" of the function ("formal parameter" if you're an academic)
# return means "give back" to whoever "called" this function

# This is a function definition and does not do anything on its own!
# It has to be called. We've called functions before!

print(my_abs(0))  # prints 0
print(my_abs(1))  # prints 1
print(my_abs(-1)) # prints 1

# When we call a function, what we give it in the parentheses
#      becomes the argument to the function.
# In this case, when we call my_abs(0), "num" in the function becomes zero
# It's just like variables, but you're taking from someone else's box!

# Functions can have multiple arguments too.

def rearrange_words(word1, word2):
    return word2 + " " + word1

# Functions are better for more than just not copy-pasting code.
# They represent the fundamental idea of abstraction that computer
#      science rests on.

# Let's rewrite our apples counter in a function.

def apples_counter():
    grocery_list = ["apples", "bananas", "apples", "carrots", "apples", "apples"]

    count = 0

    for item in grocery_list:
        if item == "apples":
            count = count + 1

    return count

# This function gives back how many apples are in the list in the function.

# But what if we wanted to use a different list?
# Let's make the list to count through an argument so it can be different things!

def apples_counter_in_list(grocery_list):
    count = 0

    for item in grocery_list:
        if item == "apples":
            count = count + 1

    return count

apples_counter_in_list(["apples", "cucumbers", "apples", "apples"])

# Now we can count the number of apples in any list!

print(apples_counter_in_list(["apples", "apples", "apples", "apples"]))
# prints 4

# But what if we wanted to count bananas instead?
# Let's make what item we're looking for into an argument so it can be different things!

def items_counter_in_list(grocery_list, word_to_count):
    count = 0

    for item in grocery_list:
        if item == word_to_count:
            count = count + 1

    return count

# Now we can count the number of any item in any grocery list!

# But what if we want to count numbers in a list of numbers instead?

# Wait...
# Our code already works for that!



# Our items_counter_in_list function is way more flexible than the apples_counter!
# It solves so many problems!



# Functions are one of computer science's *big ideas*.

# Not only do they allow us to avoid duplicate code, they allow us
#       to make solutions to problems more general (plus they basically
#       founded computer science). Look up lambda calculus if you're interested.



# EXTRA:

# What do you think this function does?

def map(func, ls):
    new_ls = []

    for e in ls:
        new_ls.append(func(e))

    return new_ls



# func stands for function
# This function "map" takes an argument of a function!
# It applies this function to every item in a list and
#     puts the result in a new list, which is returned.

print(map(my_abs, [1, -1, -10, 0, 100]))



# Practice:

# Write a function that takes the factorial of a number.

# factorial(1) should output 1.
# factorial(2) should output 2.
# factorial(3) should output 6.
# factorial(4) should output 24.
# factorial(5) should output 120.
# etc.
# Bonus: factorial(0) should output 1.
# Bonus: factorial of a negative number should raise a ValueError.


def anything(num):
    i = 0
    product = 1
    
    while i < num:
        i = i + 1
        product = i * product
        

    return product
        


# factorial(6) = 6 * 5 * 4 * 3 * 2 * 1 = 720

def factorial(num):
    count = 1
    ans = 1
        
    while count <= num:
        ans = count * ans
        count = count + 1
        
    return ans
            
    
     


def factorial(num):
    if num == 0:
        return 1
    return num* factorial(num-1)

from functools import reduce

def factorial(num):
    return reduce(range(1, num), lambda x, y: x * y)






















# Solution (only look after you've made a valiant effort):

def factorial(n):
    if n < 0:
        raise ValueError("You cannot take the factorial of a negative number")

    count = 1
    product = 1

    while count <= n:
        product = product * count
        count = count + 1

    return product
