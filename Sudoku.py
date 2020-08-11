import math
import numpy as np


class Sudoku:
    """
    An abstract data type for an nxn Sudoku puzzle

    Abstraction function(self.board, self.board_size, self.block_size) = A self.board_size by self.board_size Sudoku
        grid where self.board[i, j] is the number written in the ith row and the jth column of the board,
        if self.board[i, j] == 0, then that square in the grid is empty.
    Representation Invariant: All numbers in self.board must be between 0 and self.board_size inclusive,
        self.board_size is a perfect square, self.board is a square array
    """

    def __init__(self, board: list):
        """
        Instantiates a new Sudoku object

        :param board: A 2 dimensional list of numbers between 0 and the length of board inclusive
        """
        # numpy array was chosen as the representation because it can be used to slice into both dimensions of 2D lists
        self.board = np.array(board)
        self.block_size = int(math.sqrt(len(board)))
        self.board_size = self.block_size**2
        self._check_rep()

    def _check_rep(self):
        """
        Asserts the representation invariant
        """
        assert 0 <= self.board.all() <= self.board_size
        # Checks that the board size is a perfect square
        assert any([self.board_size == i**2 for i in range(self.block_size + 1)])
        assert self.board.shape[0] == self.board.shape[1]

    def get_next_empty_cell(self):
        """
        Find the next empty square in the Sudoku grid following a row-first traversal pattern

        :return: tuple of the next empty coordinates in the form (row, column)
        """
        # This process could be cached for better performance(because to solve a puzzle, no square is found empty twice)
        # This would involve storing the last seen row, column pair and starting traversals at that square
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # 0 is falsey
                if not self.board[i][j]:
                    return i, j
        return -1, -1

    def fits(self, row: int, col: int, elem: int):
        """
        Checks whether an element can be placed into the Sudoku grid without breaking the rules

        :param row: int of the row to be checked
        :param col: int of the column to be checked
        :param elem: int of the element to be placed into row, col
        :return: boolean whether the element can be placed at row, col
        """
        # numpy allows direct indexing into columns and rows
        row_check = elem not in self.board[row]
        col_check = elem not in self.board[:, col]

        # Blocks in a sudoku grid are the block_size by block_size subgrids that begin at the closest lower and higher
        # multiples of self.block_size
        row_start = row//self.block_size*self.block_size
        row_end = (row+self.block_size)//self.block_size*self.block_size
        col_start = col//self.block_size*self.block_size
        col_end = (col+self.block_size)//self.block_size*self.block_size

        # numpy allows slicing of both the dimensions in a 2-dimensional array
        block_check = elem not in self.board[row_start:row_end, col_start:col_end]

        return row_check and col_check and block_check

    def solved(self):
        """
        Checks if the Sudoku puzzle is solved

        :return: Boolean whether this Sudoku puzzle is solved
        """
        # Generates a list of the block upper left corners' coordinates
        block_indices = [(i, j) for i in range(0, self.board_size, self.block_size) for j in range(0, self.board_size, self.block_size)]
        # For a row, column, and block to be valid, they must have one of each number 1 through self.board_size
        correct_set = set(range(1, self.board_size + 1))

        for i in range(len(self.board)):
            x, y = block_indices[i]
            block = set(self.board[x:x+self.block_size, y:y+self.block_size].flatten())
            # Checks that row, column, and block are valid
            if not set(self.board[i]) == set(self.board[:, i]) == block == correct_set:
                return False

        return True

    def solve(self):
        """
        Solves the Sudoku puzzle

        :return: numpy array of the solved board, None if puzzle could not be solved
        """
        def add_next_number():
            """
            Modifies self.board to insert a number into the next empty square
            Recursively fills the entire board, recursively backtracks on incorrect insertions

            :return: Boolean whether the next number was added successfully
            """
            x, y = self.get_next_empty_cell()
            if self.solved():
                return True
            elif x == -1:
                # If the puzzle is not solved but there are no empty squares, it is unsolvable
                return False

            for i in range(1, self.board_size + 1):
                if self.fits(x, y, i):
                    self.board[x, y] = i

                    # Recursively fills the board
                    if add_next_number():
                        return True
                    else:
                        # Backtracking step
                        self._remove(x, y)

            # Gets to this point if no numbers fit, and thus there is no solution
            return False

        solved_board = add_next_number()
        return self.board if solved_board else None

    def _remove(self, row: int, col: int):
        """
        Private method: Removes an element from the board

        :param row: int of the row of the element to be deleted
        :param col: int of the column of the element to be deleted
        """
        self.board[row, col] = 0

    def __str__(self):
        return str(self.board)

    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other):
        return isinstance(other, Sudoku) and other.board == self.board
