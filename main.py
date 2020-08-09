import random

money = 100
money2= 100

#Write your game of chance functions here
def flipping_game(bet,guess):
  result= random.randint(1,2)
  if result==1:
    choice='heads'
  else:
    choice='tails'
  if choice==guess.lower():
    print("You Won!!")
    return bet*2
  else:
    print("You lost!!")
    return -bet
def ChoHan(bet,guess):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  if (dice1+dice2)%2==0:
    choice='even'
  else:
    choice='odd'
  if guess.lower()==choice:
    print('You won')
    return bet*2
  else:
    print("You Lost")
    return -bet
def picking_card(bet1,bet2):
  deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
  player1_number=random.choice(deck)
  player2_number=random.choice(deck)
  if player1_number > player2_number:
    print('Player1 won!')
    return '$'
  elif player1_number < player2_number:
    print('Player2 won!')
    return '&'
  else:
    print("It's a tie")
    return 0
def roulette(bet,guess):
  result = random.randint(1,36)
  if result%2==0:
    t='even'
  else:
    t='odd'
  if guess==t or guess==result:
    print('You won!')
    return bet*2
  else:
    return -bet







#Call your game of chance functions here
if money > 0:
  money += flipping_game(10,'head')
else:
  print("You dont have enough money to play ")
print("the amount of money left in ur bank is {}".format(money))
if money > 0:
  money += ChoHan(10,'odd')
else:
  print("You dont have enough money to play")
print("the amount of money left in ur bank is {}".format(money))
if money > 0 and money2 > 0:
  if picking_card(10,10) == '$':
    money = money + 20
    money2=money2-10
  else:
    money2 = money2 + 20
    money = money - 10
print("The amount of money left in ur bank is {}".format(money))
print("The amount of money left in player2's bank is {}".format(money2))
if money > 0:
  money+=roulette(10,'even')
else:
  print("You don't have enough money to pay")
print("The amount of money left in ur bank is {}".format(money))

