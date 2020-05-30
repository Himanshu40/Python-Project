# Project : Games of Chance
# Date    : Sat 30 May 2020 06:06:00 AM IST

import random

money = 100

def coinFlip(betAmount, guess):
    result = random.randint(1, 2)

    if (result == 1) and (guess == "Heads"):
        return betAmount
    elif (result == 2) and (guess == "Tails"):
        return betAmount
    else:
        return -betAmount


def choHan(betAmount, guess):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    sum = dice1 + dice2

    if (sum % 2 == 0) and (guess == "Even"):
        return betAmount
    elif (sum % 2 != 0) and (guess == "Odd"):
        return betAmount
    else:
        return -betAmount


def cardPick(betAmount):
    yourCard = random.randint(1, 13)
    oppCard  = random.randint(1, 13)

    if yourCard > oppCard:
        return betAmount
    elif oppCard > yourCard:
        return -betAmount
    elif oppCard == yourCard:
        return 0


def roulette(betAmount, guess):
    ballResult = random.randint(0, 36)

    if ballResult == guess:
        return betAmount * 34
    elif (guess == "Even") and (ballResult % 2 == 0):
        return betAmount
    elif (guess == "Even") and (ballResult % 2 != 0):
        return -betAmount
    elif (guess == "Odd") and (ballResult % 2 == 0):
        return betAmount
    elif (guess == "Odd") and (ballResult % 2 != 0):
        return -betAmount
    elif ballResult != guess:
        return -betAmount



money += coinFlip(20, "Heads")
print("Current Money after playing Coin Flip game = $" + str(money))

money += coinFlip(35, "Tails")
print("Current Money after playing Coin Flip game = $" + str(money))

money += choHan(46, "Even")
print("Current Money after playing Cho Han game = $" + str(money))

money += cardPick(31)
print("Current Money after playing Card Pick game = $" + str(money))

money += roulette(0, -40)
print("Current Money after playing Roulette game = $" + str(money))

money += roulette(13, "Odd")
print("Current Money after playing Roulette game = $" + str(money))