
# Below are the homework solutions. I strongly advise not
# viewing a given week until you have given your best attempt
# at that week.

# Note that these are model solutions, meaning they're the best way
# to do things knowing what you knew at the time. There are an infinite
# number of ways to solve any open problem, so don't be discouraged if yours
# doesn't look the same.

### Week 1 ###

# Expected:

print("Hi, my name is Jamin and I'll be your waiter for tonight. What can I get you started with?")
order = input()

print("Alright, and how many dollars does that cost?")
price = input()

print(f"Sounds good, you ordered a {order}, so your total is ${price}.")


# Reasonable advanced:

menu = {"hamburger": 7, "cheeseburger": 7.5, "hot dog": 5, "vegetarian option": 5}

print("Hi, my name is Jamin and I'll be your waiter for tonight. What can I get you started with?")
order = input().lower()

while order not in menu:
    print("I'm sorry, we don't have that. What would you like instead?")
    order = input().lower()

food_cost = menu[order]
print(f"A {order} will be ${food_cost}")
print("How much would you like to tip before tax, as a percent?")

tip = float(input())
while tip < 0:
    print("I'm sorry, you cannot tip a negative amount. I can't have been that bad!")
    tip = float(input())

tip /= 100

print("Thanks, here is your receipt.")
print(f"{order}: {food_cost}")
print(f"tip: {tip}")
subtotal = food_cost*(tip+1)
print(f"subtotal: {subtotal}")
print(f"tax: {subtotal*.07}")
print(f"total: {subtotal*1.07}")



### Week 2 ###

# Expected:

print("Welcome to rock, paper, scissors! Make your play.")

move = input()

if move == "rock" or move == "paper" or move == "scissors":
    if move == "rock":
        my_move = "paper"
    elif move == "paper":
        my_move = "scissors"
    elif move == "scissors":
        my_move = "rock"

    print(f"I play {my_move}, I win!")
else:
    print("Invalid move.")


# Reasonable advanced:

import random

print("Welcome to rock, paper, scissors, lizard, spock! Make your play.")

options = ["rock", "lizard", "spock", "scissors", "paper"]

user_move = input()
while user_move not in options:
    print("Invalid move. Please try again.")
    user_move = input()

user_move = options.index(user_move)
my_move = random.randint(0, 4)

print(f"I play {options[my_move]}.")

if my_move == user_move:
    print("Tie!")
elif my_move == ((user_move + 1) % len(options)) or \
     my_move == ((user_move + 3) % len(options)):
    print("You win!")
else:
    print("I win!")



### Week 3 ###

# Expected:

print("elcomeway otay ymay igpay atinlay ranslatortay")
print("leasepay ntereay aay ordway otay ebay ranslatedtay:")

word = input()
while word != "quit":

    acc = ""
    for i in range(1, len(word)):
        acc = acc + word[i]

    print(f"{acc}{word[0]}ay")
    print("leasepay ntereay notheraay ordway:")

    word = input()

# Reasonable advanced:
# Features:
# - preserves capitalization
# - preserves pronunciation with consonant groups
# - works on multiple words at a time

def is_vowel(letter):
    return letter in ["a", "e", "i", "o", "u"]

# undefined behavior for consonant-only words
def piglatinator(word):

    capitalized = word[0].isupper()
    word = word[0].lower() + word[1:]

    to_move_index = 1

    if not is_vowel(word[0]):
        while not is_vowel(word[to_move_index]):
            to_move_index += 1

    word = word[to_move_index:] + word[:to_move_index] + "ay"

    if capitalized:
        return word[0].upper() + word[1:]
    return word

print("elcomeway otay ymay igpay atinlay ranslatortay")
print("leasepay ntereay aay ordway otay ebay ranslatedtay:")

words = input()
while words != "quit":

    for word in words.split():
        print(piglatinator(word))

    print("leasepay ntereay notheraay ordway:")
    words = input()

# If you'd like solutions to any of the loop practice questions, email me.


### Week 4 ###

# Week 1 assignment: no functions necessary, it's very straightforward.

# Week 2
def rps_winner(move):
    if move == "rock":
        my_move = "paper"
    elif move == "paper":
        my_move = "scissors"
    elif move == "scissors":
        my_move = "rock"

    return my_move

assert rps_winner("rock") == "paper"
assert rps_winner("paper") == "scissors"
assert rps_winner("scissors") == "rock"

print("Welcome to rock, paper scissors! Make your play.")
move = input()
print(f"I play {rps_winner(move)}. I win!")

# Week 3 assignment: see more advanced for version with function.
# Here are the tests for that function:
assert piglatinator("app") == "ppaay"
assert piglatinator("aapp") == "appaay"
assert piglatinator("apap") == "papaay"
assert piglatinator("appa") == "ppaaay"
assert piglatinator("Schnapps") == "Appsschnay"
assert piglatinator("ProGram") == "OGrampray"
assert piglatinator("program") == "ogrampray"
assert piglatinator("hello") == "ellohay"

# Reasonable advanced:

def converter(direction, amount, rate):
    if direction == 1:
        return amount * rate
    else:
        return amount / rate

# direction=1 for USD to MXN, 2 for other way
def money_converter(direction, amount):
    return converter(direction, amount, 19.88)

# direction=1 for mi to km, 2 for other way
def dist_converter(direction, amount):
    return converter(direction, amount, 1.60934)

def num_to_binary(n):
    binary_rep = []

    while n > 0:
        binary_rep.insert(0, n % 2)
        n //= 2

    return binary_rep

def merge_sort(ls):

    def merge(ls1, ls2):
        if ls1 == []:
            return ls2
        if ls2 == []:
            return ls1

        if ls1[0] < ls2[0]:
            return [ls1[0]] + merge(ls1[1:], ls2)
        else:
            return [ls2[0]] + merge(ls1, ls2[1:])

    if len(ls) <= 1:
        return ls
    
    split_i = len(ls) // 2
    return merge(merge_sort(ls[:split_i]), merge_sort(ls[split_i:]))

def derivative(f, x):
    h = 0.00000001
    return (f(x + h) - f(x)) / h

def flip(f, arg1, arg2):
    return f(arg2, arg1)

def adder_factory(n):
    return lambda x: n + x
