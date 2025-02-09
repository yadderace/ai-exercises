import random
import copy

DEFAULT_DEPTH = 4

class AI:
    def __init__(self, game):
        self.game = game

    def get_random_move(self):
        """
        Returns a random valid column to play in the Connect 4 game.

        This method generates a list of columns where a move is valid and then
        randomly selects one of these columns. If no valid columns are available,
        it returns None.

        Returns:
            int or None: A randomly selected valid column index (0-6) or None if no valid moves are available.
        """
        """Devuelve una columna aleatoria donde sea válido jugar."""
        valid_columns = [col for col in range(7) if self.game.is_valid_move(col)]
        return random.choice(valid_columns) if valid_columns else None
    
    def simulate_move(self, board, col, player):
        """
        Simulates a move in the Connect 4 game by placing a player's piece in the specified column.
        Args:
            board (list of list of int): The current game board represented as a 2D list.
            col (int): The column index where the player wants to place their piece.
            player (int): The player number (typically 1 or 2) making the move.
        Returns:
            list of list of int: A new game board with the player's piece placed in the specified column.
            None: If the column is full and no move can be made.
        """
        
        new_board = copy.deepcopy(board)  # Create a deep copy to avoid modifying the original
        for row in range(self.game.ROWS - 1, -1, -1):  # Start from the bottom row
            if new_board[row][col] == self.game.EMPTY_VALUE:  # Find the first available row in the column
                new_board[row][col] = player 
                return new_board 
        return None 

    def score_position(self, piece_list):
        """
        Scores a given set of 4 pieces based on their composition.

        This function evaluates a list of 4 pieces from the Connect 4 board and 
        assigns a score based on the number of AI pieces, opponent pieces, and empty spaces.

        Args:
            piece_list (list): A list of 4 elements representing pieces on the board. 
                               Each element can be an AI piece, opponent piece, or empty space.

        Returns:
            int: The score for the given set of pieces. Positive scores favor the AI, 
                 while negative scores indicate a threat from the opponent.
        """
        """Scores a given set of 4 pieces."""
        score = 0
        piece_count = piece_list.count(self.game.AI_VALUE)
        opponent_count = piece_list.count(self.game.HUMAN_VALUE)
        empty_count = piece_list.count(self.game.EMPTY_VALUE)

        if piece_count == 4:  # AI wins in this section
            score += 1000
        elif piece_count == 3 and empty_count == 1:  # 3 in a row
            score += 50
        elif piece_count == 2 and empty_count == 2:  # 2 in a row
            score += 10

        if opponent_count == 3 and empty_count == 1:  # Opponent close to winning
            score -= 80  # Strong penalty to block it

        return score

    def evaluate_board(self, board):
        """
        Evaluates the board and returns a score based on AI advantage.
        The function checks for winning conditions for both the AI and the human player.
        If the AI wins, it returns a high positive score. If the human player wins, it returns a high negative score.
        Otherwise, it evaluates the board by checking all possible horizontal, vertical, and diagonal lines of four positions
        and sums up their scores.
        Args:
            board (list of list of int): The current state of the game board.
        Returns:
            int: The score representing the AI's advantage on the board.
        """
        
        """Evaluates the board and returns a score based on AI advantage."""
        if self.game.check_winner(self.game.AI_VALUE, board):  # AI wins
            return 100000
        if self.game.check_winner(self.game.HUMAN_VALUE, board):  # Opponent wins
            return -100000

        score = 0

        # Evaluate Horizontal, Vertical, and Diagonal
        for row in range(self.game.ROWS):
            for col in range(self.game.COLS - 3):
                score += self.score_position([board[row][col + i] for i in range(4)])

        for row in range(self.game.ROWS - 3):
            for col in range(self.game.COLS):
                score += self.score_position([board[row + i][col] for i in range(4)])

        for row in range(self.game.ROWS - 3):
            for col in range(self.game.COLS - 3):
                score += self.score_position([board[row + i][col + i] for i in range(4)])

        for row in range(3, self.game.ROWS):
            for col in range(self.game.COLS - 3):
                score += self.score_position([board[row - i][col + i] for i in range(4)])

        return score
    
    def minimax(self, board, depth, maximizing_player):
        """
        Implements the minimax algorithm with alpha-beta pruning to determine the best move for the AI.
        The function recursively evaluates all possible moves up to a certain depth and returns the best move
        based on the evaluation score.
        Args:
            board (list of list of int): The current state of the game board.
            depth (int): The depth of the search tree to explore.
            maximizing_player (bool): A boolean flag indicating whether the current player is maximizing (AI) or not.
        Returns:
            dict: A dictionary containing the best move and the decision tree of the search.
        """

        if depth == 0 or self.game.check_winner(self.game.HUMAN_VALUE, board) or self.game.check_winner(self.game.AI_VALUE, board):
            score = self.evaluate_board(board)
            return {
                "move": None,
                "score": score,
                "min": score,
                "max": score,
                "children": []
            }
        
        valid_moves = [col for col in range(7) if self.game.is_valid_move(col, board)]
        
        best_move = None
        children = []  
        min_value = float('inf')
        max_value = float('-inf')

        if maximizing_player:
            max_eval = float('-inf')
            for col in valid_moves:
                new_board = self.simulate_move(copy.deepcopy(board), col, self.game.AI_VALUE)  # AI move
                child_node = self.minimax(new_board, depth - 1, False)
                children.append(child_node)

                if child_node["score"] > max_eval:
                    max_eval = child_node["score"]
                    best_move = col
                
                max_value = max(max_value, child_node["max"])
                min_value = min(min_value, child_node["min"])

            return {
                "move": best_move,
                "score": max_eval,
                "min": min_value,
                "max": max_value,
                "children": children
            }

        else:
            min_eval = float('inf')
            for col in valid_moves:
                new_board = self.simulate_move(copy.deepcopy(board), col, self.game.HUMAN_VALUE)  # Human move
                child_node = self.minimax(new_board, depth - 1, True)
                children.append(child_node)

                if child_node["score"] < min_eval:
                    min_eval = child_node["score"]
                    best_move = col
                
                max_value = max(max_value, child_node["max"])
                min_value = min(min_value, child_node["min"])

            return {
                "move": best_move,
                "score": min_eval,
                "min": min_value,
                "max": max_value,
                "children": children
            }

    def get_minmax_best_move(self):
        """Returns the best move and the decision tree as JSON."""
        decision_tree = self.minimax(self.game.board, DEFAULT_DEPTH , True)
        return decision_tree["move"], decision_tree
