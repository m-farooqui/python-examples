#board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#display board
def display_board():
    print(board[0] + " | " + board[1] + " | "+ board[2])
    print(board[3] + " | " + board[4] + " | "+ board[5])
    print(board[6] + " | " + board[7] + " | "+ board[8])
#play game
def play_game():
    #display intial play
    display_board()
    #handle turn
    handle_turn()
    
def handle_turn():
    position = input("Choose a position from 1 to 9")
    position = int(position) -1 

    board[position] = "X"

    display_board()
#check win    
def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #check rows
    #check columns
    #check diagonals
    return  :  
play_game()

#check rows
#check column
#check diagnals
#check tie
#flip player
