
# Week 5

# How do we ensure our code works properly?


# 2 4 8
# Guess the rule (message me when you think you have it):

# I'll pause after each public number guess to let answers come in.






























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
# ...



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
