
# Week 1

# What is a computer? Let's start with things computers can do.

# we can print things
print("things")
print("woohoo!")
print(5)


# we can use Python as a calculator
print(2 + 7) # prints 9
print(3 * 7) # prints 21
print(12 - 21) # prints -9
print(-12) # prints -12
print(1 / 2) # prints 0.5
print(2 ** 3) # prints 8 (2 to the third power)
print(11 // 4) # prints 2 (the number of times 4 fits completely into 11)
print(11 % 4) # prints 3 (the remainder of dividing 11 by 4)



# variables are boxes in the computer

# you can put things in them
dime_value = 10

# and take things out of them
print(dime_value) # prints 10

# variables can be combined with other things to form "expressions," which are "evaluated" by Python
print(dime_value + 5) # prints 15

# variables can be used anywhere expressions can, and vice versa
nickel_value = 5
quarter_value = 2 * dime_value + nickel_value # puts 25 in the quarter_value variable
print(quarter_value / 2) # prints 12.5



# variables have types, which tell us what kind of thing they have in them

# There are a couple of types we'll start with:
# - int (stands for integer; whole numbers)
# - float (stands for floating point number; real numbers, don't have to be whole)
# - str (stands for string; a list of keys that you type on your keyboard)
# - boolean (can only be True or False, represents the answer to a yes/no question)

# we won't really distinguish between ints and floats right now
# the way we type strings is by surrounding them with single or double quotes, ' or "

# We can use type to tell the types of variables
print(type(5)) # prints <class 'int'>
print(type("hello")) # prints <class 'str'>
# etc.



# Python makes it easy for us to mix strings with other types
# starting a string with f tells Python that we're going to mix things in
# putting things in curly brackets {} inside the string tells Python to evaluate them
print(f"two times three is {2 * 3}") # prints two times three is 6
print(f"a quarter is worth {quarter_value} cents") # prints a quarter is worth 25 cents
print(f"two {nickel_value} cent pieces is worth one {dime_value} cent piece") # prints two 5 cent pieces is worth one 10 cent piece



# we can get input from the user too, using input()
user_pick = input() # if the user enters 3, user_pick stores "3"

# input always gives us a string
print(user_pick + 1) # gives us an error because we can't add a number to a string - it doesn't make sense



# we can use Python as an even more special calculator!
print(2 > 1) # prints True
print(5 <= 5) # prints True
print(5 == 5) # prints True
print(5 == 6) # prints False
print(not True) # prints False
print(2 > 1 and 5 >= 5) # prints True
print(2 < 1 and 5 >= 5) # prints False
print(2 < 1 or 5 >= 5) # prints True
print(2 < 1 or 5 > 5) # prints False


# A computer is a machine that takes input, stores it, processes it in
#     some way, and produces some output.

# We know how to do each of these steps:
# Input: input()
# Storage: variable = input()
# Processing: variable = variable * 2
# Output: print(variable)

print(f"uih {dime_value}")

# Practice:

# Write a program to introduce youself (as the computer) to someone else.
# Here's a sample of how it should work:

# Hi, my name is Jamin and I like to code. What's your name?
# Kaladin
# Hi Kaladin! What do you like to do?
# be sad
# Cool, I like to be sad too!
