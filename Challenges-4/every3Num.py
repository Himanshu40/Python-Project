# Challenge 1 : Create a function called every_three_nums that has one parameter named start.
#               The function should return a list of every third number between start and 100 (inclusive).
# Date        : Fri 05 Jun 2020 06:20:22 AM IST

def every_three_nums(start):
    list1 = []
    
    if start > 100:
        return list1
    else:
        list1 = range(start, 101, 3)
        return list1

print(every_three_nums(91))
