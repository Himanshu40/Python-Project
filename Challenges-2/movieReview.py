# Challenge 4 : Create a function named movie_review() that has one parameter named rating.
#               If rating is less than or equal to 5, return "Avoid at all costs!".
#               If rating is between 5 and 9, return "This one was fun.". 
#               If rating is 9 or above, return "Outstanding!"
# Date        : Thu 28 May 2020 07:31:11 AM IST

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif (rating >= 5) and (rating <= 9):
        return "This one was fun."
    elif rating >= 9:
        return "Outstanding!"

print(movie_review(9))
print(movie_review(4))
print(movie_review(6))