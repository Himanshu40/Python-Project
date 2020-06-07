# Challenge 4 : Create a function named odd_indices() that has one parameter named lst.
#               The function should create a new empty list and add every element from lst that has an odd index. 
#               The function should then return this new list.
# Date        : Sun 07 Jun 2020 07:25:09 AM IST

def odd_indices(lst):
  list1 = []
  for i in range(len(lst)):
    if i % 2 != 0:
      list1.append(lst[i])
  return list1


print(odd_indices([4, 3, 7, 10, 11, -2]))
