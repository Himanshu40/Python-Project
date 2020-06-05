# Challenge 4 : Create a function named double_index that has two parameters: a list named lst and a single number named index.
#               The function should return a new list where all elements are the same as in lst except for the element at index. 
#               The element at index should be double the value of the element at index of the original lst.
#               If index is not a valid index, the function should return the original list.
# Date        : Fri 05 Jun 2020 06:38:32 AM IST

def double_index(lst, index):
    if index > len(lst):
        return lst
    else:
        newList = lst
        newList[index] *= 2
        return newList

print(double_index([3, 8, -10, 12], 2))
