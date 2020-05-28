import random 


#casino start message and menu 

#Coint Flip Game

def zero_or_one():
    ans = random.randint(0, 1)
    return ans

#function to run coin flip game
def coin_flip_game_start(money):
    print("Welcome to the heads or tails game first you need to place a bet below. You have up to " + str(money) + " to play with.")
    bet_amount = int(input("Amount you would like to bet $"))
    while int(bet_amount) > money:
        print("You don't have enough money to bet that amount. You have $" + str(money)) 
        bet_amount = input("How much would you like to bet?" " $")
    heads_or_tails = input("Heads or Tails?")
    while heads_or_tails.lower() != "heads" and heads_or_tails.lower() != "tails":
        print("You have not entered either heads or tails.")
        heads_or_tails = input("Heads or Tails?")
    if heads_or_tails.lower() == "heads":
        num_heads_or_tails = 0
    elif heads_or_tails.lower() == "tails":
        num_heads_or_tails = 1
    money = money - int(bet_amount)
    flip = zero_or_one()
    if num_heads_or_tails == flip:
        money = money + bet_amount*2
        if flip == 1:
            result = "Tails"
        else:
            result = "Heads" 
            print("It was " + result + "!" + " You have WON! Your winnings for this game are $" + str(bet_amount*2) + "!") 
    else:
        if flip == 1:
            result = "Tails"
        else:
            result = "Heads"
            print("It was " + result + "!" + " You have LOST! Your losses for this game are -$" + str(bet_amount) + "!") 
    return game_interlude(money)
    





#cho-han game

def dice_roll():
    roll1 = random.randint(1, 6)
    return roll1 

def chohan_game_start(money):
    print("In this game 2 dice are rolled, you have to guess whether the sum of these dice will be even or odd")
    bet_amount = input("How much would you like to bet?")
    while int(bet_amount) > money:
        print("You don't have enough money to bet that amount. You have $" + str(money)) 
        bet_amount = input("How much would you like to bet?" " $")
    guess = input("Even or Odd? ")
    while guess.lower() != "even" and guess.lower() != "odd":
        print("You have not entered either EVEN or ODD.")
        guess = input("EVEN or ODD?")
    money -=  int(bet_amount)
    
    if dice_roll() % 2 == 0:
        roll = 0
        answer = "EVEN"
    else:
        roll = 1
        answer = "ODD"
    
    if guess.lower() == "even":
        num_guess = 0
    else:
        num_guess = 1

    if roll == num_guess:
        print("It was " + answer + " You have WON!")
        money = bet_amount*2 
    else:
        print("It was " + answer + " You have LOST!")  
    return game_interlude(money)


#game chooser 
def game_interlude(money):
    print("Thank you for playing with us, you now have $" + str(money))
    print("Please choose a game from below by inputing the number of the game.\n0. Coin Flip Game\n1. Cho-Han Game")
    first_game = int(input())
    games = [coin_flip_game_start, chohan_game_start, 2, 3, 4]
    games[first_game](money)




print("Welcome to the CMD Casino. Below can you please enter the amount of money you will be playing with today.")
money = int(input("$"))
print("Please choose a game from below by inputing the number of the game.\n0. Coin Flip Game\n1. Cho-Han Game")
first_game = int(input())
games = [coin_flip_game_start, chohan_game_start, 2, 3, 4]
games[first_game](money)
