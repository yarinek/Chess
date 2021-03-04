import ChessEngine

class TestChessHelper():
    
    @staticmethod 
    def test_move(PosY, PosX, DestPosY, DestPosX, figure ):
        game_state = ChessEngine.GameState()
        game_state.clearBoard()
        game_state.set_figure_in_position(PosY, PosX, figure)
        move = ChessEngine.Move([PosY, PosX], [DestPosX, DestPosY], game_state.board)
        game_state.make_move(move)
        piece = game_state.board[DestPosX][DestPosY]
        return piece