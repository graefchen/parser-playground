# Influenced by: https://ruslanspivak.com/lsbasi-part1/
NUMBER, PLUS, MINUS, STAR, SLASH, EOF = "NUMBER", "PLUS", "MINUS", "STAR", "SLASH", "EOF"

class Token(object):
    """Token."""
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()

class Lexer(object):
    """Lexer."""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalide character")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char is not None and self.current_char == ".":
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

        return float(result)

    def get_next_token(self):

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(NUMBER, self.number())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                if self.current_char.isdigit():
                    return Token(NUMBER, self.number())
                return Token(MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(STAR, "*")

            if self.current_char == "/":
                self.advance()
                return Token(SLASH, "/")

            self.error()

        return Token(EOF, None)


if __name__ == "__main__":
    lex = Lexer("1 + 2 / 3")
    while lex.pos <= len(lex.text) - 1:
        print(lex.get_next_token())