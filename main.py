
import lexer
import parser

def main():

    conteudo = ""
    with open("trabalho de verdade\src\exemplo.lalg", 'r') as arquivo:
        conteudo = arquivo.read()

    lex = lexer.Lexer(conteudo)

    tokens = lex.tokenizar()

    parse = parser.Parser(tokens)
    parse.parse()


main()
