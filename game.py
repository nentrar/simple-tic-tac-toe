board_positions = {
    1 : " ",
    2 : " ",
    3 : " ",
    4 : " ",
    5 : " ",
    6 : " ",
    7 : " ",
    8 : " ",
    9 : " "
}

gameOn = True

def show_board():
    print("{} | {} | {} \n{} | {} | {} \n{} | {} | {} ".format(
        board_positions[1],
        board_positions[2],
        board_positions[3],
        board_positions[4],
        board_positions[5],
        board_positions[6],
        board_positions[7],
        board_positions[8],
        board_positions[9]))

def show_full_board():
    print("{} | {} | {} \n{} | {} | {} \n{} | {} | {} ".format(
        "1", "2","3","4","5","6","7","8","9"))


def player_a_choice():
    choice = int(input("What position for an X? Choose from 1 to 9: "))
    for position in board_positions:
        if position == choice:
            board_positions[position] = "X"
    show_board()

def player_b_choice():
    choice = int(input("What position for an O? Choose from 1 to 9: "))
    for position in board_positions:
        if position == choice:
            board_positions[position] = "O"
    show_board()

def check_winner():
    if board_positions[1] == board_positions[2] and board_positions[2] == board_positions[3]:
        print("We have the winner!")



def tic_tac_toe():
    show_full_board()
    print("Let's start Tic Tac Toe game! X player start first!")
    while gameOn:
        player_a_choice()
        player_b_choice()
        check_winner()


tic_tac_toe()

''' Below conditions for winning to implement to a function
1 2 3
4 5 6
7 8 9
1 4 7
2 5 8
3 6 9
1 5 9
3 5 7'''
