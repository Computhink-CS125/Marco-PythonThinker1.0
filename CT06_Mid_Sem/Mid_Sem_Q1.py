# """
# ============================================================
# Q1. Bill Splitter
# ============================================================
# You are making a simple bill-splitting calculator for a group of friends.
# The program must ask for the total bill amount and how many people are sharing the bill.
# It should calculate how much each person pays (equal split).

# Program Requirements:
# - Ask the user for Total bill
# - Ask the user for Number of people
# - Calculate how much each person pays
# - Print the result exactly in this format:
#     Each person pays: $<amount>

# Note:
# - The output must be rounded to 2 decimal places (example: $25.25).
# - Follow the input order exactly as shown in the Test Cases.
# - You must get the correct output for ALL 3 test cases.

total_bill = float(input("Total bill: "))
num_people = int(input("Number of people: "))
amount_per_person = total_bill / num_people
print(f"Each person pays: ${amount_per_person:.2f}")
