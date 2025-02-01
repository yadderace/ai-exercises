import random


class AI:
    def __init__(self, game):
        self.game = game

    def get_random_move(self):
        """Devuelve una columna aleatoria donde sea válido jugar."""
        valid_columns = [col for col in range(7) if self.game.is_valid_move(col)]
        return random.choice(valid_columns) if valid_columns else None
