# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, OPERATOR, EOF, SPACE = 'INTEGER', 'OPERATOR', 'EOF', "SPACE"
#PRI1_OPLIST = ['MINUS','PLUS']
#PRI2_OPLIST = ['MUL', 'DIV']
PR1, PR2 = 'P1', 'P2'
oplist1 = ['*', '/']
oplist2 = ['+', '-']


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

class Lexer(object):

    def __init__(self, text):
        # client string input, e.g. "3 * 5", "12 / 3 * 4", etc
        self.text = text
        self.len = len(self.text)
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character.')

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

            if self.current_char in oplist1:
                return Token(PR1, self.operator())

            if self.current_char in oplist2:
                return Token(PR2, self.operator())

            self.error()

        return Token(EOF, None)

class Interpreter(object):

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax. {0}'.format(self.current_token))

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        #print(self.current_token)
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type == PR1:
            op = self.current_token
            self.eat(PR1)
            if op.value == '*':
                result = result * self.factor()
            elif op.value == '/':
                result = result / self.factor()

        #print('term:{0}'.format(result))
        return result

        
    def expr(self):
        """Arithmetic expression parser / interpreter.
 
        calc>  14 + 2 * 3 - 6 / 2
        17
 
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        result = self.term()
        while self.current_token.type == PR2 :
            op = self.current_token
            self.eat(PR2)
            if op.value == '+':
                result = result + self.term()
            elif op.value == '-':
                result = result - self.term()
            else:
                self.error()
        
        if self.current_token.type != EOF:
            self.error()
 
        return result

def main():
    while True:
        try:
            text = input('calc> ')
            if not text:
                continue  
            lexer = Lexer(text)
            interpreter = Interpreter(lexer)
            result = interpreter.expr()
            print(result)
        except Exception as e:
            print(e)
            continue
        except EOFError:
            break       

if __name__ == '__main__':
    main()
