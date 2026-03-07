# ============================================================
# Q2. Savings Simulator
# ============================================================
# You are building a small savings simulator.
# A person starts with a certain amount of money.

# Every day, the person saves more money than the previous day:

# Day 1 → save $1
# Day 2 → save $2
# Day 3 → save $3
# Day 4 → save $4
# … and so on

# The program must:
# - Ask for the starting amount of money.
# - Ask for the number of days.
# - For each day, add the correct savings amount.
# - Print the total money after each day.
# - Finally, print the final total amount.

# Program Requirements:
# - Use a for loop.
# - Use range() correctly.
# - Update the total amount inside the loop.
# - Print exactly in this format:
#     Day <X>: $<Y>
# - After the loop, print:
#     Total amount saved = $<Z>

# Note:
# - Follow the input order exactly as shown in the Test Cases.
# - You must get the correct output for ALL 3 test cases.

# ============================================================
# """

starting_amount = float(input("Starting amount: "))
num_days = int(input("Number of days: "))
total_amount = starting_amount
for day in range(1, num_days + 1):
    total_amount += day
    print(f"Day {day}: ${total_amount:.2f}")
print(f"Total amount saved = ${total_amount:.2f}")
