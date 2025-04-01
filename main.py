from turns import turn
from turns import steal
from turns import next_hole
from UI import print_board


def mancala():
    board = {"A1": 4, "A2": 4, "A3": 4, "A4": 4, "A5": 4, "A6": 4,
             "B1": 4, "B2": 4, "B3": 4, "B4": 4, "B5": 4, "B6": 4,
             "store_increase": 0, "go_again": 0}  # not actual spaces on the board, but useful for special rules
    a_store = 0
    b_store = 0
    print_board(board, a_store, b_store)
    player = "A"
    while True:
        print("Player " + player + "'s turn")
        if board["A1"] == 0 and board["A2"] == 0 and board["A3"] == 0 and board["A4"] == 0 and board["A5"] == 0 and board["A6"] == 0:
            board["B1"], board["B2"], board["B3"], board["B4"], board["B5"], board["B6"] = 0, 0, 0, 0, 0, 0
            b_store += 48 - (a_store + b_store)
            break
        if board["B1"] == 0 and board["B2"] == 0 and board["B3"] == 0 and board["B4"] == 0 and board["B5"] == 0 and board["B6"] == 0:
            board["A1"], board["A2"], board["A3"], board["A4"], board["A5"], board["A6"] = 0, 0, 0, 0, 0, 0
            a_store += 48 - (a_store + b_store)
            break
        while True:
            hole_choice = input("Which hole do you choose? ")
            try:
                board = turn(player, hole_choice, board)
                break
            except:
                print("Invalid Hole")
        if player == "A":
            a_store += board["store_increase"]
        else:
            b_store += board["store_increase"]
        board["store_increase"] = 0
        print_board(board, a_store, b_store)
        if board["go_again"] == 1:
            board["go_again"] = 0
            continue
        if player == "A":
            player = "B"
        else:
            player = "A"
    print_board(board, a_store, b_store)
    if a_store > b_store:
        print("Player A wins!")
    elif b_store > a_store:
        print("Player B wins!")
    else:
        print("It's a tie!")


mancala()
