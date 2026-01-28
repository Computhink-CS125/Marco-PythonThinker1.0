# # Lesson 5 - Introduction to For Loop and range()

# ## Recap 1: Automated Birthday Invitation

# You run a small business that creates personalized digital
# birthday invitation cards. To automate the process, you decide
# to write a Python program. 

# This program should ask the user for:
# 1. birthday person's name
# 2. the age that they are turning that year
# 3. personal message from the sender

# Finally, the program prints out a personalized invitation
# message.

# ### Sample output:
# "Happy <Age>th birthday <Name>! <Message>"

# name = input("What is the person's name?\n")
# age = input("What age is he/she turning this year?\n")
# per_message = input("What is your personal message for him/her?\n")
# print("Happy " + age + "th " + "birthday " + name + "! " + per_message)

## Task 1: Repeated Sentence Loop

# Print the sentence "I like chicken rice." 100 times using the
# 'for' loop

# for i in range(100):
#     print("I like chicken rice.")

## Task 3: Sentence Repetition Loop with Order of Code
##         Sequence

# Using the 'for' loop, print the following sentences sequence
# 100 times:
# "I like cake."
# "Give me more"
# for i in range(100):
#     print("I like cake")
#     print("Give me more")
    
# print 100 to 1
# for count in range(100,0,-1):
#     print(count)

## Task 5: range(start, stop)

# **Task 5a**:
# Print numbers from 1 to 5 using a 'for' loop.

# **Task 5b**:
# Print numbers from 51 to 100 using a 'for' loop.

# **Task 5c**:
# Print numbers from 18 to 29 using a 'for' loop.

# for i in range(1,6):
#     print(i)

# for i in range(51,101):
#     print(i)

# for i in range(18,30):
#     print(i)


# ## Task 6: range(start, stop, step)

# **Task 6a**:
# Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.

# **Task 6b**:
# Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.

# **Task 6c**:
# Use a 'for' loop to print numbers from 5 to 1 in descending order.

# **Task 6d**:
# Use a 'for' loop to print odd numbers from 51 to -35 in descending order.

# **Task 6e**:
# Use a 'for' loop to print even numbers from 32 to -67 in descending order.

# for i in range(2,25,2):
#     print(i)

# for i in range(8,97,8):
#     print(i)
# for i in range(5,0,-1):
#     print(i)

# for i in range(51,-36,-2):
#     print(i)

## Task 7: Countdown timer

# **Task 7a**:
# Imagine you are the race official and to start the race, you
# must say the following:

#     Ready!
#     3
#     2
#     1

# Using a 'for' loop, recreate the above sequence.

# **Task 7b**:
# Create a countdown timer that counts from 10 to 1.
# When the timer hits 1, print "Boo!"

# print("Ready!")
# for i in range(3,0,-1):
#     print(i)

# for i in range(10,1,-1):
#     print(i)
# print("1. Boo!")

# **Task 6e**:
# Use a 'for' loop to print even numbers from 32 to -67 in descending order.

# for i in range(32,-67,-2):
#     print(i)


## Task 8: User-Defined Range Counter

# Using input(), ask the user for 2 numbers and store them in the
# variables:
# 1. start
# 2. stop

# Write a 'for' loop to count from **start** to **stop**

# Note:
# What happens if the user inputs a higher start number than stop?
# Modify your code to be able to handle that scenario.

# start = int(input("What is the start number?\n"))
# stop = int(input("What is the stop number?\n"))
# for i in range(start,stop,):
#     print(i)


## Task 9: Accumulative Sum in Loop

# 1. Create a variable 'num' and assign the integer "0" to it
# 2. Create a 'for' loop that repeats 10 times
# 3. Add the sum of 'num' and the loop's parameter and print out
#    the value.
# 4. Observe what happens.

# num = 0
# for i in range(10):
#     num = num + i
#     print(num)

# 0 + 1 + 2 + 3 + 4 + ... + 9
# 1 + 3 + 5 + ... + 21

# num = 0
# for i in range(1,21,2):
#     num = num + i
#     print(num)

## Task 9: Name Cheer

# Your school's Sports Day is coming up and you are coding a
# program to cheer your schoolmates up.

# Your program needs to:
# 1. Using input(), ask the user for their namee e.g. <Dave>
# 2. Print a cheer as shown below:
   
#     ### Example:
#     What is your name? [Input: "Dave"]
#     Give me a D!
#     Give me a a!
#     Give me a v!
#     Give me a e!
#     What do we have?
#     Dave is the best!

# Note:
#     Notice how "Give me a..." is repeated!
#     Which function should you be using?

# name = input("What is the your name?\n")
# for char in range(len(name)):
#     print("Give me a " + name[char] + "!")
# print("What do we have?")
# print(name + " is the best!") 

# 3 + 8 + 13 + ... + 33
# total = 0
# for i in range(3,34,2):
#     total = total + i
#     print(total)

# - 14 - 12 - 10 - ... - 0 - (-2) - (-4) - ... (-14)
total = 0
for i in range(-14,15,2):
    total = total + i
    print(total)