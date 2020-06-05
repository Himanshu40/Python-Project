# Challenge 5 : Write a function named combine_sort that has two parameters named lst1 and lst2.
#               The function should combine these two lists into one new list and sort the result. 
#               Return the new sorted list.
# Date        : Fri 05 Jun 2020 05:56:34 AM IST

def combine_sort(lst1, lst2):
    newList = lst1
    newList += lst2
    newList.sort()
    return newList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
