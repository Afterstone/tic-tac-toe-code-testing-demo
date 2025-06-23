import enum


class State(enum.Enum):
    """
    Enum representing the state of the Tic Tac Toe game.
    """

    IN_PROGRESS = "in_progress"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"

    def __str__(self):
        return self.value
