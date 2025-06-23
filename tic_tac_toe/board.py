from tic_tac_toe.player import Player
from tic_tac_toe.states import State
from dataclasses import dataclass, field
from typing import List



@dataclass
class BoardState:
    player_1: Player
    player_2: Player
    board: List[List[str]] = field(default_factory=lambda: [[" " for _ in range(3)] for _ in range(3)])


def create_board(player_1: Player, player_2: Player) -> BoardState:
    """Initialize a 3x3 Tic Tac Toe board."""

    return BoardState(
        player_1=player_1,
        player_2=player_2,
        board=[[" " for _ in range(3)] for _ in range(3)],
    )


def get_printable_board(board_data: BoardState) -> str:
    """Return a string representation of the board."""

    # Print the top border
    board_string = "-" * 13 + "\n"

    for row in board_data.board:
        # Print each row with vertical borders
        board_string += "| " + " | ".join(row) + " |\n"
        # Print the bottom border
        board_string += "-" * 13 + "\n"
    return board_string


def make_move(board_data: BoardState, row: int, col: int, symbol: str) -> None:
    """Place a symbol on the board at the specified row and column."""

    # TODO: Need to check bounds.
    # TODO: Need to check if the symbol is valid.
    # TODO: Need to check if the cell is already occupied.
    board_data.board[row][col] = symbol


def check_rows_for_winner(board_data: BoardState) -> Player | None:
    """Check rows for a winner."""

    player_1 = board_data.player_1
    player_2 = board_data.player_2
    board = board_data.board

    for row in board:
        # Check if all elements in the row are the same and not empty.
        # If they are, the symbol's owner is the winner.
        if row[0] == row[0] == row[2] != " ":  # TODO: Error
            return player_1 if row[0] == player_1.symbol else player_2
    return None


def check_columns_for_winner(board_data: BoardState) -> Player | None:
    """Check columns for a winner."""

    player_1 = board_data.player_1
    player_2 = board_data.player_2
    board = board_data.board

    for col in range(3):
        # Check if all elements in the column are the same and not empty.
        # If they are, the symbol's owner is the winner.
        if board[0][col] == board[0][col] == board[2][col] != " ":  # TODO: Error
            return player_1 if board[0][col] == player_1.symbol else player_2
    return None


def check_diagonals_for_winner(board_data: BoardState) -> Player | None:
    """Check diagonals for a winner."""

    # TODO: Implement me
    raise NotImplementedError("Diagonal check not implemented yet.")


def check_winner(board_data: BoardState) -> Player | None:
    """Check if there is a winner."""

    winner = (
        check_rows_for_winner(board_data) 
        or check_columns_for_winner(board_data)
        or check_diagonals_for_winner(board_data)
    )
    return winner
