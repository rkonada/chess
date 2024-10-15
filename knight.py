from piece import WhitePiece, BlackPiece
from utils import int_to_file

class WhiteKnight(WhitePiece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)

    def get_legal_moves(self, board):
        self.legal_moves = []
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

        for df, dr in moves:
            file_num, rank = self.file_num, self.rank
            if 1 <= file_num + df <= 8 and 1 <= rank + dr <= 8 and self.is_legal(file_num + df, rank + dr, board):
                self.legal_moves.append([int_to_file[file_num + df], rank + dr])


class BlackKnight(BlackPiece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)

    def get_legal_moves(self, board):
        self.legal_moves = []
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

        for df, dr in moves:
            file_num, rank = self.file_num, self.rank
            if 1 <= file_num + df <= 8 and 1 <= rank + dr <= 8 and self.is_legal(file_num + df, rank + dr, board):
                self.legal_moves.append([int_to_file[file_num + df], rank + dr])