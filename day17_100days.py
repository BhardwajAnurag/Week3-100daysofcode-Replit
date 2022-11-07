#each player's input is hidden
from getpass import getpass as input
print("Rock Paper Scissor Battle")
count = 0
winp1 = 0
winp2 = 0
while True:
  count += 1
  print(f"Round {count}")
  print(f"Scores:\nPlayer 1 has won {winp1} round(s)\nPlayer 2 has won {winp2} round(s)")
  print("Select your move (R, P or S)")
  p1 = input("Player 1 > ").lower()
  p2 = input("Player 2 > ").lower()
  if p1 == p2:
    print("Tie, please try again")
  elif p1 == "r":
    if p2 == "p":
      winp2 += 1
      print("Player 2 winner")
    elif p2 == "s":
      winp1 += 1
      print("Player 1 winner")
    else:
      print("Try again")
  elif p1 == "p":
    if p2 == "s":
      winp2 += 1
      print("Player 2 winner")
    elif p2 == "r":
      winp1 += 1
      print("Player 1 winner")
    else:
      print("Try again")
  elif p1 == "s":
    if p2 == "r":
      winp2 += 1
      print("Player 2 winner")
    elif p2 == "p":
      winp1 += 1
      print("Player 1 winner")
    else:
      print("Try again")
  else:
    print("Try again")
    exit()
  if winp1 >= 3 or winp2 >= 3:
    break
  else:
    continue
print("Game over!")

# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#     continue
#   else:
#     print("Game over!")
#     exit()
# print("Thanks for playing!")

# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")