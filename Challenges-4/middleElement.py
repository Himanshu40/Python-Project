# Challenge 5 : Create a function called middle_element that has one parameter named lst.
#               If there are an odd number of elements in lst, the function should return the middle element. 
#               If there are an even number of elements, the function should return the average of the middle two elements.
# Date        : Fri 05 Jun 2020 06:45:12 AM IST


def middle_element(lst):
    if not(len(lst) % 2 == 0):
        return lst[int((len(lst) / 2) + 1)]
    else:
        return (lst[int(len(lst) / 2 - 1)] + lst[int(len(lst) / 2)]) / 2

print(middle_element([5, 2, -10, -4, 4, 5]))
