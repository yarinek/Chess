import ChessEngine
import unittest

class TestChessHelper():
    
    @staticmethod 
    def test_move(PosY, PosX, DestPosY, DestPosX):
        game_state = ChessEngine.GameState()
        move = ChessEngine.Move([PosY, PosX], [DestPosX, DestPosY], game_state.board)
        game_state.make_move(move)
        piece = game_state.board[DestPosX][DestPosY]
        return piece


class TestEngine(unittest.TestCase):

        def test_moves_wPawn(self):
                helper = TestChessHelper()
                piece_wp = helper.test_move(6, 1, 5, 1)
                piece_wp2 = helper.test_move(6, 2, 4, 2)
                self.assertEqual(piece_wp, "wp")
                self.assertEqual(piece_wp2, "wp")
                
        def test_moves_bPawn(self):
                helper = TestChessHelper()
                piece_bp = helper.test_move(1, 1, 2, 1)
                piece_bp2 = helper.test_move(1, 2, 3, 2)
                self.assertEqual(piece_bp, "bp")
                self.assertEqual(piece_bp2, "bp")

                
if __name__ == '__main__':
        unittest.main()
		
