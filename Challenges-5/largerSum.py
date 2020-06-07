# Challenge 6 : Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
#               The function should return the list whose elements sum to the greater number. 
#               If the sum of the elements of each list are equal, return lst1.
# Date        : Sun 07 Jun 2020 07:40:58 AM IST

def larger_sum(lst1, lst2):
  totalLst1 = 0
  totalLst2 = 0
  
  for i in lst1:
    totalLst1 += i
  
  for j in lst2:
    totalLst2 += j
  
  if totalLst1 > totalLst2:
    return lst1
  elif totalLst1 < totalLst2:
    return lst2
  else:
    return lst1


print(larger_sum([1, 9, 5], [2, 3, 7]))
