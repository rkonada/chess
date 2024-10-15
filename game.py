import pygame

pygame.init()

from piece import WhitePiece, BlackPiece
from pawn import WhitePawn, BlackPawn
from knight import WhiteKnight, BlackKnight
from bishop import WhiteBishop, BlackBishop
from rook import WhiteRook, BlackRook
from queen import WhiteQueen, BlackQueen
from king import WhiteKing, BlackKing

from board import Board
from utils import pos_to_cell, int_to_file


# variables

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

# pictures


# pieces
piece_scale: float = 1.15

white_pieces: list[WhitePiece] = []
black_pieces: list[BlackPiece] = []

# WHITE

WHITE_PAWN_1 = WhitePawn("chess files/wp.png", "a", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_2 = WhitePawn("chess files/wp.png", "b", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_3 = WhitePawn("chess files/wp.png", "c", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_4 = WhitePawn("chess files/wp.png", "d", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_5 = WhitePawn("chess files/wp.png", "e", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_6 = WhitePawn("chess files/wp.png", "f", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_7 = WhitePawn("chess files/wp.png", "g", 2, "pawn", white_pieces, piece_scale)
WHITE_PAWN_8 = WhitePawn("chess files/wp.png", "h", 2, "pawn", white_pieces, piece_scale)
WHITE_BISHOP_DARK = WhiteBishop("chess files/wB.png", "c", 1, "bishop", white_pieces, piece_scale)
WHITE_BISHOP_LIGHT = WhiteBishop("chess files/wB.png", "f", 1, "bishop", white_pieces, piece_scale)
WHITE_KNIGHT_1 = WhiteKnight("chess files/wN.png", "g", 1, "knight", white_pieces, piece_scale)
WHITE_KNIGHT_2 = WhiteKnight("chess files/wN.png", "b", 1, "knight", white_pieces, piece_scale)
WHITE_ROOK_1 = WhiteRook("chess files/wR.png", "a", 1, "rook", white_pieces, piece_scale)
WHITE_ROOK_2 = WhiteRook("chess files/wR.png", "h", 1, "rook", white_pieces, piece_scale)
WHITE_QUEEN = WhiteQueen("chess files/wQ.png", "d", 1, "queen", white_pieces, piece_scale)
WHITE_KING = WhiteKing("chess files/wK.png", "e", 1, "king", white_pieces, piece_scale)




#BLACK

BLACK_PAWN_1 = BlackPawn("chess files/bp.png", "a", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_2 = BlackPawn("chess files/bp.png", "b", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_3 = BlackPawn("chess files/bp.png", "c", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_4 = BlackPawn("chess files/bp.png", "d", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_5 = BlackPawn("chess files/bp.png", "e", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_6 = BlackPawn("chess files/bp.png", "f", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_7 = BlackPawn("chess files/bp.png", "g", 7, "pawn", black_pieces, piece_scale)
BLACK_PAWN_8 = BlackPawn("chess files/bp.png", "h", 7, "pawn", black_pieces, piece_scale)
BLACK_BISHOP_DARK = BlackBishop("chess files/bB.png", "c", 8, "bishop", black_pieces, piece_scale)
BLACK_BISHOP_LIGHT = BlackBishop("chess files/bB.png", "f", 8, "bishop", black_pieces, piece_scale)
BLACK_KNIGHT_1 = BlackKnight("chess files/bN.png", "g", 8, "knight", black_pieces, piece_scale)
BLACK_KNIGHT_2 = BlackKnight("chess files/bN.png", "b", 8, "knight", black_pieces, piece_scale)
BLACK_ROOK_1 = BlackRook("chess files/bR.png", "h", 8, "rook", black_pieces, piece_scale)
BLACK_ROOK_2 = BlackRook("chess files/bR.png", "a", 8, "rook", black_pieces, piece_scale)
BLACK_QUEEN = BlackQueen("chess files/bQ.png", "d", 8, "queen", black_pieces, piece_scale)
BLACK_KING = BlackKing("chess files/bK.png", "e", 8, "king", black_pieces, piece_scale)



pieces = white_pieces + black_pieces

# to make it 600 by 600
chess_board_width_x_factor: float = 1.999 * 1.3345
chess_board_width_y_factor: float = 2.007 * 1.3345

CHESS_BOARD = Board((340, 60), "chess files/chess board.png", chess_board_width_y_factor, chess_board_width_y_factor, white_pieces,
                    black_pieces)





# methods

def not_legal_move():
    print("not legal move") # have to figure out what to do

# all images needed to blit
images: list[pygame.Surface, (int, int)] = []


def draw() -> None:

    screen.blit(CHESS_BOARD.img, CHESS_BOARD.pos)

    # for normal images
    for img, pos in images:
        screen.blit(img, pos)

    # for all the pieces

    for piece in pieces:
        screen.blit(piece.img, piece.pos)
        if piece.clicked and piece.turn:
            piece.draw_legal_moves(screen, "chess files/legal move.png", CHESS_BOARD)


    pygame.display.update()


# game loop

def main():
    game = True
    while game:
        draw()

        for event in pygame.event.get():
            # show legal moves
            for piece in pieces:
                if piece.is_hovered(pygame.mouse.get_pos()) and piece.turn:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        piece.clicked = not piece.clicked
                        for piece_2 in pieces:
                            if piece_2.clicked and piece != piece_2:
                                piece_2.clicked = False

                # check for if user clicks a legal move
                if piece.clicked and piece.turn:
                    mouse_pos = x_pos, y_pos = pygame.mouse.get_pos()
                    if 340 < x_pos < 940 and 60 < y_pos < 660:
                        mouse_pos_cell = mouse_file_num, mouse_rank = pos_to_cell(mouse_pos)

                        mouse_file = int_to_file[mouse_file_num]
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if [mouse_file, mouse_rank] in piece.legal_moves:
                                piece_old_file_num, piece_old_rank = piece.file_num, piece.rank
                                piece.move(mouse_file, mouse_rank, CHESS_BOARD)
                                CHESS_BOARD.change_board(piece, piece_old_file_num, piece_old_rank, *mouse_pos_cell)
                                piece.clicked = False
                            else:
                                not_legal_move()




            if event.type == pygame.QUIT:
                game = False

        clock.tick(60)

    pygame.quit()






