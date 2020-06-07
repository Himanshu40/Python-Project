# Challenge 5 : Create a function named exponents() that takes two lists as parameters named bases and powers. 
#               Return a new list containing every number in bases raised to every number in powers.
# Date        : Sun 07 Jun 2020 07:33:10 AM IST

def exponents(bases, powers):
  list1 = []
  for i in range(len(bases)):
    for j in range(len(powers)):
      list1.append(pow(bases[i], powers[j]))
  return list1


print(exponents([2, 3, 4], [1, 2, 3]))
