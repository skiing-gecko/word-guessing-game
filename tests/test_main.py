import pytest

from main import Game


@pytest.fixture
def game() -> Game:
    return Game(word_length=5)


def test_word_too_short(game: Game) -> None:
    word = "a" * (game.word_length - 1)

    assert game.validate_input(input_word=word) is False


def test_word_too_long(game: Game) -> None:
    word = "a" * (game.word_length + 1)

    assert game.validate_input(input_word=word) is False


def test_lowercase_word(game: Game) -> None:
    word = "a" * game.word_length

    assert game.validate_input(input_word=word) is True


def test_uppercase_word(game: Game) -> None:
    word = "A" * game.word_length

    assert game.validate_input(input_word=word) is True


def test_numbers_in_word(game: Game) -> None:
    word = "1" * game.word_length

    assert game.validate_input(input_word=word) is False


def test_symbols_in_word(game: Game) -> None:
    word = "%" * game.word_length

    assert game.validate_input(input_word=word) is False


def test_letter_present(game: Game) -> None:
    game.word = "a" * (game.word_length - 1) + "b"

    assert game.check_letter_value("a") is True
    assert game.check_letter_value("b") is True


def test_letter_not_present(game: Game) -> None:
    game.word = "a" * game.word_length

    assert game.check_letter_value("b") is False


def test_correct_letter_position(game: Game) -> None:
    game.word = "a" * (game.word_length - 1) + "b"

    assert game.check_letter_position("b", (game.word_length - 1)) is True
    assert game.check_letter_position("a", 0) is True


def test_incorrect_letter_position(game: Game) -> None:
    game.word = "a" * (game.word_length - 1) + "b"

    assert game.check_letter_position("b", (game.word_length - 2)) is False
    assert game.check_letter_position("a", (game.word_length - 1)) is False
