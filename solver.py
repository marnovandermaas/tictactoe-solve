from __future__ import annotations

from enum import Enum

Team = Enum('Team', ['X', 'O', 'E'])

class Piece:
    def __init__(self, team: Team):
        self.team = team
    def __str__(self) -> str:
        return self.team.name

class Board:
    def __init__(self, dimension: int = 3, on_move: Team = Team.X):
        self.pieces: list[list[Piece]] = []
        for row in range(dimension):
            tmp_row: list[Piece] = []
            for column in range(dimension):
                tmp_row.append(Piece(Team.E))
            self.pieces.append(tmp_row)
        for column in range(dimension):
            tmp_col: list[Piece] = []
            for idx in range(dimension):
                tmp_col.append(self.pieces[idx][column])
            self.pieces.append(tmp_col)
        diag0: list[Piece] = []
        diag1: list[Piece] = []
        for idx in range(dimension):
            diag0.append(self.pieces[idx][idx])
            diag1.append(self.pieces[idx][dimension-1-idx])
        self.pieces.append(diag0)
        self.pieces.append(diag1)
        self.dimension: int = dimension
        self.on_move: Team = on_move
    def __str__(self) -> str:
        mystring: str = '-' * (self.dimension + 2)
        mystring += '\n'
        for row in self.pieces:
            mystring += '|'
            for piece in row:
                mystring += str(piece)
            mystring += '|\n'
        mystring += '-' * (self.dimension + 2)
        mystring += '\nWinner: ' + self.get_winner().name
        return mystring
    def set_position(self, pieces: list[list[Piece]]):
        if len(pieces) != self.dimension * 2 + 2:
            sys.exit()
        if len(pieces[0]) != self.dimension:
            sys.exit()
        for row in range(self.dimension):
            for idx, piece in enumerate(pieces[row]):
                self.pieces[row][idx].team = piece.team
    def make_move(self, column: int, row: int) -> Board:
        if(column >= self.dimension or row >= self.dimension):
            sys.exit()
        if self.on_move is Team.X:
            next_move = Team.O
        elif self.on_move is Team.O:
            next_move = Team.X
        else:
            sys.exit()
        board = Board(dimension = self.dimension, on_move = next_move)
        board.set_position(self.pieces)
        board.pieces[row][column].team = self.on_move
        return board
    def get_winner(self) -> Team:
        for line in self.pieces:
            team = line[0].team
            for idx in range(self.dimension):
                if line[idx].team is not team:
                    team = Team.E
            if team is not Team.E:
                return team
        return Team.E

def main() -> None:
    board = Board()
    board = board.make_move(0, 1)
    board = board.make_move(1, 1)
    old_board = board.make_move(0, 2)
    print(old_board)
    board = old_board.make_move(2, 2)
    board = board.make_move(0, 0)
    print(board)
    print(old_board)

main()
