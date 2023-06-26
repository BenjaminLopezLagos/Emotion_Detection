# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#start.
    def visitStart(self, ctx:GrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#s.
    def visitS(self, ctx:GrammarParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#np.
    def visitNp(self, ctx:GrammarParser.NpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#nominal.
    def visitNominal(self, ctx:GrammarParser.NominalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#vp.
    def visitVp(self, ctx:GrammarParser.VpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pp.
    def visitPp(self, ctx:GrammarParser.PpContext):
        return self.visitChildren(ctx)



del GrammarParser