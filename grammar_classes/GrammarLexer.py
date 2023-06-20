# Generated from Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,89,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,12,4,12,79,8,12,11,12,12,12,80,1,13,4,13,84,8,13,
        11,13,12,13,85,1,13,1,13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,25,13,27,14,1,0,2,2,0,65,90,97,122,3,0,
        9,10,13,13,32,32,90,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,1,29,1,0,0,0,3,31,1,0,0,0,5,36,1,0,0,0,7,40,1,0,0,0,9,43,1,0,
        0,0,11,47,1,0,0,0,13,51,1,0,0,0,15,54,1,0,0,0,17,56,1,0,0,0,19,59,
        1,0,0,0,21,65,1,0,0,0,23,73,1,0,0,0,25,78,1,0,0,0,27,83,1,0,0,0,
        29,30,5,97,0,0,30,2,1,0,0,0,31,32,5,115,0,0,32,33,5,111,0,0,33,34,
        5,109,0,0,34,35,5,101,0,0,35,4,1,0,0,0,36,37,5,116,0,0,37,38,5,104,
        0,0,38,39,5,101,0,0,39,6,1,0,0,0,40,41,5,97,0,0,41,42,5,110,0,0,
        42,8,1,0,0,0,43,44,5,97,0,0,44,45,5,110,0,0,45,46,5,100,0,0,46,10,
        1,0,0,0,47,48,5,98,0,0,48,49,5,117,0,0,49,50,5,116,0,0,50,12,1,0,
        0,0,51,52,5,111,0,0,52,53,5,114,0,0,53,14,1,0,0,0,54,55,5,46,0,0,
        55,16,1,0,0,0,56,57,5,115,0,0,57,58,5,111,0,0,58,18,1,0,0,0,59,60,
        5,100,0,0,60,61,5,111,0,0,61,62,5,110,0,0,62,63,5,32,0,0,63,64,5,
        116,0,0,64,20,1,0,0,0,65,66,5,100,0,0,66,67,5,111,0,0,67,68,5,101,
        0,0,68,69,5,115,0,0,69,70,5,110,0,0,70,71,5,32,0,0,71,72,5,116,0,
        0,72,22,1,0,0,0,73,74,5,110,0,0,74,75,5,111,0,0,75,76,5,116,0,0,
        76,24,1,0,0,0,77,79,7,0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,
        0,0,0,80,81,1,0,0,0,81,26,1,0,0,0,82,84,7,1,0,0,83,82,1,0,0,0,84,
        85,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,6,13,
        0,0,88,28,1,0,0,0,3,0,80,85,1,6,0,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    WORD = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'a'", "'some'", "'the'", "'an'", "'and'", "'but'", "'or'", 
            "'.'", "'so'", "'don t'", "'doesn t'", "'not'" ]

    symbolicNames = [ "<INVALID>",
            "WORD", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "WORD", "WS" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


