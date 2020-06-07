# Challenge 10 : Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
#                The function should return True if lst1 is the same as lst2 reversed. 
#                The function should return False otherwise.
# Date         : Sun 07 Jun 2020 09:43:32 AM IST

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True


print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
