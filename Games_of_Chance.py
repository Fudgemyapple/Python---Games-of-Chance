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
        if zero_or_one == 1:
            result = "Tails"
        else:
            result = "Heads" 
        return print("It was " + result + "!" + " You have WON! Your winnings for this game are $" + str(winnings) + "!") 
    else:
        if zero_or_one == 1:
            result = "Tails"
        else:
            result = "Heads"
        losses = bet
        return print("It was " + result + "!" + " You have LOST! Your losses for this game are -$" + str(losses) + "!") 

def heads_or_tails_conversion(heads_or_tails):
    if heads_or_tails == "Heads":
        outcome_bet = 0
        return outcome_bet
    elif heads_or_tails == "Tails":
        outcome_bet = 1
        return outcome_bet

print("Welcome to the heads or tails game first you need to play a bet below. You have up to $100 to play with.")
bet_amount = input("Amount you would like to bet $")
heads_or_tails = input("Heads or Tails?")
outcome_bet = heads_or_tails_conversion(heads_or_tails)
coin_flip_bet(int(bet_amount), outcome_bet, money)