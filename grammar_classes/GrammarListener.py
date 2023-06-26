# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#start.
    def enterStart(self, ctx:GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by GrammarParser#start.
    def exitStart(self, ctx:GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by GrammarParser#s.
    def enterS(self, ctx:GrammarParser.SContext):
        pass

    # Exit a parse tree produced by GrammarParser#s.
    def exitS(self, ctx:GrammarParser.SContext):
        pass


    # Enter a parse tree produced by GrammarParser#np.
    def enterNp(self, ctx:GrammarParser.NpContext):
        pass

    # Exit a parse tree produced by GrammarParser#np.
    def exitNp(self, ctx:GrammarParser.NpContext):
        pass


    # Enter a parse tree produced by GrammarParser#nominal.
    def enterNominal(self, ctx:GrammarParser.NominalContext):
        pass

    # Exit a parse tree produced by GrammarParser#nominal.
    def exitNominal(self, ctx:GrammarParser.NominalContext):
        pass


    # Enter a parse tree produced by GrammarParser#vp.
    def enterVp(self, ctx:GrammarParser.VpContext):
        pass

    # Exit a parse tree produced by GrammarParser#vp.
    def exitVp(self, ctx:GrammarParser.VpContext):
        pass


    # Enter a parse tree produced by GrammarParser#pp.
    def enterPp(self, ctx:GrammarParser.PpContext):
        pass

    # Exit a parse tree produced by GrammarParser#pp.
    def exitPp(self, ctx:GrammarParser.PpContext):
        pass



del GrammarParser