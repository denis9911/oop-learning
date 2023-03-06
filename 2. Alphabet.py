import string

class Alphabet:
    def __init__(self, language, letters):
        self.language = language
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self, language, letters, letters_num):
        super.__init__(language, letters)
        self.__letters_num = letters_num

    def is_en_letter(self, letter):
        print(letter in string.ascii_uppercase)

    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example(self):
        print('London is the capital of Great Britan')
