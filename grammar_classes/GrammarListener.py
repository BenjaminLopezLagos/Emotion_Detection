# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#sentence.
    def enterSentence(self, ctx:GrammarParser.SentenceContext):
        pass

    # Exit a parse tree produced by GrammarParser#sentence.
    def exitSentence(self, ctx:GrammarParser.SentenceContext):
        pass


    # Enter a parse tree produced by GrammarParser#subject.
    def enterSubject(self, ctx:GrammarParser.SubjectContext):
        pass

    # Exit a parse tree produced by GrammarParser#subject.
    def exitSubject(self, ctx:GrammarParser.SubjectContext):
        pass


    # Enter a parse tree produced by GrammarParser#object.
    def enterObject(self, ctx:GrammarParser.ObjectContext):
        pass

    # Exit a parse tree produced by GrammarParser#object.
    def exitObject(self, ctx:GrammarParser.ObjectContext):
        pass


    # Enter a parse tree produced by GrammarParser#verb.
    def enterVerb(self, ctx:GrammarParser.VerbContext):
        pass

    # Exit a parse tree produced by GrammarParser#verb.
    def exitVerb(self, ctx:GrammarParser.VerbContext):
        pass


    # Enter a parse tree produced by GrammarParser#article.
    def enterArticle(self, ctx:GrammarParser.ArticleContext):
        pass

    # Exit a parse tree produced by GrammarParser#article.
    def exitArticle(self, ctx:GrammarParser.ArticleContext):
        pass


    # Enter a parse tree produced by GrammarParser#conjuntion.
    def enterConjuntion(self, ctx:GrammarParser.ConjuntionContext):
        pass

    # Exit a parse tree produced by GrammarParser#conjuntion.
    def exitConjuntion(self, ctx:GrammarParser.ConjuntionContext):
        pass


    # Enter a parse tree produced by GrammarParser#point.
    def enterPoint(self, ctx:GrammarParser.PointContext):
        pass

    # Exit a parse tree produced by GrammarParser#point.
    def exitPoint(self, ctx:GrammarParser.PointContext):
        pass


    # Enter a parse tree produced by GrammarParser#adjective.
    def enterAdjective(self, ctx:GrammarParser.AdjectiveContext):
        pass

    # Exit a parse tree produced by GrammarParser#adjective.
    def exitAdjective(self, ctx:GrammarParser.AdjectiveContext):
        pass


    # Enter a parse tree produced by GrammarParser#negation.
    def enterNegation(self, ctx:GrammarParser.NegationContext):
        pass

    # Exit a parse tree produced by GrammarParser#negation.
    def exitNegation(self, ctx:GrammarParser.NegationContext):
        pass



del GrammarParser