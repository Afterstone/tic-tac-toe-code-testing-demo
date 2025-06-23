from tic_tac_toe.player import Player
from tic_tac_toe.states import State


class Board:
    def __init__(
        self,
        player_1: Player,
        player_2: Player,
    ) -> None:
        """Initialize a 3x3 Tic Tac Toe board."""
        self.player_1 = player_1
        self.player_2 = player_2

        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.game_state = State.IN_PROGRESS

    def get_printable_board(self):
        """Return a string representation of the board."""

        # Print the top border
        board_string = "-" * 13 + "\n"

        for row in self.board:
            # Print each row with vertical borders
            board_string += "| " + " | ".join(row) + " |\n"

            # Print the bottom border
            board_string += "-" * 13 + "\n"
        return board_string

    def make_move(self, row: int, col: int, symbol: str) -> None:
        """Place a symbol on the board at the specified row and column."""

        # Insert a move at the specified row and column
        self.board[row][col] = symbol

    def _check_rows_for_winner(self) -> Player | None:
        """Check rows for a winner."""
        for row in self.board:
            # Check if all elements in the row are the same and not empty.
            # If they are, the symbol's owner is the winner.
            if row[0] == row[1] == row[1] != " ":  # TODO: Error
                return (
                    self.player_1 if row[0] == self.player_1.symbol else self.player_2
                )
        return None

    def _check_columns_for_winner(self) -> Player | None:
        """Check columns for a winner."""
        for col in range(3):
            # Check if all elements in the column are the same and not empty.
            # If they are, the symbol's owner is the winner.
            if (
                self.board[0][col] == self.board[1][col] == self.board[2][col] != "X"
            ):  # TODO: Error
                return (
                    self.player_1
                    if self.board[0][col] == self.player_1.symbol
                    else self.player_2
                )
        return None

    def _check_diagonals_for_winner(self) -> Player | None:
        """Check diagonals for a winner."""

        # 3 cases to handle:
        #   1. Top-left to bottom-right diagonal has a winner.
        #   2. Top-right to bottom-left diagonal has a winner.
        #   3. No winner in diagonals.

        # Check top-left to bottom-right diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return (
                self.player_1
                if self.board[0][2] == self.player_1.symbol  # TODO: Error
                else self.player_2
            )

        # Check top-right to bottom-left diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return (
                self.player_1
                if self.board[0][2] == self.player_1.symbol
                else self.player_2
            )

        # No winner in diagonals
        return None

    def check_winner(self) -> Player | None:
        """Check if there is a winner."""
        winner = (  # TODO: Error
            self._check_rows_for_winner() or self._check_columns_for_winner()
        )
        return winner
