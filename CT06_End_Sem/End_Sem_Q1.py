# ============================================================
# Q1a. Multiples of 10
# ============================================================
# You are writing a program to print numbers from 10 to 200.
# The program must use a while loop and increase in multiples of 10.

# Program Requirements:
# - Start from 10
# - End at 200
# - Increase by 10 each time
# - Use a while loop

# ============================================================

num = 0
while num != 200:
    num += 10
    print(num)

#     ============================================================
# Q1b. Password Checker
# ============================================================
# You are writing a program to check a password.

# The program must:
# - Store the password "superpass123"
# - Ask the user to enter a password
# - If correct, print:
#     Access Granted
# - If wrong, print:
#     Access Denied

# ============================================================

password = "superpass123"
input_pass = input("Enter password")
if input_pass == password:
    print("Access Granted")
else:
    print("Access Denied")