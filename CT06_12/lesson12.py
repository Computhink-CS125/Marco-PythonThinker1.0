# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# visitor = 0
# while visitor < 50:
#     visitor += 1
#     print(visitor)


# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25

# visitor = 18
# while visitor < 30:
#     visitor += 1
#     print(visitor)

# visitor = 4
# while visitor < 25:
#     visitor += 1
#     print(visitor)

# print number in the following sequences 11, 9 , 7, 5 ,3 ,1, -1,-3,-5,-7
# count = 11
# while count >= -7:
#     print(count)
#     count -= 2

# Task 2: while... break
# A restaurant used to have a max capacity of 50. However, due to
# the worsening of the pandemic, the government has restricted the
# max capacity of the restaurant to 30.

# Using an 'if' condition and 'break' within the 'while' loop,
# modify your answer for Task 1a to terminate the 'while' loop when
# number of visitors is 30.

# visitor = 0
# while visitor < 50:
#     visitor += 1
#     print(visitor)
#     if visitor >= 30:
#         break

# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# order = ""
# user_input = input("Order?: \n")

# while user_input != "end":
#     order += user_input + ", "
#     user_input = input("Order?: \n")

# print(order)
# while True:
#     user_input = input("Order?: \n")
#     if user_input == "end":
#         break 
#     order += user_input + ", "

# Task 5: Math Question
# **Task 5a**:
# Create a program to test the user on their math skills! The
# program will continue generating new questions until the user
# get the correct answer.

# 1. Using a 'while' loop, 
# 2. Generate 2 random numbers between 1 and 10 (import 'random'
#    and use 'random.randint()')
# 3. Ask the user to add the 2 numbers together in the following
#    format:
#     "What is 3 + 5?"
# 4. If the user gets the correct answer:
#     Print "That's correct!
# 5. Else:
#     print "Wrong! Try again"
#     End the 'while' loop

# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# user_ans = int(input(f"What is {num1} + {num2}?\n"))

# while user_ans != num1 + num2:
#     print("Wrong! Try Again.")
#     user_ans = int(input(f"What is {num1} + {num2}?"))
# else:
#     print("That is coorect.")

# while user_ans != num1 + num2:
#     if user_ans == num1 + num2:
#         print("That is coorect.")
#         break
#     print("Wrong! Try Again.")
#     user_ans = int(input(f"What is {num1} + {num2}?"))

# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# op_no = random.randint(1,3)
# op = "+"
# correct_ans = 0
# if op_no == 1:
#     op = "+"
#     correct_ans = num1 + num2
# elif op_no == 2:
#     op = "-"
#     correct_ans = num1 - num2
# else:
#     op = "*"
#     correct_ans = num1 * num2

# while True:
#     user_ans = int(input(f"What is {num1} {op} {num2}?\n"))
#     if user_ans == correct_ans:
#         print("Correct")
#         break
#     print("Wrong! Try Again.")

# **Bonus**
# Some ideas to improve on the above program:
# 1. Print the user's score once the game is over
# 2. Randomly choose an operator for each question: + - *

# **Task 5b**:
# Modify your answer from Task 5a to keep asking a new
# question until the user get 5 correct answers.

# **Bonus**
# Some ideas to improve on the above program:
# 1. Add a score system (+2 for right answer, -1 for wrong answer)
# 2. Add an ability for users to skip by saying "skip"
# 3. Disqualify user when they have gotten the wrong answer or
#    skipped more than 5 times.

# Using 'while' loop and the 'random.randint()' function from the
# 'random' library, constantly print a random number between 1 and
# 6 until the random number generated is 4.

# 1. Import the 'random' library
# 2. Create 'num' variable and assign it '0'
# 3. While 'num' variable is not '4',
#     a. Using 'random.randint()', assign 'num' variable a random
#        number between 1 and 6.
#     b. Print the random number generated.

import random
# num = 0
# while num != 4:
#     num = random.randint(1,6)
#     print(num)

# while True:
#     num = random.randint(1,6)
#     print (num)
#     if num == 4:
#         break
