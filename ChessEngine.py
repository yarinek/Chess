# Storing all information about state of game

class GameState():
    def __init__(self):
        # Board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

    def make_move(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)  # log the move
        self.whiteToMove = not self.whiteToMove  # swap players

    # Undo last move

    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove  # switch turn back

    # All moves considering checks
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    # All moves without considering checks
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pieceColor = self.board[r][c][0]
                if (pieceColor == 'w' and self.whiteToMove) or (pieceColor == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
                    elif piece == 'N':
                        self.getKnightMoves(r, c, moves)
                    elif piece == 'B':
                        self.getBishopMoves(r, c, moves)
                    elif piece == 'Q':
                        self.getQueenMoves(r, c, moves)
                    elif piece == 'K':
                        self.getKingMoves(r, c, moves)
        return moves

    # Get all the pawn moves for the pawn located at row, col
    def getPawnMoves(self, r, c, moves):
        # Moves for white pieces
        if self.whiteToMove:
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
        if self.whiteToMove == 0:
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
    # Get all the rook moves for the rook located at row, col

    def getRookMoves(self, r, c, moves):
        pass
    # Get all the knight moves for the knight located at row, col

    def getKnightMoves(self, r, c, moves):
        pass
    # Get all the bishop moves for the bishop located at row, col

    def getBishopMoves(self, r, c, moves):
        pass
    # Get all the queen moves for the queen located at row, col

    def getQueenMoves(self, r, c, moves):
        pass
    # Get all the king moves for the king located at row, col

    def getKingMoves(self, r, c, moves):
        pass


class Move():
    # map keys to values
    # key:value
    ranks_to_rows = {"1": 7, "2": 6, "3": 5,
                     "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}

    files_to_cols = {"h": 7, "g": 6, "f": 5,
                     "e": 4, "d": 3, "c": 2, "b": 1, "a": 0}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

        self.moveID = self.startRow * 1000 + self.startCol * \
            100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    # overriding the equals method
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c]+self.rows_to_ranks[r]
