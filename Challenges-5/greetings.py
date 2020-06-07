# Challenge 2 : Create a function named add_greetings() which takes a list of strings named names as a parameter.
#               In the function, create an empty list that will contain each greeting. 
#               Add the string "Hello, " in front of each name in names and append the greeting to the list.
#               Return the new list containing the greetings.
# Date        : Sun 07 Jun 2020 07:02:37 AM IST

def add_greetings(names):
  list1 = []
  for name in names:
    list1.append("Hello, " + name)
  return list1


print(add_greetings(["Owen", "Max", "Sophie"]))
