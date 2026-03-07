# ## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print
#    it out.
   
product = 1
for i in range(5):
    num = float(input("Enter a number: "))
    product *= num
print("The product of the 5 numbers is:", product)

## Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.

import time
for i in range(10, 0, -1):
    print(i, "seconds remaining...")
    time.sleep(1)
print("Time's up!")


# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.

countdown_start = int(input("Enter the number to countdown from: "))
for i in range(countdown_start, 0, -1):
    print(i, "seconds remaining...")
    time.sleep(1)
print("Time's up!")

# ## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

import random
# Task 2a
random_number = random.randint(1, 6)
print("Random number between 1 and 6:", random_number)
# Task 2b
random_numbers = [random.randint(0, 9999) for _ in range(20)]
print("20 random numbers between 0 and 9999:", random_numbers)  


# ## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.

# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.

# Print out the result of comparing the 2 variables using
# the "==" operator.

# Task 3a
bool_var = True
print("Boolean value:", bool_var)
# Task 3b
bool_var1 = True
bool_var2 = True
print("Comparing bool_var1 and bool_var2:", bool_var1 == bool_var2
)
# Task 3c
bool_var1 = True
bool_var2 = False
print("Comparing bool_var1 and bool_var2:", bool_var1 == bool_var2
)

## Task 5: Random Number Guessing Game

# Create a simple program to guess a random number:
# a. Create a variable called 'guess' and assign a number that
#    you are guessing
# b. Create a variable called 'num1' and assign a random integer
#    between 1 to 10.

# Your program will check if 'guess' is equal to 'num1'.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

guess = int(input("Enter your guess (1-10): "))
num1 = random.randint(1, 10)
print("Random number generated:", num1)
print("Is your guess correct?", guess == num1)

## Task 6: Random Multiplication Quiz

# You have been tasked by Ms Tan, the Math teacher to create a
# multiplication quiz.

# Create a program that generates a certain number of random
# multiplication questions.

# Each question should involve multiplying 2 random numbers
# between 1 and 10. The user should input the number of questions
# they want to attempt.

num_questions = int(input("How many multiplication questions do you want to attempt? "))
score = 0
for _ in range(num_questions):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = int(input(f"What is {num1} x {num2}? "))
    if answer == num1 * num2:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {num1 * num2}.")
print(f"You got {score} out of {num_questions} correct!")
