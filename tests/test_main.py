from tic_tac_toe.main import get_human_player_details, make_random_move, run_game_loop_with_human_and_ai
import pytest
from tic_tac_toe.board import BoardState, make_move, get_printable_board, check_winner
from tic_tac_toe.player import Player


def test_get_human_player_details__can_get_details(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    def get_human_player_details_info():
        yield "Human"
        yield "X"

    iterable_human_info = iter(get_human_player_details_info())
    monkeypatch.setattr('builtins.input', lambda _: next(iterable_human_info))
    
    # Act
    player = get_human_player_details()
    
    # Assert
    assert player.name == "Human"
    assert player.symbol == "X"


def test_make_random_move__can_make_move() -> None:
    # Arrange
    player_1 = Player("AI", "X")
    player_2 = Player("Human", "O")
    board = BoardState(player_1=player_1, player_2=player_2)

    # Act
    make_random_move(board, player_1)

    # Assert
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board.board[r][c] == " "]
    filled_cells = [board.board[r][c] for r in range(3) for c in range(3) if board.board[r][c] != " "]
    assert len(empty_cells) == 8  # At least one cell should be filled
    assert len(filled_cells) == 1  # At least one cell should be filled
    assert player_1.symbol in filled_cells  # The AI's symbol should be in the filled cells
    assert player_2.symbol not in filled_cells  # The human's symbol should not be in the filled cells