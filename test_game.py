from game import Connect4

# Crear una nueva partida
game = Connect4()

# Simular movimientos
game.drop_piece(1, 1)
game.drop_piece(3, 2)
game.drop_piece(3, 1)
game.drop_piece(2, 2)
game.drop_piece(3, 1)
game.drop_piece(3, 2)

# Imprimir el tablero
game.print_board()
