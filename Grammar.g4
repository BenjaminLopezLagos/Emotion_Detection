grammar Grammar;

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
/*subject: WORD;
verb: WORD;
object: WORD;
adjective: 'so';
adverb: WORD;
noun: WORD;
*/
