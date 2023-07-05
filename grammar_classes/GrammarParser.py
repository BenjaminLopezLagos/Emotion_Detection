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
        4,1,11,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,4,0,23,8,0,11,0,12,0,24,
        1,1,1,1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,
        2,1,2,5,2,43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,
        1,4,1,4,1,4,5,4,58,8,4,10,4,12,4,61,9,4,1,4,5,4,64,8,4,10,4,12,4,
        67,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,79,8,4,1,4,1,
        4,1,4,5,4,84,8,4,10,4,12,4,87,9,4,1,5,1,5,1,5,1,5,0,2,4,8,6,0,2,
        4,6,8,10,0,0,100,0,22,1,0,0,0,2,30,1,0,0,0,4,37,1,0,0,0,6,52,1,0,
        0,0,8,78,1,0,0,0,10,88,1,0,0,0,12,17,3,2,1,0,13,14,5,5,0,0,14,16,
        3,2,1,0,15,13,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,10,0,0,21,23,1,0,0,0,22,12,1,
        0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,1,1,0,0,0,26,
        27,3,4,2,0,27,28,3,8,4,0,28,31,1,0,0,0,29,31,3,8,4,0,30,26,1,0,0,
        0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,6,2,-1,0,33,38,5,1,0,0,34,38,
        5,2,0,0,35,36,5,3,0,0,36,38,3,6,3,0,37,32,1,0,0,0,37,34,1,0,0,0,
        37,35,1,0,0,0,38,44,1,0,0,0,39,40,10,1,0,0,40,41,5,5,0,0,41,43,3,
        4,2,2,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,
        5,1,0,0,0,46,44,1,0,0,0,47,48,5,7,0,0,48,53,3,6,3,0,49,53,5,7,0,
        0,50,51,5,6,0,0,51,53,3,6,3,0,52,47,1,0,0,0,52,49,1,0,0,0,52,50,
        1,0,0,0,53,7,1,0,0,0,54,55,6,4,-1,0,55,59,5,9,0,0,56,58,5,8,0,0,
        57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,65,1,
        0,0,0,61,59,1,0,0,0,62,64,5,6,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,
        63,1,0,0,0,65,66,1,0,0,0,66,79,1,0,0,0,67,65,1,0,0,0,68,69,5,9,0,
        0,69,79,3,4,2,0,70,71,5,9,0,0,71,72,3,4,2,0,72,73,3,10,5,0,73,79,
        1,0,0,0,74,75,5,9,0,0,75,79,3,10,5,0,76,77,5,9,0,0,77,79,3,2,1,0,
        78,54,1,0,0,0,78,68,1,0,0,0,78,70,1,0,0,0,78,74,1,0,0,0,78,76,1,
        0,0,0,79,85,1,0,0,0,80,81,10,2,0,0,81,82,5,5,0,0,82,84,3,8,4,3,83,
        80,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,9,1,0,0,
        0,87,85,1,0,0,0,88,89,5,4,0,0,89,90,3,4,2,0,90,11,1,0,0,0,10,17,
        24,30,37,44,52,59,65,78,85
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'DT'", "<INVALID>", 
                     "'CC'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "PRONOUN", "PROPERNOUN", "DETERMINER", 
                      "PREPOSITION", "CONJUNCTION", "ADJECTIVE", "NOUN", 
                      "ADVERB", "VERB", "DOT", "WS" ]

    RULE_start = 0
    RULE_s = 1
    RULE_np = 2
    RULE_nominal = 3
    RULE_vp = 4
    RULE_pp = 5

    ruleNames =  [ "start", "s", "np", "nominal", "vp", "pp" ]

    EOF = Token.EOF
    PRONOUN=1
    PROPERNOUN=2
    DETERMINER=3
    PREPOSITION=4
    CONJUNCTION=5
    ADJECTIVE=6
    NOUN=7
    ADVERB=8
    VERB=9
    DOT=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.SContext)
            else:
                return self.getTypedRuleContext(GrammarParser.SContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.DOT)
            else:
                return self.getToken(GrammarParser.DOT, i)

        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.CONJUNCTION)
            else:
                return self.getToken(GrammarParser.CONJUNCTION, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = GrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.s()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 13
                    self.match(GrammarParser.CONJUNCTION)
                    self.state = 14
                    self.s()
                    self.state = 19
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 20
                self.match(GrammarParser.DOT)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 526) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def np(self):
            return self.getTypedRuleContext(GrammarParser.NpContext,0)


        def vp(self):
            return self.getTypedRuleContext(GrammarParser.VpContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = GrammarParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3]:
                self.state = 26
                self.np(0)
                self.state = 27
                self.vp(0)
                pass
            elif token in [9]:
                self.state = 29
                self.vp(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRONOUN(self):
            return self.getToken(GrammarParser.PRONOUN, 0)

        def PROPERNOUN(self):
            return self.getToken(GrammarParser.PROPERNOUN, 0)

        def DETERMINER(self):
            return self.getToken(GrammarParser.DETERMINER, 0)

        def nominal(self):
            return self.getTypedRuleContext(GrammarParser.NominalContext,0)


        def np(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.NpContext)
            else:
                return self.getTypedRuleContext(GrammarParser.NpContext,i)


        def CONJUNCTION(self):
            return self.getToken(GrammarParser.CONJUNCTION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_np

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNp" ):
                listener.enterNp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNp" ):
                listener.exitNp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNp" ):
                return visitor.visitNp(self)
            else:
                return visitor.visitChildren(self)



    def np(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.NpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_np, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 33
                self.match(GrammarParser.PRONOUN)
                pass
            elif token in [2]:
                self.state = 34
                self.match(GrammarParser.PROPERNOUN)
                pass
            elif token in [3]:
                self.state = 35
                self.match(GrammarParser.DETERMINER)
                self.state = 36
                self.nominal()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.NpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_np)
                    self.state = 39
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 40
                    self.match(GrammarParser.CONJUNCTION)
                    self.state = 41
                    self.np(2) 
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NominalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self):
            return self.getToken(GrammarParser.NOUN, 0)

        def nominal(self):
            return self.getTypedRuleContext(GrammarParser.NominalContext,0)


        def ADJECTIVE(self):
            return self.getToken(GrammarParser.ADJECTIVE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_nominal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNominal" ):
                listener.enterNominal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNominal" ):
                listener.exitNominal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNominal" ):
                return visitor.visitNominal(self)
            else:
                return visitor.visitChildren(self)




    def nominal(self):

        localctx = GrammarParser.NominalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nominal)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(GrammarParser.NOUN)
                self.state = 48
                self.nominal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(GrammarParser.NOUN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(GrammarParser.ADJECTIVE)
                self.state = 51
                self.nominal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERB(self):
            return self.getToken(GrammarParser.VERB, 0)

        def ADVERB(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.ADVERB)
            else:
                return self.getToken(GrammarParser.ADVERB, i)

        def ADJECTIVE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.ADJECTIVE)
            else:
                return self.getToken(GrammarParser.ADJECTIVE, i)

        def np(self):
            return self.getTypedRuleContext(GrammarParser.NpContext,0)


        def pp(self):
            return self.getTypedRuleContext(GrammarParser.PpContext,0)


        def s(self):
            return self.getTypedRuleContext(GrammarParser.SContext,0)


        def vp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VpContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VpContext,i)


        def CONJUNCTION(self):
            return self.getToken(GrammarParser.CONJUNCTION, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_vp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVp" ):
                listener.enterVp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVp" ):
                listener.exitVp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVp" ):
                return visitor.visitVp(self)
            else:
                return visitor.visitChildren(self)



    def vp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.VpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_vp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 55
                self.match(GrammarParser.VERB)

                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 56
                        self.match(GrammarParser.ADVERB) 
                    self.state = 61
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 62
                        self.match(GrammarParser.ADJECTIVE) 
                    self.state = 67
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 2:
                self.state = 68
                self.match(GrammarParser.VERB)
                self.state = 69
                self.np(0)
                pass

            elif la_ == 3:
                self.state = 70
                self.match(GrammarParser.VERB)
                self.state = 71
                self.np(0)
                self.state = 72
                self.pp()
                pass

            elif la_ == 4:
                self.state = 74
                self.match(GrammarParser.VERB)
                self.state = 75
                self.pp()
                pass

            elif la_ == 5:
                self.state = 76
                self.match(GrammarParser.VERB)
                self.state = 77
                self.s()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.VpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_vp)
                    self.state = 80
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 81
                    self.match(GrammarParser.CONJUNCTION)
                    self.state = 82
                    self.vp(3) 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPOSITION(self):
            return self.getToken(GrammarParser.PREPOSITION, 0)

        def np(self):
            return self.getTypedRuleContext(GrammarParser.NpContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_pp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPp" ):
                listener.enterPp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPp" ):
                listener.exitPp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPp" ):
                return visitor.visitPp(self)
            else:
                return visitor.visitChildren(self)




    def pp(self):

        localctx = GrammarParser.PpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(GrammarParser.PREPOSITION)
            self.state = 89
            self.np(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.np_sempred
        self._predicates[4] = self.vp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def np_sempred(self, localctx:NpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def vp_sempred(self, localctx:VpContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




