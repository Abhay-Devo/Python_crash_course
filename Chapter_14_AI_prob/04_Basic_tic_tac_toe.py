"""Project 4: Text-based Tic-Tac-Toe

Description: Build a text-based Tic-Tac-Toe game for two players.

Skills: Lists (to store the board), loops, conditionals, functions.

Challenge: Implement a feature to detect when a player wins or if there's a tie..."""



 
# Displaying Tic Tac Toe board with position numbers 
def platform():
    print("      1  |  2  |  3  ")
    print("    -----|-----|-----")
    print("      4  |  5  |  6  ")
    print("    -----|-----|-----")
    print("      7  |  8  |  9  ")


# Displaying board everytime after user put (x/o) acc to the position 
def display_board(board):
    print("")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("")


def check_winner(player, board):
    # Making winning scenarios in form of list of lists
    winning_scenario = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows winning 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns  
        [0, 4, 8], [2, 4, 6]              # Diagonals 
    ]
    
    # If any of the combo is matched with the user input true will return else false
    for combo in winning_scenario:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
    
# if ' ' space in not available in board will return false
def check_tie(board):
    return ' ' not in board
        

def play_game():
    # Creating the board with spaces with 9 position 
    board = [' ' for _ in range(9)]
    current_player = 'X'           # Setting the default/first player as 'X' always
    game_running = True     

    print("\nWelcome to Tic Tac Toe playing game:\n")
    platform()

    # Running the main loop
    while game_running:
        try:
            choice = int(input(f"Player {current_player}, Enter your position in the chart(0-9):"))-1
        except Exception as e:
            print("Invalid input!!! Please enter a valid input...")
            continue
        
        # If user enter position not in the range or place is not availale at that position
        if choice < 0 or choice > 9 or board[choice] != ' ':
            print("Invalid move!!! Please try again...")
            continue
        
        # Displaying board after user input
        board[choice]= current_player
        display_board(board)

        # checking for winner or tie
        if check_tie(board):
            print("It's a tie\n")
            game_running = False
        elif check_winner(current_player, board):
            print(f"Player {current_player} wins!!!")
            game_running = False
        else:
            # Changing the current player after every input of first player 
            # until any of the above condition gets true.
            current_player = 'O' if current_player == 'X' else 'X'

    # Exiting the program
    while exit:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            play_game()
            break
        elif play_again == 'no':
            print("Thank you for playing Tic-Tac-Toe!")
            break
        else:
            print("Invalid input!!!")
            continue

if __name__ == "__main__":
    play_game()



