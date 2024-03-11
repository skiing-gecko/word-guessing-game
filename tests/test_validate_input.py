import pytest
from main import Game


game = Game(word_length=5)


def test_word_length() -> None:

    word_correct_length: str = "a" * game.word_length

    # length + 1 used to get a word longer than specified
    word_too_long: str = "a" * (game.word_length + 1)

    # length - 1 used to get word shorter than specified
    word_too_short: str = "a" * (game.word_length - 1)

    assert game.validate_input(word_correct_length) is True
    assert game.validate_input(word_too_long) is False
    assert game.validate_input(word_too_short) is False


def test_only_alphabetical_characters() -> None:
    word_lower: str = "a" * game.word_length
    word_upper: str = "A" * game.word_length
    word_numbers: str = "1" * game.word_length
    word_symbols: str = "%" * game.word_length

    if game.word_length > 1:
        word_mixed: str = ("a" * (game.word_length - 1)) + "A"
        assert game.validate_input(word_mixed) is True

    assert game.validate_input(word_lower) is True
    assert game.validate_input(word_upper) is True
    assert game.validate_input(word_numbers) is False
    assert game.validate_input(word_symbols) is False
