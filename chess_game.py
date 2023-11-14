def draw_chessboard():
    for i in range(8):
        for j in range(8):
            print("██" if (i + j) % 2 == 0 else "  ", end="")
        print()

draw_chessboard()
