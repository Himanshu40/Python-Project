# Challenge 4 : Create a function called divisible_by_ten() that has one parameter named num.
#               The function should return True if num is divisible by 10, and False otherwise.
# Date        : Thu 28 May 2020 07:08:28 AM IST

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(divisible_by_ten(20))
print(divisible_by_ten(25))