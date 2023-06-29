from enum import Enum

Team = Enum('Team', ['X', 'O'])

class Piece:
    def __init__(self, team: Team):
        self.team = team


def main() -> None:
    piece = Piece(Team.X)
    print(piece)

main()
