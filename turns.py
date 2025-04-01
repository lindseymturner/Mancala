def next_hole(hole, p):
    """
    returns the next hole on the board
    :param hole: current hole
    :param p: which player's turn it is
    :return: the next hole on the mancala board
    """
    if p == "A":
        a_holes = ["A1", "A2", "A3", "A4", "A5", "A6", "store_increase", "B1", "B2", "B3", "B4", "B5", "B6"]
        if hole == "B6":
            return "A1"
        x = a_holes.index(hole)
        return a_holes[x + 1]
    else:
        b_holes = ["A1", "A2", "A3", "A4", "A5", "A6", "B1", "B2", "B3", "B4", "B5", "B6", "store_increase"]
        if hole == "store_increase":
            return "A1"
        x = b_holes.index(hole)
        return b_holes[x+1]


def steal(p: str, hole: [str], board:[dict]):
    if p not in hole:
        return board
    if board[hole] > 1:
        return board
    if p == "A":
        opposite = "B"
    else:
        opposite = "A"
    opposite += str((7 - int(hole[1:])))
    if board[opposite] == 0:
        return board
    board['store_increase'] += board[hole] + board[opposite]
    board[hole] = 0
    board[opposite] = 0
    return board


def turn(p: [str], hole: [str], board: [dict]) -> dict:
    """
    method that makes the changes after a player takes their turn
    :param p: which player is taking a turn
    :param hole: which hole the player is picking
    :param board: the current game board
    :return: the updated game board
    """
    assert p in hole
    assert board[hole] != 0
    num_stones = board[hole]  # remember number of stones for distribution
    board[hole] = 0  # remove stones from chosen hole
    current_hole = hole
    while num_stones > 0:
        current_hole = next_hole(current_hole, p)
        board[current_hole] += 1
        num_stones -= 1
    if current_hole == "store_increase":
        board["go_again"] = 1
    board = steal(p, current_hole, board)
    return(board)


