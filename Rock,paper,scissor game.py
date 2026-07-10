#function to check both players choices
def check_choices(player1,player2):
    if player1==player2:
        print(f'You both chose {player1}.It\'s a tie!!!')
    elif player1=='rock':
        if player2=='paper':
            print("Player2 wins (paper covers rock)")
        else:
            print("Player1 wins (rock crushes scissors)")
    elif player1=='paper':
        if player2=='rock':
            print("Player1 wins (paper covers rock)")
        else:
            print("Player2 wins (scissors cuts paper)")
    elif player1=='scissors':
        if player2=='rock':
            print("Player2 wins (rock crushes scissors)")
        else:
            print("Player1 wins (scissors cuts paper)")
#loop to keep playing while both players wants
while True:
    player1=input("Player1:Choose between rock,paper and scissors ").lower()
    while player1 not in ("rock","paper","scissors"):
        print("Error in input.Try again!")
        player1=input("Player1:Choose between rock,paper and scissors ").lower()
    player2=input("Player2:Choose between rock,paper and scissors ").lower()
    while player2 not in ("rock","paper","scissors"):
         print("Error in input.Try again!")
         player2=input("Player2:Choose between rock,paper and scissors ").lower()
    print(f'Player1 chose {player1},Player2 chose {player2}')
    check_choices(player1,player2)
    print("End of game!")
    play_again=input("Do you want to play again?(y/n)").lower()
    if play_again!='y':
        print("Bye!")
        break