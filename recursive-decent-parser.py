from astree import AST, BinOp, Num, UnaryOP
from lexer import NUMBER, PLUS, MINUS, STAR, SLASH, EOF, Lexer

class Parser(object):
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self) -> Exception:
        return Exception('Invalid Syntax')
    
    def eat(self, token_type: str) -> None:
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def number(self):
        """
        number = digit+ ( "." digit+ )?
        digit  = "0" ... "9"
        """
        token = self.current_token
        if token.type == NUMBER:
            self.eat(NUMBER)
            return Num(token)
        else:
            return self.error()

    def unary(self):
        """
        unary  = "-" unary | number
        number = digit+ ( "." digit+ )?
        digit  = "0" ... "9"
        """
        token = self.current_token

        if self.current_token.type == MINUS:
            self.eat(MINUS)
            return UnaryOP(op=token, right=self.number)
        else:
            node = self.number()
            return node

    def expr(self):
        """
        expr   = unary ("+" | "-" | "*" | "/") ( unary | expr )
        unary  = "-" unary | number
        number = digit+ ( "." digit+ )?
        digit  = "0" ... "9"
        """
        node = self.unary()

        if self.current_token.type in (PLUS, MINUS, STAR, SLASH):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            elif token.type == STAR:
                self.eat(STAR)
            elif token.type == SLASH:
                self.eat(SLASH)

            node = BinOp(left=node, op=token, right=self.expr())

        return node

    def parse(self):
        return self.expr()


if __name__ == "__main__":
    lex = Lexer("1 + 2 * 3")
    par = Parser(lex)
    print(par.parse())