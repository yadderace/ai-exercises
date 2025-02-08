from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.game import Connect4
from app.ai import AI

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Inicializamos el juego y la IA
game = Connect4()
ai = AI(game)

@app.get("/play")
def play_move(player_col: int):
    """Permite que el jugador elija una columna para su movimiento."""
    
    # Verificar si la jugada del jugador es válida
    if not game.is_valid_move(player_col):
        raise HTTPException(status_code=400, detail="Movimiento inválido. Intenta con otra columna.")

    # Jugador 1 hace su movimiento
    player_row = game.drop_piece(player_col, 1)

    # Verificar si el jugador ganó
    if game.check_winner(1):
        game.print_board()
        return {"winner": 1,  "player_last_move": { "row": player_row , "col": player_col }, "ai_last_move": None }

    # La IA hace su movimiento aleatorio
    ai_col = ai.get_random_move()
    ai_row = -1
    if ai_col is not None:
        ai_row = game.drop_piece(ai_col, 2)

    # Verificar si la IA ganó
    if game.check_winner(2):
        game.print_board()
        return {"winner": 2,  "player_last_move": { "row": player_row , "col": player_col }, "ai_last_move": { "row": ai_row, "col": ai_col } }

    # Imprimir el tablero después de los movimientos
    print(f"Player Move ({play_move, player_row})")
    game.print_board()

    return {"winner": None,  "player_last_move": { "row": player_row , "col": player_col }, "ai_last_move": { "row": ai_row, "col": ai_col } }


@app.get("/reset")
def reset_game():
    """Reinicia el juego (resetea el tablero)."""
    game.reset_board()
    return {}