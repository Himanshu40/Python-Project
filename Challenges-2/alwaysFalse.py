# Challenge 3 : Create a function named always_false() that has one parameter named num.
#               Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

def always_false(num):
    if (num <= 0) or (num >= 0):
        return False

print(always_false(0))
print(always_false(-1))
print(always_false(1))
