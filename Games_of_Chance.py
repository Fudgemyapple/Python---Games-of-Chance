import random 

money = 100

#Coint Flip Game

def zero_or_one():
    ans = random.randint(0, 1)
    return ans

def coin_flip_bet(bet, outcome, money):
    money = money - bet
    flip = zero_or_one()
    if outcome == flip:
        winnings = bet*2
        money = money + winnings 
        if flip == 1:
            result = "Tails"
        else:
            result = "Heads" 
        return print("It was " + result + "!" + " You have WON! Your winnings for this game are $" + str(winnings) + "!") 
    else:
        if flip == 1:
            result = "Tails"
        else:
            result = "Heads"
        losses = bet
        return print("It was " + result + "!" + " You have LOST! Your losses for this game are -$" + str(losses) + "!") 

def heads_or_tails_conversion(heads_or_tails):
    if heads_or_tails.lower() == "heads":
        outcome_bet = 0
        return outcome_bet
    elif heads_or_tails.lower() == "tails":
        outcome_bet = 1
        return outcome_bet

def check_money(bet_amount, money):
    if bet_amount <= money:
        return 
    else:
        print("You don't have enough money to bet that amount") 
        return 

def coin_flip_game_start():
    print("Welcome to the heads or tails game first you need to play a bet below. You have up to $100 to play with.")
    bet_amount = input("Amount you would like to bet $")
    while int(bet_amount) > money:
        print("You don't have enough money to bet that amount. You have $" + str(money)) 
        bet_amount = input("How much would you like to bet?" " $")
    heads_or_tails = input("Heads or Tails?")
    while heads_or_tails.lower() != "heads" and heads_or_tails.lower() != "tails":
        print("You have not entered either heads or tails.")
        heads_or_tails = input("Heads or Tails?")
    outcome_bet = heads_or_tails_conversion(heads_or_tails)
    return coin_flip_bet(int(bet_amount), outcome_bet, money)

coin_flip_game_start()