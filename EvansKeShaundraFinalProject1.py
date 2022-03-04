import random
moves = ['Rock','Paper','Scissors']
player_wins = ['rockScissors','paperRock','scissorsPaper']
while True:
    Player_move =input("Your move:")
    if Player_move == 'q':
        break
    computer_move = random.choice(moves)
    print("You:", Player_move)
    print("Me:",computer_move)
    if Player_move == computer_move:
        print("Tie")
    elif Player_move + computer_move in player_wins:
        print("You win!")
    else:
        print("You lose!")
