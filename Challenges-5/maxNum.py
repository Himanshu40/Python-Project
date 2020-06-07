# Challenge 8 : Create a function named max_num() that takes a list of numbers named nums as a parameter.
#               The function should return the largest number in nums
# Date        : Sun 07 Jun 2020 09:19:45 AM IST

def max_num(nums):
  maximum = nums[0]

  for i in range(len(nums)):
    if maximum < nums[i]:
      maximum = nums[i]

  return maximum


print(max_num([50, -10, 0, 75, 20]))
print(max_num([-50, -20]))
