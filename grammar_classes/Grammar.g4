grammar Grammar;
/*
WORD: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
sentence: (subject negation? verb negation? article? adjective? (object)? point)+;
subject: WORD;
object: WORD;
verb: WORD;
article:'a'|'some'|'the'|'an' ;
conjuntion: 'and'|'but'| 'or';
point:'.';
adjective: 'so';
negation: 'don t'|'doesn t'| 'not';
*/
start: (s (CONJUNCTION s)* DOT)+;
s: (np vp | vp);
np: PRONOUN | PROPERNOUN | DETERMINER nominal | np CONJUNCTION np;
nominal: NOUN nominal | NOUN | ADJECTIVE nominal;
// VERB ((ADVERB)* (ADJECTIVE)*) puede cambiar
vp:  VERB ((ADVERB)* (ADJECTIVE)*) | VERB np | VERB np pp | VERB pp | vp CONJUNCTION vp | VERB s;
pp: PREPOSITION np;

PRONOUN: 'PRP' | 'PRP$';
PROPERNOUN: 'NNP' | 'NNPS';
DETERMINER: 'DT';
PREPOSITION: 'IN' | 'TO';
CONJUNCTION: 'CC';
ADJECTIVE: 'JJ' | 'JJR' | 'JJS';
NOUN: 'NN' | 'NNS';
ADVERB: 'RB' | 'RBR' | 'RBS';
VERB: 'VB' | 'VBD' | 'VBG' | 'VBN' | 'VBP' | 'VBZ';
DOT: '.';
WS: [ \t\r\n]+ -> skip;

/*subject: WORD;
verb: WORD;
object: WORD;
adjective: 'so';
adverb: WORD;
noun: WORD;
*/
