grammar yapl;

program: ( classkey ';')+ EOF;

classkey: CLASS TYPE (INHERITS TYPE)? '{' (feature ';')* '}';

feature: (
		ID '(' (formal (',' formal)*)* ')' ':' TYPE '{' expression '}'
	)
	| formal ('<-' expression)?;

formal: ID ':' TYPE;

expression:
	expression ('@' TYPE)? '.' ID '(' (
		expression (',' expression)*
	)* ')'
	| IF expression THEN expression ELSE expression FI
	| ID '(' (expression (',' expression)*)* ')'
	| WHILE expression LOOP expression POOL
	| expression ('*' | '/') expression
	| expression ('+' | '-') expression
	| expression '<-' expression
	| '{' (expression ';')+ '}'
	| expression '<=' expression
	| expression '=>' expression
	| expression '=' expression
	| expression '<' expression
	| ID '<-' expression
	| ISVOID expression
	| '~' expression
	| NOT expression
	| '(' expression ')'
	| NEW TYPE
	| STRING
	| FALSE
	| TRUE
	| INT
	| ID;

// Palabras reservadas
CLASS: 'class';
ELSE: 'else';
FI: 'fi';
IF: 'if';
IN: 'in';
INHERITS: 'inherits';
LOOP: 'loop';
POOL: 'pool';
THEN: 'then';
WHILE: 'while';
NEW: 'new';
ISVOID: 'isvoid';
NOT: 'not';
TRUE: 'true';
FALSE: 'false';

// Expecificaciones lexicas
STRING:
	'"' (
		(
			'\\' (
				["\\/bfnrt]
				| (
					'u' [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F]
				)
			)
		)
		| ~ ["\\]
	)* '"';
INT: [0-9]+;
TYPE: [A-Z][_0-9A-Za-z]*;
ID: [a-z][_0-9A-Za-z]*;

// Omisiones

WHITESPACE: [ \t\r\n\f]+ -> skip;
BLOCK_COMMENT:
	'(*' (BLOCK_COMMENT | .)*? '*)' -> channel(HIDDEN);
LINE_COMMENT: '--' .*? '\n' -> channel(HIDDEN);