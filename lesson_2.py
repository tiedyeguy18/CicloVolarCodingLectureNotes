
# Week 2

# What would make our programs better? Decisions!
# How do computers make decisions?



# if statements
if 1 == 1:
    print("math is whole")

if 1 == 2:
    print("math is broken")

# "math is whole" is the output of this program

# if statements ask a question
# *if* the answer to that question is "yes" (True), it does what's after the colon (:)
# if it's "no" (False), it doesn't do anything

# Note that the indentation is necessary to tell Python that what we're doing depends on the if statement.
# You can do the indentation by pressing the "Tab" key or by pressing the spacebar 4 times.

# Here's a program that asks the user if they won. It prints "yay!" if they say "yes" and nothing otherwise.
print("Did you win?")
won_string = input()

if won_string == "yes":
    print("yay!")



# Well, what if we want to print something if they lose? We can add an else to do that.

# Now the program does the same thing, but it prints "aww." if the user didn't say "yes"
print("Did you win?")
won_string = input()

if won_string == "yes":
    print("yay!")
else:
    print("aww.")

# Notice the colon and indentation again.
# Also notice that else doesn't have a question after it, because it doesn't have to!
# It's just the opposite of the question for the if statement.
# We can read this statement in English: "If the user input "yes", then print "yay!" Otherwise, print "aww."



# What if it was possible to have a tie?
# "elif" is short for "else if" or "otherwise, if"

# Now the program does almost the same thing, but it prints "even match" if it was a tie.
print("What was the outcome of the game?")
outcome_string = input()

if outcome_string == "won":
    print("yay!")
elif outcome_string == "tie":
    print("even match")
else:
    print("aww.")

# In English, this reads as "If the user input "won", then print "yay!"
# Otherwise, if the user input "tie", print "even match"
# Otherwise print "aww."



# What if the user didn't listen to us and put in something that didn't indicate the outcome of the game, like "hi?"
# We could make sure they did indicate the outcome of the game, and if they didn't, we can say "invalid input."
print("What was the outcome of the game?")
outcome_string = input()

if outcome_string == "won":
    print("yay!")
elif outcome_string == "tie":
    print("even match")
elif outcome_string == "loss":
    print("aww.")
else:
    print("invalid input.")

# So, how do computers make decisions? If statements!



# Practice:

# Write a simple chatbot. You can support whatever commands you like.
# Here's a sample of how it could work:

# Hi, I'm Mr. Chips, the chatbot! I can reverse phrases! What's the word you'd like to come second?
# Hello
# What's the word you'd like to come first?
# World
# Your output is: World Hello
