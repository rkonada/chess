import pygame

from utils import scale_image_even, scale_image_uneven, file_to_int, file_change, rank_change


class Piece:
    def __init__(self, img_file: str, file: str, rank: int, piece:str, pieces: list, piece_scale: float):
        self.img: pygame.Surface = scale_image_even(pygame.image.load(img_file), piece_scale)
        self.img_mask: pygame.mask = pygame.mask.from_surface(self.img)
        self.rank: int = rank
        self.file: str = file
        self.file_num: int = file_to_int[file]
        self.x_pos: int = 0
        self.y_pos: int = 0
        self.pos: tuple[int, int] = (0, 0)
        self.find_pos()
        self.legal_moves: list[list[str, int]] = []
        self.legal_moves_pos: list[list[int, int]] = []
        self.piece: str = piece
        self.clicked: bool = False
        self.color: str = ""
        self.first: bool = True # only needed for pawns
        pieces.append(self) # add to list of all pieces

    def find_pos(self):
        self.x_pos = 267 + self.file_num * 75
        self.y_pos = 590 - (self.rank - 1) * 75
        self.pos = (self.x_pos, self.y_pos)

    def is_hovered(self, mouse_pos) -> bool:
        mouse_x_pos, mouse_y_pos = mouse_pos
        if ((self.x_pos <= mouse_x_pos <= self.x_pos + self.img.get_width()) and self.y_pos <= mouse_y_pos <=
                self.y_pos + self.img.get_height()):
            return True
        return False





    def __repr__(self) -> str:
        return "This " + self.color + " " + self.piece + " is at " + self.file.upper() + str(self.rank) + "."

    def get_legal_moves(self, board) -> None:
        ...


    def is_legal(self, file_num, rank, board) -> bool:
        piece_at_loc: str = board.board[8 - rank][file_num - 1]
        return piece_at_loc == "" or self.color not in piece_at_loc

    def is_other_color(self, file_num, rank, board):
        piece_at_loc: str = board.board[8 - rank][file_num - 1]
        return self.color not in piece_at_loc and piece_at_loc != ""



    def draw_legal_moves(self, win, img_file, board) -> None:
        self.get_legal_moves(board)

        for file, rank in self.legal_moves:
            self.legal_moves_pos.append([file_change(file_to_int[file]), rank_change(rank)])

        for legal_move in self.legal_moves:
            legal_move_x_pos: int = 287 + file_to_int[legal_move[0]] * 75
            legal_move_y_pos: int = 610 - (legal_move[1] - 1) * 75
            legal_move_pos: tuple[int, int] = legal_move_x_pos, legal_move_y_pos
            legal_move_img: pygame.Surface = scale_image_uneven(pygame.image.load(img_file), 0.207, 0.213)

            win.blit(legal_move_img, legal_move_pos)

    def move(self, file, rank, board) -> None:
        if self.is_other_color(file_to_int[file], rank, board):
            ...
        self.file = file
        self.file_num = file_to_int[file]
        self.rank = rank
        self.find_pos()
        if self.piece == "pawn":
            self.first = False

    def take_piece(self):
        ...


# colors

class WhitePiece(Piece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)
        self.color = "white"
        self.turn = True

class BlackPiece(Piece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)
        self.color = "black"
        self.turn = False


        
