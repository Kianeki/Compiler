grammar calc;

start       : (expression SEMICOLON)* EOF
            ;
expression  : (var|declaration|assignment)                          #vadExp
            | expression (MUL|DIV) expression                       #infixExp
            | expression (PLUS|MINUS) expression                    #infixExp
            | unaryOperation var                                    #unaryExp
            | expression (relOperation|logicOperation) expression   #relogicExp
            | (MINUS|PLUS)? LPAREN expression RPAREN                #parenthesesExp
            | number                                                #numberExp
            | printf                                                #printExp
            | char                                                  #charExp
            | string                                                #stringExp
            ;
printf      : 'printf' LPAREN (var|number) RPAREN
            ;
pointer     : (RESERVED '*')
            ;
declaration : (pointer|RESERVED)? var
            ;
assignment  : (ID|declaration) '=' expression
            ;
relOperation: LT|GT|EQ
            ;
logicOperation: AND|OR
            ;
unaryOperation: NOT|'*'|'&'
            ;
var         : (PLUS|MINUS)? ID
            ;
number      : (PLUS|MINUS)? (INT|FLOAT)
            ;



RESERVED : 'char'|'float'|'int';
ID  : ([a-zA-Z]|'_') (DIGIT|[a-zA-Z]|'_')* ;
ID2 : ('a'..'z' | 'A'..'Z')+ ;
//testdeel
SQ : '\'';
DQ : '\"';
char        : SQ .? SQ
            ;
string      : DQ .? DQ
            ;
//

LPAREN : '(';
RPAREN : ')';
SEMICOLON : ';';
PLUS: '+';
MINUS : '-';
MUL : '*';
DIV : '/';
LT  : '<';
GT  : '>';
EQ  : '==';
AND : '&&';
OR : '||';
NOT : '!';
FLOAT : DIGIT+ '.' DIGIT+
      | '.' DIGIT+
      ;
INT : DIGIT+;
DIGIT : [0-9];
ML_COMMENT: '/*' .*? '*/' -> skip;
SL_COMMENT: '//' .*? '\n' -> skip;
WS: [ \n\t\r]+ -> skip;