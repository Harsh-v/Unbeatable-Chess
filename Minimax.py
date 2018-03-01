import chess

def minimax(board, depth, maximize):
    if board.is_checkmate():
        return -40 if maximize else 40
    elif board.is_game_over():
        return 0

    if depth == 0:
        return boardValue(board)

    if maximize:
        bestValue = float("-inf")
        for move in board.legal_moves:
            experimentBoard = board.copy()
            experimentBoard.push(move)
            value = minimax(experimentBoard, depth, False)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = float("inf")
        for move in board.legal_moves:
            experimentBoard = board.copy()
            experimentBoard.push(move)
            value = minimax(experimentBoard, depth - 1, True)
            bestValue = min(bestValue, value)
        return bestValue

    return 0

def boardValue(board):
    boardString = board.fen().split()[0]
    pawnDiff = boardString.count("P") - boardString.count("p")
    rookDiff = boardString.count("R") - boardString.count("r")
    knightDiff = boardString.count("N") - boardString.count("n")
    bishopDiff = boardString.count("B") - boardString.count("b")
    queenDiff = boardString.count("Q") - boardString.count("q")

    return 1*pawnDiff + 3*bishopDiff + 3*knightDiff + 5*rookDiff + 9*queenDiff

if __name__ == "__main__":
    gameBoard = chess.Board()

    while True:

        print(gameBoard)
        print(gameBoard.legal_moves)
        userMove = raw_input("Enter the move you want to make: ")
        gameBoard.push_san(userMove)

        if gameBoard.is_checkmate():
            print(gameBoard)
            print("User wins!")
            break
        elif gameBoard.is_game_over():
            print(gameBoard)
            print("Tie game")
            break

        minValue = float("inf")
        minMove = None
        for move in gameBoard.legal_moves:
            experimentBoard = gameBoard.copy()
            experimentBoard.push(move)
            value = minimax(experimentBoard, 2, False)

            if value < minValue:
                minValue = value
                minMove = move

        gameBoard.push(minMove)
        if gameBoard.is_checkmate():
            print(gameBoard)
            print("Computer wins")
            break
        elif gameBoard.is_game_over():
            print(gameBoard)
            print("Tie game")
            break
