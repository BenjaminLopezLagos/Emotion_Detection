# Generated from Grammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,3,0,21,8,0,1,0,1,0,3,0,25,8,0,1,0,3,0,
        28,8,0,1,0,3,0,31,8,0,1,0,3,0,34,8,0,1,0,1,0,4,0,38,8,0,11,0,12,
        0,39,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,1,4,1,0,5,7,1,0,10,12,
        54,0,37,1,0,0,0,2,41,1,0,0,0,4,43,1,0,0,0,6,45,1,0,0,0,8,47,1,0,
        0,0,10,49,1,0,0,0,12,51,1,0,0,0,14,53,1,0,0,0,16,55,1,0,0,0,18,20,
        3,2,1,0,19,21,3,16,8,0,20,19,1,0,0,0,20,21,1,0,0,0,21,22,1,0,0,0,
        22,24,3,6,3,0,23,25,3,16,8,0,24,23,1,0,0,0,24,25,1,0,0,0,25,27,1,
        0,0,0,26,28,3,8,4,0,27,26,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,
        31,3,14,7,0,30,29,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,34,3,4,
        2,0,33,32,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,3,12,6,0,36,
        38,1,0,0,0,37,18,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,
        0,40,1,1,0,0,0,41,42,5,13,0,0,42,3,1,0,0,0,43,44,5,13,0,0,44,5,1,
        0,0,0,45,46,5,13,0,0,46,7,1,0,0,0,47,48,7,0,0,0,48,9,1,0,0,0,49,
        50,7,1,0,0,50,11,1,0,0,0,51,52,5,8,0,0,52,13,1,0,0,0,53,54,5,9,0,
        0,54,15,1,0,0,0,55,56,7,2,0,0,56,17,1,0,0,0,6,20,24,27,30,33,39
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'some'", "'the'", "'an'", "'and'", 
                     "'but'", "'or'", "'.'", "'so'", "'don t'", "'doesn t'", 
                     "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WORD", "WS" ]

    RULE_sentence = 0
    RULE_subject = 1
    RULE_object = 2
    RULE_verb = 3
    RULE_article = 4
    RULE_conjuntion = 5
    RULE_point = 6
    RULE_adjective = 7
    RULE_negation = 8

    ruleNames =  [ "sentence", "subject", "object", "verb", "article", "conjuntion", 
                   "point", "adjective", "negation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    WORD=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subject(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.SubjectContext)
            else:
                return self.getTypedRuleContext(GrammarParser.SubjectContext,i)


        def verb(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VerbContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VerbContext,i)


        def point(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.PointContext)
            else:
                return self.getTypedRuleContext(GrammarParser.PointContext,i)


        def negation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.NegationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.NegationContext,i)


        def article(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ArticleContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ArticleContext,i)


        def adjective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AdjectiveContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AdjectiveContext,i)


        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ObjectContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ObjectContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = GrammarParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.subject()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0):
                    self.state = 19
                    self.negation()


                self.state = 22
                self.verb()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0):
                    self.state = 23
                    self.negation()


                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                    self.state = 26
                    self.article()


                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 29
                    self.adjective()


                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 32
                    self.object_()


                self.state = 35
                self.point()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(GrammarParser.WORD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_subject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubject" ):
                listener.enterSubject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubject" ):
                listener.exitSubject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubject" ):
                return visitor.visitSubject(self)
            else:
                return visitor.visitChildren(self)




    def subject(self):

        localctx = GrammarParser.SubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(GrammarParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(GrammarParser.WORD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = GrammarParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_object)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(GrammarParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(GrammarParser.WORD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_verb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb" ):
                listener.enterVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb" ):
                listener.exitVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = GrammarParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_verb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GrammarParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArticleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_article

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticle" ):
                listener.enterArticle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticle" ):
                listener.exitArticle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArticle" ):
                return visitor.visitArticle(self)
            else:
                return visitor.visitChildren(self)




    def article(self):

        localctx = GrammarParser.ArticleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_article)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjuntionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_conjuntion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjuntion" ):
                listener.enterConjuntion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjuntion" ):
                listener.exitConjuntion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjuntion" ):
                return visitor.visitConjuntion(self)
            else:
                return visitor.visitChildren(self)




    def conjuntion(self):

        localctx = GrammarParser.ConjuntionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conjuntion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_point

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoint" ):
                listener.enterPoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoint" ):
                listener.exitPoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoint" ):
                return visitor.visitPoint(self)
            else:
                return visitor.visitChildren(self)




    def point(self):

        localctx = GrammarParser.PointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_point)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(GrammarParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdjectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_adjective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdjective" ):
                listener.enterAdjective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdjective" ):
                listener.exitAdjective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdjective" ):
                return visitor.visitAdjective(self)
            else:
                return visitor.visitChildren(self)




    def adjective(self):

        localctx = GrammarParser.AdjectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_adjective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(GrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_negation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)




    def negation(self):

        localctx = GrammarParser.NegationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_negation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





