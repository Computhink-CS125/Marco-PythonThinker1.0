# # Lesson 11 - AND OR NOT

# # Recap 1: Purchase Advisor
# Create a program that asks the user for the price of an item (px) and
# gives a comment based on the price:

# if:
#     px <= 5: "Sounds good!"
#     px <= 50: "Are you sure you need this?"
#     px <= 500: "Where are you getting this money from?!"
#     px > 500: "Don't even think about it!"

# px = int(input("How much is the price?\n"))
# if px <= 5:
#     print("Sounds good!")
# elif px <= 50:
#     print("Are you sure you need it?")
# elif px <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")
# --------------------------------------------------------------------

# # Task 1: AND Operator in Simple Conditions (AND)
# You are writing a program for an amusement park that needs to check
# if both riders of a ride are above the height of 120cm. Use the 'and'
# operator to determine if value of both 'rider1' and 'rider2' are
# greater than 120.

# 'rider1' = 125
# 'rider2' = 150

# rider1 = int(input("How tall is rider 1?"))
# rider2 = int(input("How tall is rider 2?"))
# if rider1 >= 120 and rider2 >= 120:
#     print("You can take the ride.")
# else:
#     print("You are too young to take the ride.")
# --------------------------------------------------------------------

# # Task 2: Multiples of 3 and 7 (AND)
# Create a program to check if a number is both divisible by 3 and 7

# 1. Ask the user to input a number
# 2. If the number is both a multiple of 3 and a multiple of 7:
#     print "The number is divisible by 3 and 7!"

# num = int(input("Enter the number."))
# is_divisible_by_3 = num%3 == 0
# is_divisible_by_7 = num%7 == 0
# if is_divisible_by_3 and is_divisible_by_7:
#     print("The number is divisible by 3 and 7!")

# divided_by_3 = num%3
# divided_by_7 = num%7
# if divided_by_3 == 0 and divided_by_7 == 0:
#     print("The number is divisible by 3 and 7!")


# --------------------------------------------------------------------

# # Task 3: Identity Identifier (AND)
# Create a program that asks for user's first and last name and checks
# if it matches "James" and "Leong" respectively and print "YOU ARE
# WANTED" if true.

# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# if first_name == "James" and last_name == "Leong":
#     print("YOU ARE WANTED")

# --------------------------------------------------------------------

# # Task 4: 'or' Operator in Conditional Statements (OR)
# You run a go-kart business and need a program to check if at least
# 1 occupant of a 2-person go-kart is at least 18 years old.

# Use the 'or' operator to determine if value of either 'rider1' or
# 'rider2' is equal to or greater than 18.

# 'rider1' = 25
# 'rider2' = 6

# rider1 = int(input("How old are you?"))
# rider2 = int(input("How old are you"))
# if rider1 >= 18 or rider2 >= 18:
#     print("You can ride it.")
# else:
#     print("You cannot ride it.")

# # Task 5: Ticket Pricing Machine (OR)
# Create a program that will decide on the price of a ticket based on
# user's age. Original ticket price costs $20 per person. However,
# children below the age of 12 and elderly above the age of 65 can buy
# the ticket for just $15.

# 1. Ask user for their age
# 2. Use the 'or' operator to determine if user's age is less than 12 or
#    more than 65. If true, print "Ticket price: $15"
# 3. Else, print "Ticket price: $20"

# age = int(input("How old are you?"))
# if age < 12 or age > 65:
#     print("You can buy the ticket at $15.")
# else:
#     print("The ticket cost $20.")
# --------------------------------------------------------------------

# # Task 6: Input Validator (OR)
# Using the 'or' operator, create a program that prints "Valid Input"
# if the user has entered "M" or "Male" as an input. Or else, print
# "Invalid Input" instead

# 1. Ask user for input
# 2. If user input is "M" OR "Male", print "Valid Input"
# 3. Else, print "Invalid Input"

# something = input("Type something.")
# if something == "M" or something == "Male":
#     print("Valid Input")
# else:
#     print("Invalid Input")
# --------------------------------------------------------------------

# # Task 7: Colour filter (NOT)
# Create a program that will ask the user for a colour and print
# "Try again" if the input of the user is not "Green".

# 1. Ask user for a colour
# 2. Using the 'not' operator, check if input is not "Green".
#    If true, print "Try again"

# colour = input("Enter colour.")
# if not colour == "green":
#     print("Try again")
# --------------------------------------------------------------------

# # Task 8: Not the Right Day (NOT)
# Create a program that asks the user for the day of the week. If the
# input is not "Saturday", the program should print "It's not the
# weekend yet!"

# 1. Ask the user for the day of the week.
# 2. Using the 'not' operator, check if the input is not "Saturday".
# 3. If true, print "It's not the weekend yet!"

# day = input("What is today?")
# if not day == "Saturday" or not day == "Sunday":
#     print("Its not the weekend yet!")
# --------------------------------------------------------------------

# # Task 9: Not the Correct Password (NOT)
# Create a program that prompts for a password. If the entered password
# is not "Python123", the program should display "Access Denied."

# 1. Prompt the user for a password.
# 2. Using the 'not' operator, check if the password is not "Python123".
# 3. If true, display "Access Denied."

# password = input("Enter password")
# if not password == "Python123":
#     print("Access denied")
# --------------------------------------------------------------------

# # Task 10: What do you want to eat? (AND, NOT)
# Create a program that asks the user what they want to eat

# 1. Ask the user if they want a burger (y/n)
# 2. Ask the user if they want a drink (y/n)
# 3. Ask the user if they want fries (y/n)
# 4. If the user wants a burger and fries but not a drink:
#     print "Won't you get thirsty?"

# burger = input("Do you want a burger?")
# fries = input("Do you want fries?")
# drink = input("Do you want a drink?")

# if not drink == "yes" and burger == "yes" and fries == "yes":
#     print("Won't you get thirsty?")
# --------------------------------------------------------------------

# # Task 11: Login Credentials (AND, OR)
# Create a program that allows John to log in to TokTik.

# 1. John's username is 'John123' and his password is 'pw123'
# 2. The TokTik program will only allow John to log in.
# 3. Create 2 variables to store John's username and password
# 4. Ask John to enter his username and password
# 5. If both the username and password matches:
#     print "Access Granted"
# 6. If either the username or password is correct:
#     print "Either username or password is incorrect"
# 7. Otherwise:
#     print "Access Denied" 

# username = input("Enter username")
# password = input("Enter password")
# if username == "John123" and password == "pw123":
#     print("Access granted")
# elif username == "John123" or password == "pw123":
#     print("Either username or password is incorrect")
# else:
#     print("Access denied")

# --------------------------------------------------------------------

# # Task 12: Game status report (OR, NOT)
# Imagine you're programming a simple game. Write a conditional
# statement that checks whether a variable 'game_status' is either
# "active" or not "paused". Depending on the condition, print
# appropriate messages: "Game in progress..." or "Game is paused or
# inactive."

# 1. Declare a variable game_status and assign it a value
#    (e.g. "active").
# 2. Use an 'if' statement to check if 'game_status' equals "active"
#    OR if it's NOT equal to "paused" using the 'or' and 'not'
#    logical operator.
# 3. If the condition is 'True', print "Game in progress...".
# 4. Otherwise, print "Game is paused or inactive."

# game_status = "active"
# if game_status == "active" or not game_status == "paused":
#     print("Game in progress...")
# else:
#     print("Game is paused or inactive")

# =========================================
# TASK 13: Scholarship Eligibility System
# =========================================
 
# A student may receive a scholarship.
 
# The student must not be banned.
 
# After that, the student qualifies if they scored at least 85 and
# attended at least 90 percent of classes, or if they scored at least
# 70 and have won a competition.
 
# Otherwise → "Not Eligible"
 
# 1. Ask for:
#    - score
#    - attendance
#    - won_competition (yes/no)
#    - banned (yes/no)
 
# score = int(input("What is your score?"))
# attendance = int(input("What percentage is your overall attendance?"))
# won_competition = input("Did you win any competitions?")
# banned = input("Have you been banned before?")

# if banned == "no" and ((score >= 85 and attendance >= 90) or (score >= 70 and won_competition == "yes")):
#     print("You are eligible for the scholarship")
# else:
#     print("Not eligible")

# =========================================
# TASK 14: Smart Home Security System
# =========================================
 
# A home alarm system decides whether to trigger an alarm.
 
# The alarm should trigger if the door is open while the owner is not
# at home, or if a window is open during the night, or if motion is
# detected while pet mode is off.
 
# Otherwise → "All Safe"
 
# 1. Ask for:
#    - door_open (yes/no) T
#    - owner_home (yes/no)
#    - window_open (yes/no)
#    - time ("day"/"night")
#    - motion_detected (yes/no)
#    - pet_mode (yes/no)

door = input("Is the door open?")
owner_home = input("Is the owner at home?")
window_open = input("Is the window open?")
time = input("Is it day or night?")
motion = input("Are there any motion detected?")
pet_mode = input("Is pet mode activated?")
if (door == "yes" and owner_home == "no") or (window_open == "yes" and time == "night") or motion == "yes" and pet_mode == "no":
    print("ALARM TRIGGERED")
else:
    print("Safe")



