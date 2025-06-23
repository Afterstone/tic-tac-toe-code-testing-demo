from tic_tac_toe.player import Player
from tic_tac_toe.board import Board
import random


def get_human_player_details() -> Player:
    name = input("Enter your name: ")
    symbol = input("Enter player symbol (X or O): ")

    return Player(name, symbol)


def make_random_move(board: Board, ai_player: Player) -> None:
    # Select a random empty cell for the AI move
    empty_cells = [
        (r, c) for r in range(3) for c in range(3) if board.board[r][c] == " "
    ]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board.make_move(row, col, ai_player.symbol)


def run_game_loop_with_human_and_ai(
    board: Board, human_player: Player, ai_player: Player
) -> None:
    while True:
        print(board.get_printable_board())

        # Get and handle human player's move
        move = input(
            f"{human_player.name}, enter your move (row and column, e.g., 1 2): "
        )
        row, col = map(int, move.split())
        board.make_move(row, col, human_player.symbol)

        # Check if the human player has won
        # TODO: Duplicated code, consider refactoring
        winner = board.check_winner()
        if winner:
            print(board.get_printable_board())
            print(f"{winner.name} wins!")
            break

        # AI makes its move
        make_random_move(board, ai_player)

        # Check if the AI player has won
        # TODO: Duplicated code, consider refactoring
        winner = board.check_winner()
        if winner:
            print(board.get_printable_board())
            print(f"{winner.name} wins!")
            break


def main():
    human_player = get_human_player_details()
    ai_player = Player("AI", "P" if human_player.symbol == "X" else "X")

    board = Board(player_1=human_player, player_2=ai_player)

    run_game_loop_with_human_and_ai(board, human_player, ai_player)


if __name__ == "__main__":
    main()
