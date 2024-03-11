class Game:
    def __init__(self, word_length: int):
        self._word_length: int = word_length

    def generate_random_word(self) -> str:
        pass

    def validate_input(self, input_word: str) -> bool:
        pass

    def run(self):
        word: str = self.generate_random_word()


if __name__ == "__main__":
    game = Game(word_length=5)
    game.run()
