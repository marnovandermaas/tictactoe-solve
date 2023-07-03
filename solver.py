#Necessary to use list[Piece] instead of List[Piece]
from __future__ import annotations

from enum import Enum

#Two teams X and O, as well as an E for empty fields
Team = Enum('Team', ['X', 'O', 'E'])

class Piece:
    #Currently this just takes a team, but eventually it can include a power like for Gobblet
    def __init__(self, team: Team):
        self.team = team
    def __str__(self) -> str:
        return self.team.name
    def __eq__(self, other) -> bool:
        return self.team == other.team

class Board:
    #Creates a board object
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
        self.winner = None
    #Prints all rows columns and diagonals including the winner of a position
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
    #Returns a short string for lots of printing
    def short_string(self) -> str:
        mystring = '{'
        for row in range(self.dimension):
            for piece in self.pieces[row]:
                mystring += str(piece)
            mystring += ','
        mystring += str(self.winner) + '}'
        return mystring
    def __eq__(self, other: Board) -> bool:
        if self.dimension != other.dimension:
            return False
        if self.on_move != other.on_move:
            return False
        for row in range(self.dimension):
            for idx, piece in enumerate(self.pieces[row]):
                if piece != other.pieces[row][idx]:
                    return False
        return True
    #Set a postition
    def set_position(self, pieces: list[list[Piece]]):
        if len(pieces) != self.dimension * 2 + 2:
            sys.exit()
        if len(pieces[0]) != self.dimension:
            sys.exit()
        for row in range(self.dimension):
            for idx, piece in enumerate(pieces[row]):
                self.pieces[row][idx].team = piece.team
    #Make a move, advance the turn and return the new board as a new object
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
    #Evaluates who is winning in the position, if no one, return E.
    def get_winner(self) -> Team:
        for line in self.pieces:
            team = line[0].team
            for idx in range(self.dimension):
                if line[idx].team is not team:
                    team = Team.E
            if team is not Team.E:
                return team
        return Team.E
    #Generate list of tuples of possible moves
    def get_moves(self) -> list[tuple(int,int)]:
        moves: list[tuple(int,int)] = []
        for row in range(self.dimension):
            for idx, piece in enumerate(self.pieces[row]):
                if piece.team is Team.E:
                    moves.append((idx,row))
        return moves

def recursive_solve(boards: list[Board], already_searched: list[Board] = [], depth: int = 0) -> list[Board]:
    ret_val = boards.copy()
    if depth < 3:
        print("Starting recursion " + str(depth) + " with length " + str(len(ret_val)))
    for board in boards:
        if(board.get_winner() == Team.E):
            new_boards = []
            moves = board.get_moves()
            for move in moves:
                new_board = board.make_move(move[0], move[1])
                if new_board not in already_searched:
                    new_boards.append(new_board)
            ret_val += recursive_solve(new_boards, ret_val, depth + 1)
    return ret_val

def evaluate_positions(unique_boards: list[Board]) -> None:
    #Mark winner for decisive positions
    for board in unique_boards:
        winner = board.get_winner()
        if winner != Team.E:
            board.winner = winner

def main() -> None:
    board = Board()
    board = board.make_move(0, 1)
    board = board.make_move(1, 1)
    old_board = board.make_move(0, 2)
    print(old_board) #E should be winner
    print(old_board.short_string())
    print(old_board.get_moves())
    board = old_board.make_move(2, 2)
    board = board.make_move(0, 0)
    print(board) #X should be winner
    print(board.short_string())
    print(board.get_moves())
    old_board = old_board.make_move(2, 2)
    old_board = old_board.make_move(0, 0)
    print(id(board))
    print(id(old_board))
    print(board == old_board) #This should be True even though the IDs above don't match

    print("Now trying to recursively solve")
    root = [Board()]
    space = recursive_solve(root)
    print("Final recursion with length " + str(len(space)))
    unique_space = []
    #Filter out the unique positions
    for board in space:
        if board not in unique_space:
            unique_space.append(board)
    evaluate_positions(unique_space)
    print("Unique space with length " + str(len(unique_space)))
    with open("recursion.txt", "w") as f:
        for board in unique_space:
            print(board.short_string(), file=f)

main()
