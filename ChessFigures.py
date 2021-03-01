class Pawn():
    def __init__(self, board):
        self.board = board

    # Get all the pawn moves for the pawn located at row, col
    def getMoves(self, r, c, moves, whiteToMove, Move):
        # Moves for white pieces
        if whiteToMove:
            # Moves from start position
            if self.board[r-1][c] == "--":
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r, c), (r-2, c), self.board))
                    moves.append(Move((r, c), (r-1, c), self.board))
                # Basic pawn move
                else:
                    moves.append(Move((r, c), (r-1, c), self.board))

            # Pawn attack
            if c != 0 and self.board[r-1][c-1][0] == 'b':
                moves.append(Move((r, c), (r-1, c-1), self.board))

            if c != 7 and self.board[r-1][c+1][0] == 'b':
                moves.append(Move((r, c), (r-1, c+1), self.board))

        # Moves for black pieces
        if not whiteToMove:
            # Moves from start position
            if r == 1 and self.board[r+2][c] == "--" and self.board[r+1][c] == "--":
                moves.append(Move((r, c), (r+2, c), self.board))
                moves.append(Move((r, c), (r+1, c), self.board))

            # Basic pawn move
            elif self.board[r+1][c] == "--":
                moves.append(Move((r, c), (r+1, c), self.board))

            # Pawn attack
            if c != 0 and self.board[r+1][c-1][0] == 'w':
                moves.append(Move((r, c), (r+1, c-1), self.board))

            if c != 7 and self.board[r+1][c+1][0] == 'w':
                moves.append(Move((r, c), (r+1, c+1), self.board))


class Rook():
    def __init__(self, board):
        self.board = board
        # up, left, down, right
        self.directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

    # Get all rook moves for the rook located at row, col
    def getMoves(self, r, c, moves, whiteToMove, Move):
        # Color of enemy Pawn
        enemyColor = "b" if whiteToMove else "w"
        for d in self.directions:
            for i in range(1, 8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # Figure on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(
                            Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(
                            Move((r, c), (endRow, endCol), self.board))
                        break
                    else:  # Friendly piece invalid
                        break
                else:  # out of board
                    break


class Bishop():
    def __init__(self, board):
        self.board = board
        # top-left, top-right, bottom-right, bottom-left
        self.directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))

    # Get all the bishop moves for the bishop located at row, col
    def getMoves(self, r, c, moves, whiteToMove, Move):
        enemyColor = "b" if whiteToMove else "w"
        for d in self.directions:
            for i in range(1, 8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # Pieces on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':
                        moves.append(
                            Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(
                            Move((r, c), (endRow, endCol), self.board))
                        break
                    else:  # Friendly piece invalid
                        break
                else:  # Out of board
                    break


class Queen():
    def __init__(self, board):
        self.board = board
        # All queen directions
        self.directions = ((-1, -1), (-1, 1), (1, 1), (1, -1),
                           (-1, 0), (0, -1), (1, 0), (0, 1))

    # Get all the Queen moves for the Queen located at row, col
    def getMoves(self, r, c, moves, whiteToMove, Move):
        enemyColor = "b" if whiteToMove else "w"
        for d in self.directions:
            for i in range(1, 8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # Pieces on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':
                        moves.append(
                            Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(
                            Move((r, c), (endRow, endCol), self.board))
                        break
                    else:  # Friendly piece invalid
                        break
                else:  # Out of board
                    break


class King():
    def __init__(self, board):
        self.board = board
        # All King directions
        self.directions = ((-1, -1), (-1, 1), (1, 1), (1, -1),
                           (-1, 0), (0, -1), (1, 0), (0, 1))

    # Get all the King moves for the King located at row, col
    def getMoves(self, r, c, moves, whiteToMove, Move):
        enemyColor = "b" if whiteToMove else "w"
        for d in self.directions:
            endRow = r + d[0]
            endCol = c + d[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:  # Pieces on board
                endPiece = self.board[endRow][endCol]
                if endPiece == '--':
                    moves.append(
                        Move((r, c), (endRow, endCol), self.board))
                elif endPiece[0] == enemyColor:
                    moves.append(
                        Move((r, c), (endRow, endCol), self.board))


class Knight():
    def __init__(self, board):
        self.board = board
        # All Knight directions
        self.directions = ((-2, -1), (-2, 1), (2, 1), (2, -1),
                           (-1, -2), (-1, 2), (1, -2), (1, 2))

    # Get all the Knight moves for the Knight located at row, col
    def getMoves(self, r, c, moves, whiteToMove, Move):
        enemyColor = "b" if whiteToMove else "w"
        for d in self.directions:
            endRow = r + d[0]
            endCol = c + d[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:  # Pieces on board
                endPiece = self.board[endRow][endCol]
                if endPiece == '--':
                    moves.append(
                        Move((r, c), (endRow, endCol), self.board))
                elif endPiece[0] == enemyColor:
                    moves.append(
                        Move((r, c), (endRow, endCol), self.board))
