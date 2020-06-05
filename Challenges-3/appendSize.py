# Challenge 4 : Create a function called append_size that has one parameter named lst.
#               The function should append the size of lst (inclusive) to the end of lst. 
#               The function should then return this new list.
# Date        : Fri 05 Jun 2020 05:53:31 AM IST

def append_size(lst):
    lst.append(len(lst))
    return lst

print(append_size([23, 42, 108]))
