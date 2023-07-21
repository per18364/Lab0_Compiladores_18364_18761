from antlr4 import *
from yaplLexer import yaplLexer
from yaplParser import yaplParser
from antlr4.tree.Trees import Trees
from graphviz import Digraph

def visualize_tree(tree, filename):
    graph = Digraph(comment='YAPL Syntax Tree')
    build_graph(tree, graph)
    graph.render(filename, view=True)

def build_graph(tree, graph, parent=None):
    if tree.getText():
        node = str(hash(tree))
        graph.node(node, tree.getText())
        if parent:
            graph.edge(parent, node)
        for i in range(tree.getChildCount()):
            build_graph(tree.getChild(i), graph, node)

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

    visualize_tree(tree, "arbol_sintactico.pdf")

if __name__ == '__main__':
    main()