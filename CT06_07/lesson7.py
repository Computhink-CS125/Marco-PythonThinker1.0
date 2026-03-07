# Lesson 7 - For Loop (Part 2)

## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two score_three

# average_score = totl / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + average_score)


# Debugging question 1
# total = 0

# for i in range(1, 4):
#     score = int(input("Enter score " + str(i) + ": "))
#     total = total + score

# print("Total score is: " + str(total))

# # Debugging question 2
# name = input("Enter your name: ")

# for i in range(5):
#     message = str(i) + ". " + name
#     print(message)

## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1? <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19 

# ---------------------------------------------------------------

# total_sum = 0
# for i in range(1,6):
#     num = int(input("What is the number #" + str(i) + "? "))
#     total_sum += num
# print("Sum of the 5 number is " + str(total_sum))


## Task 7: Multiplication Table Generator

# Ask the user for a number, then print the multiplication table
# for that number from 1 to 12.

# input_number = int(input("Enter a number to generate its multiplication table: "))
# print("Multiplication Table for " + str(input_number) + ":")
# for i in range(1,13):
#     result = input_number * i
#     print(str(input_number) + "x" + str(i) + " = " + str(result))


# ---------------------------------------------------------------

## Task 8: Number Pyramid Pattern

# 1. Ask the user for a number
# 2. Using the 'for' loop, print out the number like the
#    following:

# 1
# 22
# 333
# 4444
# 55555
#...
# 222222222222
# 3333333333333
# Hint: You can use a code like this >>> print("a" * 5)
# %
# 10 % 4 = 2
# 25 % 10 = 5
# 4 % 10 = 4
# 1 2 3 .... 10 11 12 ....
# 1 2 3 .... 0 1 2 ....


# input_number = int(input("Enter a number to generate the pyramid pattern: "))
# for i in range(1, input_number + 1):
#     print(str(i % 10) * i) 



# ---------------------------------------------------------------

## Task 9: Average Calculator of 5 numbers
# Ms Tan would like to calculate the average score of her 5
# students in class 6A.

# Write a program to calculate the average of 5 numbers.

# 1. Using a 'for' loop, ask the user for 5 numbers one at a
#    time.
# 2. Calculate the average for these 5 numbers and print it
#    out.

# You will need to 
# a. sum up the numbers
# b. divide the sum by the total count.
# total_sum = 0
# for i in range(1,6):
#     num = int(input("Enter score for student #" + str(i) + ":"))
#     total_sum += num
# ave = total_sum / 5
# print("The average score for the 5 students is " + str(ave))


# ---------------------------------------------------------------

## Task 10: Dynamic Average Calculator
# Ms Tan also teaches class 6B and 6C, but all of them have
# different number of students. Modify your program so that Ms
# Tan can use the same program to calculate the average score
# for all her classes.

# Design a program that will calculate the average of the
# numbers based on the number of students.

# 1. Ask the user for the number of score to find the
#    average of.
# 2. Using a 'for' loop, ask the user for each student's score
#    one at a time.
# 3. Calculate the average for the scores and print it out.

# You will need to:
# a. ask user for the number of students
# b. sum up the numbers
# c. divide the sum by the number of students

# total_sum = 0
# num_of_students = int(input("Enter the number of students: "))
# for i in range(1, num_of_students + 1):
#     num = int(input("Enter score for student #" + str(i) + ":"))
#     total_sum += num
# ave = total_sum / num_of_students
# print("The average score for the " + str(num_of_students) + " students is " + str(ave))


# Print the following after asking for the number of rows, for example n = 5

#     *
#    ***
#   *****
#  ******
# ********

#     *
#    ***
#   *****
#  ******
# ********

# 1. How do i print the row?
# " " + "*" + " " and they are symmetrical

# 2 How do i print the asterisk?
# *
# ***
# *****
# ******
# ********

# i = 1, 1 = 1 + (2 x 0)
# i = 2, 3 = 1 + 2 = 1 + (2 x 1)
# i = 3, 5 = 1 + 2 + 2 = 1 + (2 x 2)
# i = 4, 7 = 1 + 2 + 2 + 2 = 1 + (2 x 3)
# i = 5, 9 = 1 + 2 + 2 + 2 + 2 = 1 + (2 x 4)
# 1 + 2 x (i - 1)

# 3. How do we print the space?
# #     *
# #    ***
# #   *****
# #  *******
# # *********

# i = 1, 4 space
# i = 2, 3 space
# i = 3, 2 space = 5 - 3 = 2
# i = 4, 1 space = 5 - 4 = 1
# i = 5, 0 space = 5 - 5 = 0
# n = 5, what is the relationship for the length of the space and i with n?
# number of space = n - i


# num_of_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_of_rows + 1):
#     num_of_spaces = num_of_rows - i
#     num_of_asterisks = 1 + (2 * (i - 1))
#     print(" " * num_of_spaces + "*" * num_of_asterisks)

# print the following
# 1
# 12
# 123
# 1234
# 12345
# 123456

# num_of_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_of_rows + 1):
#     line = ""
#     for j in range(1, i + 1):
#         line += str(j % 10)
#     print(line)

# Write a program that prints a centre-aligned number pyramid of height n.

# Each row:
# - Is centred using spaces
# - Prints numbers starting from 1
# - Wraps around after 9 (e.g. 10 → 0, 11 → 1)

# Example (n = 6):
#      1
#     123
#    12345
#   1234567
#  123456789
# 12345678901

# num_of_rows = int(input("Enter the number of rows: "))
# for i in range(1, num_of_rows + 1):
#     num_of_space = num_of_rows - i
#     line = ""
#     for j in range(1, 2 * i):
#         line += str(j % 10)
#     print(" " * num_of_space + line)


# 5) Palindrome Number Pyramid
# ----------------------------
# Write a program that prints a centre-aligned palindrome number pyramid.

# Example (n = 4):
#    1
#   121
#  12321
# 1234321

# Rules:
# - No if / else
# - Nested for loops allowed

# you can use abs

#print the following
#     *
#    ***
#   *****
#    ***
#     *


