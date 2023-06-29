from enum import Enum

Team = Enum('Team', ['X', 'O'])

class Piece:
    def __init__(self, team: Team):
        self.team = team
    def __str__(self) -> str:
        return self.team.name


def main() -> None:
    piece = Piece(Team.X)
    print(piece)

main()
