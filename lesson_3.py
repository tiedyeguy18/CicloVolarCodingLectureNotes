
# Week 3

# What would make our program better? Being better than humans!
# In what ways are machines better than humans?
# - no mistakes, we've explored
# - speed!



# Before we get to loops, we should talk about lists.
# A list is a type of data that stores multiple values of any type in order.
# We use square brackets [] to make a list.
groceries = ["apples", "bananas", "carrots"]
fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13]
fibonacci_numbers_even = [True, False, False, True, False, False, True, False]
random_items = ["hello", 7, 3.14, "c", True]


# Lists are just variables, meaning they can also be used in expressions.
# How do we get things out of lists?
# What's the first thing on my grocery list?
# We use square brackets around a number to get the item at a given location.
# The location is called an "index" (think when you look in the back of a textbook)
print(groceries[0]) # prints apples

# Zero!?
# Yes, us programmers start counting from zero. This makes sense.
# How far is "apples" from the start of the list?
# It's zero away.
# What are the second and third things on my grocery list?
print(groceries[1]) # prints bananas
print(groceries[2]) # prints carrots

# What's the fourth thing on my grocery list?
print(groceries[3]) # gives an error; there is no fourth thing!

# What if we want to print the whole grocery list?
print(groceries[0])
print(groceries[1])
print(groceries[2])

# What if there were 10 things on the list?

print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[3])
print(groceries[4])
print(groceries[5])
print(groceries[6])
print(groceries[7])
print(groceries[8])
print(groceries[9])

# My hands are tired! How can we do this better?



# Loops allow us to do things many times in a row.

for item in groceries:
    print(item)

for number in fibonacci_numbers:
    print(number)

# Each time through the loop, the variable we say before "in" gets updated to be the next thing in the list.
# This continues until the end of the list.

# We don't just have to print.
# This prints the biggest number in a list of positive numbers.

biggest = 0

for number in fibonacci_numbers:
    if number > biggest:
        biggest = number

print(biggest)



# What if we don't want to go through a list, we just want to go through numbers?
# If you're using a for loop? Too bad!
# You can go through a list of numbers though.
# Python's range will (kind of) make a list of numbers for you!
print(list(range(10))) # prints a list of numbers from 0 to 9
print(list(range(1, 11))) # prints a list of numbers from 1 to 10



# What if we want to do something over and over again that doesn't involve a list at all?
# Loops' most general form: while loops.
# While loops are like if statements, but they keep going until the condition is False.

# This prints the numbers 0 to 9.
count = 0

while count < 10:
    print(count)
    count = count + 1

# This program says hi until the user says bye.

while input() != "bye":
    print("hi")

# There are 3 key things that these loops (and all loops) must have
# a place to start
# a place to stop
# progress from the start to the stop

# In the above 0-9 loop:
# the start is count = 0
# the end is count < 10 (so when count is 10 or more, it stops)
# the progress is count = count + 1



# Practice:

# Write a program to "hissify" a word. Anytime you encounter an "s", make it into three "s"s.
# Here's a sample of how it should work:

# What's the word you'd like to hissssify?
# trust
# Your hissified word is trussst.

