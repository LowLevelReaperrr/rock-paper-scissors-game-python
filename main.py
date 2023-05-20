# Rock, Paper, Scissors Game!
print("WELCOME TO MY ROCK, PAPER, SCISSORS GAME! ENJOY!")


# Defining Options with a Function
def rock_paper_or_scissors(player1, player2):
    if player1.lower() == player2.lower():
        print("TIE!")
    elif player1.lower() == 'rock' and player2.lower() == 'scissors':
        print("PLAYER 1 WINS!")
    elif player1.lower() == 'scissors' and player2.lower() == 'rock':
        print("PLAYER 2 WINS!")
    elif player1.lower() == 'paper' and player2.lower() == 'rock':
        print("PLAYER 1 WINS!")
    elif player1.lower() == 'rock' and player2.lower() == 'paper':
        print("PLAYER 2 WINS!")
    elif player1.lower() == 'scissors' and player2.lower() == 'paper':
        print("PLAYER 1 WINS!")
    elif player1.lower() == 'paper' and player2.lower() == 'scissors':
        print("PLAYER 2 WINS!")
    else:
        print("ERROR, TRY AGAIN!")




# While Loop just in case players would like to continue.


while True:
    player1 = input("Enter a choice (Rock, Paper, Scissors): ")
    player2 = input("Enter a choice (Rock, Paper, Scissors): ")
    rock_paper_or_scissors(player1, player2)
    choice = input("Keep playing? (Yes/No)")
    if choice.lower() == "no":
        break
