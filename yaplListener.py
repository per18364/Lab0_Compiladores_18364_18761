# Generated from yapl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#program.
    def enterProgram(self, ctx:yaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by yaplParser#program.
    def exitProgram(self, ctx:yaplParser.ProgramContext):
        pass


    # Enter a parse tree produced by yaplParser#classkey.
    def enterClasskey(self, ctx:yaplParser.ClasskeyContext):
        pass

    # Exit a parse tree produced by yaplParser#classkey.
    def exitClasskey(self, ctx:yaplParser.ClasskeyContext):
        pass


    # Enter a parse tree produced by yaplParser#feature.
    def enterFeature(self, ctx:yaplParser.FeatureContext):
        pass

    # Exit a parse tree produced by yaplParser#feature.
    def exitFeature(self, ctx:yaplParser.FeatureContext):
        pass


    # Enter a parse tree produced by yaplParser#formal.
    def enterFormal(self, ctx:yaplParser.FormalContext):
        pass

    # Exit a parse tree produced by yaplParser#formal.
    def exitFormal(self, ctx:yaplParser.FormalContext):
        pass


    # Enter a parse tree produced by yaplParser#expression.
    def enterExpression(self, ctx:yaplParser.ExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#expression.
    def exitExpression(self, ctx:yaplParser.ExpressionContext):
        pass



del yaplParser