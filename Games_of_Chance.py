import random 


#casino start message and menu 

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


#function to run coin flip game
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

#cho-han game

def dice_roll():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    rollsum = roll1 + roll2
    return rollsum 

def chohan_game_start():
    print("In this game 2 dice are rolled, you have to guess whether the sum of these dice will be even or odd")
    guess = input("Even or Odd? ")
    
    if dice_roll() % 2 == 0:
        roll = 0
        answer = "Even"
    else:
        roll = 1
        answer = "Odd"
    
    if guess.lower() == "even":
        num_guess = 0
    else:
        num_guess = 1

    if roll == num_guess:
        print("It was " + answer + "Won!") 
    else:
        print("It was " + answer + "Lost!")  


    




print("Welcome to the CMD Casino. Below can you please enter the amount of money you will be playing with today.")
money = int(input("$"))
print("Please choose a game from below by inputing the number of the game.\n0. Coin Flip Game\n1. Cho-Han Game")
first_game = input()
games = ["coin_flip_game_start()", "chohan_game_start(), 2, 3, 4"]
print(games[int(first_game)])
