from enum import Enum

Team = Enum('Team', ['X', 'O'])

class Piece:
    def __init__(self, team: Team):
        self.team = team
    def __str__(self) -> str:
        return self.team.name

class Board:
    def __init__(self, width: int, height: int):
        self.pieces = [[None] * width] * height
        self.width = width
        self.height = height
    def __str__(self) -> str:
        mystring: str = ''
        for row in self.pieces:
            for piece in row:
                if(piece is None):
                    mystring += ' '
                else:
                    mystring += piece
            mystring += '\n'
        return mystring

def main() -> None:
    piece = Piece(Team.X)
    print(piece)
    board = Board(3,3)
    print(board)

main()
