import ChessEngine
import unittest
import TChessHelper

class TestMovesPawn(unittest.TestCase):

        def test_moves_wRook(self):
                helper = TChessHelper.TestChessHelper()
                piece= helper.test_move(4, 4, 4, 1, "wR")
                piece_2 = helper.test_move(4, 4, 1, 4, "wR")
                piece_3 = helper.test_move(4, 4, 4, 7, "wR")
                piece_4 = helper.test_move(4, 4, 7, 4, "wR")
                self.assertEqual(piece, "wR")
                self.assertEqual(piece_2, "wR")
                self.assertEqual(piece_3, "wR")
                self.assertEqual(piece_4, "wR")
                
        def test_moves_bRook(self):
                helper = TChessHelper.TestChessHelper()
                piece= helper.test_move(4, 4, 4, 1, "bR")
                piece_2 = helper.test_move(4, 4, 1, 4, "bR")
                piece_3 = helper.test_move(4, 4, 4, 7, "bR")
                self.assertEqual(piece, "bR")
                self.assertEqual(piece_2, "bR")
                self.assertEqual(piece_3, "bR")
                
if __name__ == '__main__':
        unittest.main()
		
