# Challenge 1 : Write a function named append_sum that has one parameter — a list named named lst.
#               The function should add the last two elements of lst together and append the result to lst. 
#               It should do this process three times and then return lst.
# Date        : Fri 05 Jun 2020 05:40:06 AM IST

def append_sum(lst):
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    return lst

print(append_sum([1, 1, 2]))
