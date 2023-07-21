import chess
import os
import random


move = 0
board = chess.Board()
while True:
    os.system("cls")
    
    print(board)

    if board.is_checkmate():
        break

    moves = list(board.legal_moves)
    movida_negra = random.choice(moves)

    board.push_san(not move and input("Ingrese su movimiento (Blancas)") or str(movida_negra))

    move = not move and 1 or 0

print(board.is_checkmate())