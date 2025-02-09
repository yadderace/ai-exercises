import numpy as np

# Define the dimensions of the board
ROWS = 6
COLS = 7
HUMAN_VALUE = 1
AI_VALUE = 2
EMPTY_VALUE = 0

class Connect4:
    def __init__(self):
        """Initializes the board with zeros (empty)."""
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.ROWS = ROWS
        self.COLS = COLS
        self.HUMAN_VALUE = HUMAN_VALUE
        self.AI_VALUE = AI_VALUE
        self.EMPTY_VALUE = EMPTY_VALUE

    def is_valid_move(self, col, board = None):
        """Checks if a column has available space."""
        if board is None:
            board = self.board
        
        return board[0][col] == 0

    def drop_piece(self, col, player):
        """Places the piece in the column selected by the player or AI."""
        for row in range(ROWS - 1, -1, -1):  # From bottom to top
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return row  # Returns the row where the piece was placed

    def check_winner(self, player, board = None):
        """
        Check if the given player has won the game.
        This function checks the board for a winning condition for the specified player.
        A player wins if they have four of their pieces in a row horizontally, vertically,
        or diagonally.
        Args:
            player (int): The player number to check for a win (typically 1 or 2).
            board (list of list of int, optional): The game board to check. If not provided,
                the current game board (`self.board`) will be used.
        Returns:
            bool: True if the player has won, False otherwise.
        """
        
        if board is None:
            board = self.board

        # Horizontal check
        for row in range(ROWS):
            for col in range(COLS - 3):
                print(f"board[{row}, {col}]")
                if all(board[row, col + i] == player for i in range(4)):
                    return True

        # Vertical check
        for row in range(ROWS - 3):
            for col in range(COLS):
                if all(board[row + i, col] == player for i in range(4)):
                    return True

        # Diagonal check (\)
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(board[row + i, col + i] == player for i in range(4)):
                    return True

        # Diagonal check (/)
        for row in range(ROWS - 3):
            for col in range(3, COLS):
                if all(board[row + i, col - i] == player for i in range(4)):
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

