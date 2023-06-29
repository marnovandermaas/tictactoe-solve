from enum import Enum

Team = Enum('Team', ['X', 'O', 'E'])

class Piece:
    def __init__(self, team: Team):
        self.team = team
    def __str__(self) -> str:
        return self.team.name

class Board:
    def __init__(self, dimension: int):
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
        self.dimension = dimension
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
    def set_piece(self, column: int, row: int, team: Team) -> None:
        if(column >= self.dimension or row >= self.dimension):
            sys.exit()
        self.pieces[row][column].team = team
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
    board = Board(3)
    board.set_piece(0, 1, Team.X)
    board.set_piece(1, 1, Team.O)
    board.set_piece(0, 2, Team.X)
    print(board)
    board.set_piece(0, 0, Team.X)
    print(board)

main()
