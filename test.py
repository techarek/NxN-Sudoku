from Sudoku import Sudoku
import unittest


class TestSudokuSolver1x1(unittest.TestCase):
    """
    Testing Strategy:
    Partition on fill of puzzle: Empty,  full
    """
    def test_valid_empty(self):
        """ Empty valid 1x1 Sudoku with one solution """
        s = Sudoku([[0]])
        s.solve()
        self.assertTrue(s.solved())

    def test_valid_full(self):
        """ Full valid 9x9 Sudoku with one solution """
        s = Sudoku([[1]])
        s.solve()
        self.assertTrue(s.solved())


class TestSudokuSolver4x4(unittest.TestCase):
    """
    Testing Strategy:
    Partition on validity of puzzle: Valid, invalid row, invalid column, invalid block
    Partition on fill of puzzle: Empty, partially filled, full
    """
    def test_valid_partial(self):
        """ Valid partially filled 4x4 Sudoku """
        s = Sudoku([[3, 0, 0, 0], [4, 0, 3, 1], [1, 0, 4, 0], [0, 0, 1, 0]])
        s.solve()
        self.assertTrue(s.solved())

    def test_valid_empty(self):
        """ Valid empty 4x4 Sudoku """
        s = Sudoku([[0]*4]*4)
        s.solve()
        self.assertTrue(s.solved())

    def test_valid_full(self):
        """ Valid full 4x4 Sudoku """
        s = Sudoku([[4, 1, 3, 2], [2, 3, 1, 4], [1, 4, 2, 3], [3, 2, 4, 1]])
        s.solve()
        self.assertTrue(s.solved())

    def test_invalid_row(self):
        """ Invalid row """
        s = Sudoku([[4, 3, 2, 1], [0, 2, 0, 0], [0, 0, 0, 4], [2, 4, 1, 2]])
        s.solve()
        self.assertFalse(s.solved())

    def test_invalid_column(self):
        """ Invalid column """
        s = Sudoku([[4, 3, 2, 1], [0, 2, 0, 0], [0, 0, 0, 4], [3, 2, 1, 2]])
        s.solve()
        self.assertFalse(s.solved())

    def test_invalid_block(self):
        """ Invalid block """
        s = Sudoku([[2, 3, 0, 1], [0, 2, 0, 0], [0, 0, 0, 4], [3, 2, 1, 2]])
        s.solve()
        self.assertFalse(s.solved())

    def test_invalid_full(self):
        """ All invalid """
        s = Sudoku([[1]*4]*4)
        s.solve()
        self.assertFalse(s.solved())


class TestSudokuSolver9x9(unittest.TestCase):
    """
    Testing Strategy:
    Partition on validity of puzzle: Valid, invalid row, invalid column, invalid block
    Partition on fill of puzzle: Empty, partially filled, full
    """
    def test_valid_partial(self):
        """ Valid partially filled 9x9 Sudoku """
        s = Sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]])
        s.solve()
        self.assertTrue(s.solved())

    def test_valid_empty(self):
        """ Valid empty 9x9 Sudoku """
        s = Sudoku([[0]*9]*9)
        s.solve()
        self.assertTrue(s.solved())

    def test_valid_full(self):
        """ Valid filled 9x9 Sudoku """
        s = Sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]])
        s.solve()
        self.assertTrue(s.solved())

    def test_invalid_row(self):
        """ Invalid 9x9 Sudoku by row"""
        s = Sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 8, 7, 9]])
        s.solve()
        self.assertFalse(s.solved())

    def test_invalid_column(self):
        """ Invalid 9x9 Sudoku by column"""
        s = Sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 2, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]])
        s.solve()
        self.assertFalse(s.solved())

    def test_invalid_block(self):
        """ Invalid 9x9 Sudoku by block"""
        s = Sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 9, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]])
        s.solve()
        self.assertFalse(s.solved())

    def test_invalid_full(self):
        """ Invalid 9x9 Sudoku"""
        s = Sudoku([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        s.solve()
        self.assertFalse(s.solved())


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
