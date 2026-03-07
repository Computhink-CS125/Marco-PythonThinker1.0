### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:
# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + average_score)



# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger

word = input("What word would you like to repeat?")
n = int(input("How many times would you like to repeat it?"))
for i in range(n):
    print(word)

