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
