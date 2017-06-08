# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, OPERATOR, EOF, SPACE = 'INTEGER', 'OPERATOR', 'EOF', "SPACE"
oplist = ['+', '-', '*', '/']


class ExprException(Exception):
    pass


class Token(object):

    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    __repr__ = __str__


class Interpreter(object):

    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        self.len = len(text)
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self, info='wrong input'):
        raise ExprException('Error parsing input, {0}.'.format(info))

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > self.len - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def operator(self):
        """Return the operator from the input."""
        op = self.current_char
        self.advance()
        return op

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char in oplist:
                return Token(OPERATOR, self.operator())

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        self.current_token = self.get_next_token()
        print(self.current_token)
        return self.current_token.type == token_type

    def term(self):
        """Return an INTEGER token value."""
        if not self.eat(INTEGER):
            self.error()
        token = self.current_token
        return token.value

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        result = self.term()
        while self.eat(OPERATOR):
            op = self.current_token
            if op.value == '+':
                result = result + self.term()
            elif op.value == '-':
                result = result - self.term()
            elif op.value == '*':
                result = result * self.term()
            elif op.value == '/':
                result = result / self.term()
            else:
                self.error()
            print(result)
        
        if self.current_token.type != EOF:
            self.error()
 
        return result

def main():
    while True:
        try:
            text = input('calc> ')
            if not text:
                continue   
            interpreter = Interpreter(text)
            result = interpreter.expr()
            print(result)
        except ExprException as e:
            print(e)
            continue
        except EOFError:
            break       

if __name__ == '__main__':
    main()
