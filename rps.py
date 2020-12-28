import getpass
#player 1's input
player1_input = [getpass.getpass("Player 1's turn, Choose an item (Type R for Rock, P for Paper, S for Scissors\n: ").lower()]
#player 2's input
player2_input = [input("Player 2's turn, Choose an item (Type R for Rock, P for Paper, S for Scissors)\n:  ").lower()]

def winner():
    #logic of which player won

    if player1_input == player2_input:
        return 'Game is a tie'
    elif  player1_input == ['r'] and player2_input == ['p']:
        return 'player2 won'
    elif player1_input == ['r'] and player2_input == ['s']:
        return 'player1 won'
    elif player1_input == ['p'] and player2_input == ['r']:
        return 'player1 won'
    elif player1_input == ['p'] and player2_input == ['s']:
        return 'player2 won'
    elif player1_input == ['s'] and player2_input == ['r']:
        return 'player2 won'
    elif player1_input == ['s'] and player2_input == ['p']:
        return 'player1 won'

    elif (player1_input and player2_input == ['r']) or (player1_input and player2_input == ['p']) or (player1_input and player2_input == ['s']):
        return 'Game is a tie'

    elif player1_input != ['r', 'p', 's'] and player2_input != ['r', 'p', 's']:
        if player1_input != ['r', 'p', 's']:
            return 'Player1: invalid input'
        elif player2_input != ['r', 'p', 's']:
            return 'Player2: invalid input'
        return 'Player1 & Player2: invalid input'


def play_game():
    # Start game by getting the player's input
    player1_input
    player2_input
    # check winner logic to see who won
    return winner()


print(play_game())
