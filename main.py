class Game:
    def __init__(self, word_length: int):
        self._word_length: int = word_length

    # getters and setters
    @property
    def word_length(self) -> int:
        return self._word_length

    @word_length.setter
    def word_length(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Word length must be an integer")
        self._word_length = value

    # class methods
    def generate_random_word(self) -> str:
        pass

    def validate_input(self, input_word: str) -> bool:
        if len(input_word) == self._word_length:
            for character in input_word:
                if 97 <= ord(character.lower()) <= 122:
                    return True
        return False

    def run(self) -> None:
        word: str = self.generate_random_word()


if __name__ == "__main__":
    game = Game(word_length=5)
    game.run()
