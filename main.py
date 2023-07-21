from antlr4 import *
from yaplLexer import yaplLexer
from yaplParser import yaplParser
from antlr4.tree.Trees import Trees
from graphviz import Digraph
import os

class yaplListener(ParseTreeListener):
    def enterExpression(self, ctx:yaplParser.ExpressionContext):
        print("Entrando en expresión:", ctx.getText())

    def exitExpression(self, ctx:yaplParser.ExpressionContext):
        print("Saliendo de expresión:", ctx.getText())

def main():
    # Lee el código fuente de YAPL desde un archivo o un string
    input_stream = FileStream("codigo.yapl")
    lexer = yaplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = yaplParser(stream)
    tree = parser.expression()

    # Visualizar el árbol de análisis sintáctico en consola
    print('Arbol de analisis sintactico: ', Trees.toStringTree(tree, recog=parser))

    # Crear el árbol de análisis
    yl = yaplListener()
    walker = ParseTreeWalker()
    walker.walk(yl, tree)

if __name__ == '__main__':
    main()