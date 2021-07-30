
# Week 5

# How do we ensure our code works properly?

# Guess the rule (message me when you think you have it):

# I'll pause after each public number guess to let answers come in.


# 2 4 8   WORKS
# 9       DOES NOT WORK
# 16      DOES NOT WORK
# 1 3 5   WORKS
# 3 9 27  WORKS
# 4 8 12  WORKS
# 5 10 15 WORKS
# 100 200 300 WORKS
# 0 1 2   WORKS
# 1 2 3   WORKS
# -1 0 1  WORKS
# -1 0 25 WORKS
# 1 2     DOES NOT WORK
# 1 5000 10000 WORKS
# 1 2 3 4 DOES NOT WORK
# 2 7 9   WORKS
# 1 4 6 8 9 10 DOES NOT WORK
# 1 1 2   DOES NOT WORK
# -1000 -500 2 WORKS
# 2.5 7.8 0.9 DOES NOT WORK
# 1 8000 1000000 WORKS

# 3 numbers in strictly increasing order


















# Confirmation bias is something we need to avoid at all times,
# but particularly when ensuring our programs work!

# Manual testing is a pain!
# How can we automate it?

assert True  # does nothing
# assert False  # raises AssertionError

# reverses a list
def reverse(to_reverse):
     return reverse(to_reverse[1:]) + [to_reverse[0]] if to_reverse else [];

# How can we test this function?

assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([11, 12 ,13]) == [13, 12, 11]
assert reverse([1, "apple", 3]) == [3, "apple", 1]
assert reverse([4 % 8, 2, 3]) != ["apple", 85, 90]
assert reverse([2, "banana", 500]) == [500, "banana", 2]
assert reverse([-0.6, 0, "lemon"]) == ["lemon", 0, -0.6]
assert reverse([]) == []
assert reverse([4, 5, 6]) != [6, 5]
assert reverse(["", ""]) == ["", ""]
assert reverse(["!!!###$$?"]) == ["!!!###$$?"]


# How can we avoid programs that don't work?
# - Mental debugging
# - Thoughtful design


# Assistive tool #1: readable code
# "Any fool can write code that a computer can understand. Good
#  programmers write code that humans can understand." — Martin Fowler 

def my_func(user):
    ls = []
    
    for x in user:
        if x != "h":
            ls = ls + x

    return ls

def remove_hs(to_remove_from):
    acc_no_hs = []
    to_avoid = "h"

    for letter in to_remove_from:
        if letter != to_avoid:
            acc_no_hs = acc_no_hs + letter

    return acc_no_hs

# Part of having readable code is breaking problems up into small pieces,
# then solving them one step at a time. If someone can see how your problem
# is broken down and how each step is solved, they'll have a much easier time
# understanding your solution.


# Assistive tool #2: variables should have concrete representation;
#   they should mean something specific

def plus_one_to_all(ls):
    seen_count = 0

    while seen_count < len(ls):
        ls[seen_count] = ls[seen_count] + 1
        seen_count = seen_count + 1

    return ls


# Assistive tool #3: be the computer! Use print statements to figure out what's happening

def broken_func(x):
    if x == "hello" or "hi":
        return "well hi there!"
    if x == "goodbye" or "bye":
        return "see ya!"


# Final Project!




# We can ensure our code works properly through:
# - thoughtful design
# - thorough testing


# PRACTICE:

# Write a function to multiply two integers.
# Your function may not use the * operator.
# If you've figured out a solution using / or **, excellent work; now do it again without those.
# Follow the design principles from today and test your function thoroughly.

# If you're done, start working on your project.



# 3 * 2 = 3 + 3 = 2 + 2 + 2

# 5 * 9

# a * b = adding a, b times

def multiply(inp1, inp2):
    a = int(inp1)
    b = int(inp2)

    product = 0
    for i in range(abs(b)):
        if b < 0:
            product = product - a
        else:
            product = product + a

    return product

assert multiply(0, 0) == 0
assert multiply(0, 1) == 0
assert multiply(1, 0) == 0
assert multiply(0, 23445346) == 0
assert multiply(1, 1) == 1
assert multiply(1, 325435) == 325435
assert multiply(325435, 1) == 325435
assert multiply(11, 12) == 132
assert multiply(9, 6) == 54
assert multiply(256, 256) == 65536
assert multiply(-1, 0) == 0
assert multiply(-2, -2) == 4
assert multiply(-2, 2) == -4
assert multiply(-9, 6) == -54
assert multiply(9, -6) == -54
assert multiply(-9, -6) == 54




















