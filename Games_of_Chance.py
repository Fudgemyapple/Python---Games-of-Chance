import random

money = 100


#Coint Flip Game

def zero_or_one():
    ans = random.randint(0, 1)
    return ans

def coin_flip_bet(bet, outcome, money):
    money = money - bet
    if outcome == zero_or_one():
        winnings = bet*2
        money = money + winnings 
        return print("You have WON! Your winnings for this game are " + str(winnings) + "!") 
    else:
        losses = bet
        return print("You have LOST! Your losses for this game are -" + str(losses) + "!") 
    
coin_flip_bet(100, 1, money)
