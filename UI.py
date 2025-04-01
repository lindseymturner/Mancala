def print_board(board, s1, s2):
    hole_values = [board["A1"], board["A2"], board["A3"], board["A4"], board["A5"], board["A6"],
                   board["B1"], board["B2"], board["B3"], board["B4"], board["B5"], board["B6"]]
    print(" -----------------------------")
    print(" |   "+str(board["B6"])+"   "+str(board["B5"])+"   "+str(board["B4"])+"   "+str(board["B3"])+"   "+str(board["B2"])+"   "+str(board["B1"])+"   |")
    print(str(s2)+"|   "+str(board["A1"])+"   "+str(board["A2"])+"   "+str(board["A3"])+"   "+str(board["A4"])+"   "+str(board["A5"])+"   "+str(board["A6"])+"   |"+str(s1))
    print(" -----------------------------")
