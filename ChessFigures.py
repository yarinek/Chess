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
        if whiteToMove == 0:
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
        return moves
