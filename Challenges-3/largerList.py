# Challenge 2 : Write a function named larger_list that has two parameters named lst1 and lst2.
#               The function should return the last element of the list that contains more elements. 
#               If both lists are the same size, then return the last element of lst1.
# Date        : Fri 05 Jun 2020 05:45:24 AM IST

def larger_list(lst1, lst2):
    if (len(lst1) > len(lst2)):
        return lst1
    elif not (len(lst1) > len(lst2)):
        return lst2
    else:
        return lst1

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
