class Game:
    def __init__(self, word_length: int):
        self._word_length: int = word_length
        self._word: str = self.generate_random_word()

    # getters and setters
    @property
    def word_length(self) -> int:
        return self._word_length

    @word_length.setter
    def word_length(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Word length must be an integer")
        self._word_length = value

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Word word must be a string")
        self._word = value

    # class methods
    def generate_random_word(self) -> str:
        pass

    def validate_input(self, input_word: str) -> bool:
        if len(input_word) == self._word_length:
            for character in input_word:
                # ascii codes for lowercase alphabet, i.e., a-z
                if 97 <= ord(character.lower()) <= 122:
                    return True
        return False

    def check_letter_value(self, letter: str) -> bool:
        if letter in self._word:
            return True
        return False

    def check_letter_position(self, letter: str, position: int) -> bool:
        if self._word[position] == letter:
            return True
        return False

    def run(self) -> None:
        word: str = self.generate_random_word()


if __name__ == "__main__":
    game = Game(word_length=5)
    game.run()
