from enum import Enum

Team = Enum('Team', ['X', 'O'])

class Piece:
    def __init__(self, team: Team):
        self.team = team
    def __str__(self) -> str:
        return self.team.name

class Board:
    def __init__(self, dimension: int):
        self.pieces = []
        for row in range(dimension):
            self.pieces.append([None] * dimension)
        self.dimension = dimension
    def __str__(self) -> str:
        mystring: str = '-' * (self.dimension + 2)
        mystring += '\n'
        for row in self.pieces:
            mystring += '|'
            for piece in row:
                if(piece is None):
                    mystring += ' '
                else:
                    mystring += str(piece)
            mystring += '|\n'
        mystring += '-' * (self.dimension + 2)
        return mystring
    def set_piece(self, column: int, row: int, piece: Piece) -> None:
        if(column >= self.dimension or row >= self.dimension):
            sys.exit()
        self.pieces[row][column] = piece

def main() -> None:
    piece = Piece(Team.X)
    print(piece)
    board = Board(3)
    board.set_piece(0,1,piece)
    print(board)

main()
