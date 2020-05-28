# Challenge 1 : Create a function named in_range() that has three parameters named num, lower, and upper.
#               The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
# Date        : Thu 28 May 2020 07:18:15 AM IST

def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))