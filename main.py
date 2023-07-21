from antlr4 import *
from yaplLexer import yaplLexer
from yaplParser import yaplParser

class yaplListener(ParseTreeListener):
    def enterExpr(self, ctx:yaplParser.ExpressionContext):
        print("Entrando en expresión:", ctx.getText())

    def exitExpr(self, ctx:yaplParser.ExpressionContext):
        print("Saliendo de expresión:", ctx.getText())

def main():
    # Lee el código fuente de YAPL desde un archivo o un string
    input_stream = FileStream("codigo.yapl")
    lexer = yaplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = yaplParser(stream)
    tree = parser.expression()

    # Crear el árbol de análisis
    yl = yaplListener()
    walker = ParseTreeWalker()
    walker.walk(yl, tree)

# if __name__ == '__main__':
main()