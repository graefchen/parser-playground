from lexer import Token

class AST(object):
    pass

class BinOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self) -> str:
        return 'BinOP({left}, {op}, {right})'.format(left=self.left, op=self.op, right=self.right)

    def __repr__(self) -> None:
        return self.__str__()

class UnaryOP(AST):
    def __init__(self, op: Token, right: AST) -> None:
        self.token = self.op = op
        self.right = right

    def __str__(self) -> str:
        return 'UnaryOP({op}, {right})'.format(op=self.op, right=self.right)

    def __repr__(self) -> None:
        return self.__str__()

class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self) -> str:
        return 'Num({token}, {value})'.format(token=self.token, value=self.value)

    def __repr__(self) -> None:
        return self.__str__()