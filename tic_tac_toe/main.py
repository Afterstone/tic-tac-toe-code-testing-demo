from tic_tac_toe.player import Player
from tic_tac_toe.board import BoardState, make_move, get_printable_board, check_winner
import random


def get_human_player_details() -> Player:
    name = input("Enter your name: ")
    symbol = input("Enter player symbol (X or O): ")

    return Player(name, symbol)


def make_random_move(board: BoardState, player: Player) -> None:
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board.board[r][c] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        make_move(board, row, col, player.symbol)


def run_game_loop_with_human_and_ai(board: BoardState) -> None:
    while True:
        print(get_printable_board(board))

        # Get and handle human player's move
        move = input(f"{board.player_1.name}, enter your move (row and column, e.g., 1 2): ")
        row, col = map(int, move.split())
        make_move(board, row, col, board.player_1.symbol)

        # Check if the human player has won
        # TODO: Duplicated code, consider refactoring
        winner = check_winner(board)
        if winner:
            print(get_printable_board(board))
            print(f"{winner.name} wins!")
            break

        # AI makes its move
        make_random_move(board, board.player_2)

        # Check if the AI player has won
        # TODO: Duplicated code, consider refactoring
        winner = check_winner(board)
        if winner:
            print(get_printable_board(board))
            print(f"{winner.name} wins!")
            break


def main():
    human_player = get_human_player_details()
    ai_player = Player("AI", "P" if human_player.symbol == "X" else "X")

    board = BoardState(
        player_1=human_player,
        player_2=ai_player,
        board=[[" " for _ in range(3)] for _ in range(3)],
    )

    run_game_loop_with_human_and_ai(board)


if __name__ == "__main__":
    main()
