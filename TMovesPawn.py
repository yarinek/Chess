import ChessEngine
import unittest
import TChessHelper

class TestMovesPawn(unittest.TestCase):

        def test_moves_wPawn(self):
                helper = TChessHelper.TestChessHelper()
                piece_wp = helper.test_move(6, 1, 5, 1, "wp")
                piece_wp2 = helper.test_move(6, 2, 4, 2, "wp")
                piece_wp3 = helper.test_move(4, 2, 3,2,"wp")
                self.assertEqual(piece_wp, "wp")
                self.assertEqual(piece_wp2, "wp")
                self.assertEqual(piece_wp3, "wp")
                
        def test_moves_bPawn(self):
                helper = TChessHelper.TestChessHelper()
                piece_bp = helper.test_move(1, 1, 2, 1,"bp")
                piece_bp2 = helper.test_move(1, 2, 3, 2,"bp")
                piece_bp3 = helper.test_move(3, 2, 4,2,"bp")
                self.assertEqual(piece_bp, "bp")
                self.assertEqual(piece_bp2, "bp")
                self.assertEqual(piece_bp3, "bp")
                
if __name__ == '__main__':
        unittest.main()
		
