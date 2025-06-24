from tic_tac_toe.board import check_rows_for_winner, BoardState, check_columns_for_winner, check_diagonals_for_winner
from tic_tac_toe.player import Player


def test_check_rows_for_winner__finds_valid_winner():
    # Arrange
    player_1 = Player(name="Alice", symbol="X")
    player_2 = Player(name="Bob", symbol="O")
    board_data = BoardState(player_1=player_1, player_2=player_2)

    board_data.board = [
        ["X", "X", "X"],
        ["O", " ", "O"],
        [" ", " ", " "]
    ]

    # Act
    winner = check_rows_for_winner(board_data)

    # Assert
    assert winner == player_1, f"Expected {player_1} to be the winner, but got {winner}"


def test_check_rows_for_winner__no_winner():
    # Arrange
    player_1 = Player(name="Alice", symbol="X")
    player_2 = Player(name="Bob", symbol="O")

    board_data = BoardState(player_1=player_1, player_2=player_2)
    board_data.board = [
        ["X", "O", "X"],
        ["O", " ", "O"],
        [" ", " ", " "]
    ]

    # Act
    winner = check_rows_for_winner(board_data)

    # Assert
    assert winner is None, f"Expected no winner, but got {winner}"


def test_check_columns_for_winner__finds_valid_winner():
    raise NotImplementedError("This test is not implemented yet.")
    # Arrange
    ...  # TODO: Implement me

    # Act
    ...  # TODO: Implement me

    # Assert
    ...  # TODO: Implement me


def test_check_columns_for_winner__no_winner():
    raise NotImplementedError("This test is not implemented yet.")
    # Arrange
    ...  # TODO: Implement me

    # Act
    ...  # TODO: Implement me

    # Assert
    ...  # TODO: Implement me


def test_check_diagonals_for_winner__finds_valid_winner():
    raise NotImplementedError("This test is not implemented yet.")
    # Arrange
    ...  # TODO: Implement me

    # Act
    ...  # TODO: Implement me

    # Assert
    ...  # TODO: Implement me


def test_check_diagonals_for_winner__no_winner():
    raise NotImplementedError("This test is not implemented yet.")
    # Arrange
    ...  # TODO: Implement me

    # Act
    ...  # TODO: Implement me

    # Assert
    ...  # TODO: Implement me