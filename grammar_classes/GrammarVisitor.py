# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#sentence.
    def visitSentence(self, ctx:GrammarParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#subject.
    def visitSubject(self, ctx:GrammarParser.SubjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#object.
    def visitObject(self, ctx:GrammarParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#verb.
    def visitVerb(self, ctx:GrammarParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#article.
    def visitArticle(self, ctx:GrammarParser.ArticleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#conjuntion.
    def visitConjuntion(self, ctx:GrammarParser.ConjuntionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#point.
    def visitPoint(self, ctx:GrammarParser.PointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#adjective.
    def visitAdjective(self, ctx:GrammarParser.AdjectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#negation.
    def visitNegation(self, ctx:GrammarParser.NegationContext):
        return self.visitChildren(ctx)



del GrammarParser