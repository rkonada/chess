from piece import WhitePiece, BlackPiece

class WhitePawn(WhitePiece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)

    def get_legal_moves(self, board):
        self.legal_moves = []
        if self.is_legal(self.file_num, self.rank + 1, board):
            self.legal_moves.append([self.file, self.rank + 1])
            if self.first and self.is_legal(self.file_num, self.rank + 2, board):
                self.legal_moves.append([self.file, self.rank + 2])

class BlackPawn(BlackPiece):
    def __init__(self, file_load: str, file, rank, piece: str, pieces, piece_scale):
        super().__init__(file_load, file, rank, piece, pieces, piece_scale)

    def get_legal_moves(self, board):
        self.legal_moves = []
        if self.is_legal(self.file_num, self.rank - 1, board):
            self.legal_moves.append([self.file, self.rank - 1])
            if self.first and self.is_legal(self.file_num, self.rank - 2, board):
                self.legal_moves.append([self.file, self.rank - 2])