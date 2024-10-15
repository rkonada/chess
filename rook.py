from piece import WhitePiece, BlackPiece
from utils import int_to_file

class WhiteRook(WhitePiece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)

    def get_legal_moves(self, board):
        self.legal_moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for df, dr in directions:
            file_num, rank = self.file_num, self.rank
            while 1 <= file_num + df <= 8 and 1 <= rank + dr <= 8 and self.is_legal(file_num + df, rank + dr, board):
                file_num += df
                rank += dr
                self.legal_moves.append([int_to_file[file_num], rank + dr])
                if self.is_other_color(file_num, rank, board):
                    break

class BlackRook(BlackPiece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)

    def get_legal_moves(self, board):
        self.legal_moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for df, dr in directions:
            file_num, rank = self.file_num, self.rank
            while 1 <= file_num + df <= 8 and 1 <= rank + dr <= 8 and self.is_legal(file_num, rank, board):
                file_num += df
                rank += dr
                self.legal_moves.append([int_to_file[file_num], rank])
                if self.is_other_color(file_num, rank, board):
                    break