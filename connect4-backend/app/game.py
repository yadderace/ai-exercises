import numpy as np

# Define the dimensions of the board
ROWS = 6
COLS = 7

class Connect4:
    def __init__(self):
        """Initializes the board with zeros (empty)."""
        self.board = np.zeros((ROWS, COLS), dtype=int)

    def is_valid_move(self, col):
        """Checks if a column has available space."""
        return self.board[0][col] == 0

    def drop_piece(self, col, player):
        """Places the piece in the column selected by the player or AI."""
        for row in range(ROWS - 1, -1, -1):  # From bottom to top
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return row  # Returns the row where the piece was placed

    def check_winner(self, player):
        """Checks if the player has won the game."""

        # Horizontal check
        for row in range(ROWS):
            for col in range(COLS - 3):
                if all(self.board[row, col + i] == player for i in range(4)):
                    return True

        # Vertical check
        for row in range(ROWS - 3):
            for col in range(COLS):
                if all(self.board[row + i, col] == player for i in range(4)):
                    return True

        # Diagonal check (\)
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(self.board[row + i, col + i] == player for i in range(4)):
                    return True

        # Diagonal check (/)
        for row in range(ROWS - 3):
            for col in range(3, COLS):
                if all(self.board[row + i, col - i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        """Checks if the board is completely full."""
        return not any(self.is_valid_move(col) for col in range(COLS))

    def reset_board(self):
        """Resets the board for a new game."""
        self.board = np.zeros((ROWS, COLS), dtype=int)

    def print_board(self):
        """Prints the board to the console (for testing)."""
        print(self.board)  # Flips the board so that row 0 is at the bottom

