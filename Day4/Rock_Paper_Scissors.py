import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("This is a Rock Paper Scissors game!")
while True:
    moves = [rock, paper, scissors]
    ai_move = random.randint(0, 2)

    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "
                       "Type 3 to exit the game.\n"))

    if choice == 3:
        break
    if choice > 3 or choice < 0:
        print("Invalid input!")
        continue

    print(moves[choice])
    print(f"Computer chose {ai_move}:")
    print(moves[ai_move])
    if ai_move == choice:
        print("It's a draw!")
    elif (ai_move == choice + 1) or (ai_move == 0 and choice == 2):
        print("You lose!")
    else:
        print("You win!")
