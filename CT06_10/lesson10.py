# import random
# ran_num = random.randint(1,10)
# print(ran_num)
# guess = int(input("What is your guess? "))
# if guess == ran_num:
#     print("Congratulations.")

# num = int(input("What is the number?\n"))
# if num > 0:
#     print(str(num) + " is positive.")
# else:
#     print(str(num) + " is negative.")

# age = int(input("What is your age?\n"))
# if age < 13:
#     print("You are a Child.")
# else:
#     if age < 20 and age > 12:
#         print("You are a Teen.")
#     else:
#         print("You are a Adult.")

# age = int(input("What is your age?\n"))
# if age < 13:
#     print("You are a Child.")
# elif age < 20:
#     print("You are teen.")
# else:
#     print("You are an adult.")

# temp = int(input("What is the temperature?\n"))
# if temp > 30:
#     print("Go swimming")
# elif temp >= 25:
#     print("Go play Basketball")
# elif temp >= 20:
#     print("Go cycling")
# else:
#     print("Read indoor")

# score = int(input("What is your score?"))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# age = int(input("What is your age?\n"))
# if age < 0:
#     print("Age cannot be negative.")
# elif age >= 18:
#     print("Eligible to vote.")
# else:
#     print("Not eligible to vote.")

money = int(input("How much money do you have?\n"))
if money >= 150:
    print("You can buy a gaming keyboard")
elif money >= 100:
    print("You can buy a new game.")
elif money >= 50:
    print("You can buy a gaming mouse")
elif money >= 20:
    print("You can buy a mousing pad")
else:
    print("You can only buy snacks")