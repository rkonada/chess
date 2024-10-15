import pygame
from piece import Piece
from utils import scale_image_uneven


#variables

# turns files into numbers


class Board:
    def __init__(self, pos, img_file, x_factor, y_factor, white_pieces, black_pieces):
        self.img: pygame.Surface = scale_image_uneven(pygame.image.load(img_file), x_factor,
                                y_factor)
        self.mask: pygame.Mask = pygame.mask.from_surface(self.img)
        self.pos: tuple[int, int] = pos
        self.x_pos, self.y_pos = pos
        self.board =    [
                ["", "", "", "", "", "", "", ""], 
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""]
        ]
        self.board_pieces = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]

        self.white_pieces = white_pieces
        for white_piece in white_pieces:
            self.board[8 - white_piece.rank][white_piece.file_num - 1] = white_piece.piece + " white"
            self.board_pieces[8 - white_piece.rank][white_piece.file_num - 1] = white_piece

        self.black_pieces = black_pieces
        for black_piece in black_pieces:
            self.board[8 - black_piece.rank][black_piece.file_num - 1] = black_piece.piece + " black"
            self.board_pieces[8 - black_piece.rank][black_piece.file_num - 1] = black_piece

        self.pieces = white_pieces + black_pieces



    def change_board(self, piece: Piece, piece_file_num: int, piece_rank: int, mouse_file_num: int, mouse_rank: int) -> None:
        self.board[8 - piece_rank][piece_file_num - 1] = ""
        self.board[8 - mouse_rank][mouse_file_num - 1] = piece.piece + " " + piece.color

        self.board_pieces[8 - piece_rank][piece_file_num - 1] = None
        self.board_pieces[8 - mouse_rank][mouse_file_num - 1] = piece # type: ignore

        for loop_piece in self.pieces:
            loop_piece.get_legal_moves(self)

        self.change_turn(piece)

    def change_turn(self, piece: Piece):
        if piece.color == "white":
            for black_piece in self.black_pieces: black_piece.turn = True
            for white_piece in self.white_pieces: white_piece.turn = False
        elif piece.color == "black":
            for black_piece in self.black_pieces: black_piece.turn = False
            for white_piece in self.white_pieces: white_piece.turn = True




    

