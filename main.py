from fastapi import FastAPI, HTTPException
from game import Connect4
from ai import AI

app = FastAPI()

# Inicializamos el juego y la IA
game = Connect4()
ai = AI(game)

@app.get("/play")
def play_move(player_move: int):
    """Permite que el jugador elija una columna para su movimiento."""
    
    # Verificar si la jugada del jugador es válida
    if not game.is_valid_move(player_move):
        raise HTTPException(status_code=400, detail="Movimiento inválido. Intenta con otra columna.")

    # Jugador 1 hace su movimiento
    game.drop_piece(player_move, 1)

    # Verificar si el jugador ganó
    if game.check_winner(1):
        game.print_board()
        return {"message": "¡Jugador 1 gana!", "board": game.board.tolist()}

    # La IA hace su movimiento aleatorio
    ai_move = ai.get_random_move()
    if ai_move is not None:
        game.drop_piece(ai_move, 2)

    # Verificar si la IA ganó
    if game.check_winner(2):
        game.print_board()
        return {"message": "¡La IA gana!", "board": game.board.tolist()}

    # Imprimir el tablero después de los movimientos
    game.print_board()

    return {"player_move": player_move, "ai_move": ai_move, "board": game.board.tolist()}


@app.get("/reset")
def reset_game():
    """Reinicia el juego (resetea el tablero)."""
    game.reset_board()
    return {"message": "Juego reiniciado", "board": game.board.tolist()}