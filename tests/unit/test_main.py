from tic_tac_toe.main import get_greeting

def test_get_greeting__returns_expected_string() -> None:
    # Arrange
    expected_greeting = "Hello, Bob"

    # Act
    actual_greeting = get_greeting("Bob")

    # Assert
    assert actual_greeting == expected_greeting, "The greetings do not match."