def printBoard(xState, zState):
    zero = 'X' if xState[0] == 1 else 'O' if zState[0] == 1 else '0'
    one = 'X' if xState[1] == 1 else 'O' if zState[1] == 1 else '1'
    two = 'X' if xState[2] == 1 else 'O' if zState[2] == 1 else '2'
    three = 'X' if xState[3] == 1 else 'O' if zState[3] == 1 else '3'
    four = 'X' if xState[4] == 1 else 'O' if zState[4] == 1 else '4'
    five = 'X' if xState[5] == 1 else 'O' if zState[5] == 1 else '5'
    six = 'X' if xState[6] == 1 else 'O' if zState[6] == 1 else '6'
    seven = 'X' if xState[7] == 1 else 'O' if zState[7] == 1 else '7'
    eight = 'X' if xState[8] == 1 else 'O' if zState[8] == 1 else '8'
    print(f"\t {zero} | {one} | {two}")
    print(f"\t --|---|--")
    print(f"\t {three} | {four} | {five}")
    print(f"\t --|---|--")
    print(f"\t {six} | {seven} | {eight}")


def sumVals(x, y, z):
    return x + y + z


def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if (sumVals(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print('\n X won the game \n')
            return 1

        if (sumVals(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print('\n O won the game \n')
            return 0

    return -1


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for x 0 for O
    print("Welcome to Tic Tac Toe Game \n")
    while (True):
        printBoard(xState, zState)
        if (turn == 1):
            print("\nX's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("\nO's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1

        turn = 1 - turn

        result = checkWin(xState, zState)

        if result != -1:
            print("\n Match Over \n")
            print("\n Final Results :- \n")
            printBoard(xState, zState)
            break
