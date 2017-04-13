
% Predicados para leer una oracion

terminacion(X) :- member(X,['.','!','?']).

puntuacion(X) :- member(X,[46, 44, 58, 59, 63, 33]).

%puntuacion(X) :- member(X,".,:;?!").

char_valido(I) :- I > 96, I < 123.
char_valido(I) :- I > 64, I < 91.
char_valido(I) :- I > 47, I < 58.


leer_oracion([Primera_palabra|Lw]) :-
	get0(C),
	leer_palabra(C, Primera_palabra, C1),
	resto_oracion(Primera_palabra, C1, Lw), !.

resto_oracion(W,_,[]) :-
	terminacion(W), !.

resto_oracion(_, C, [W1|Lw]) :-
	leer_palabra(C,W1,C1),
	resto_oracion(W1,C1,Lw).


leer_palabra(C,W,C1) :-
	puntuacion(C),
	!,
	name(W,[C]),
	get0(C1).

leer_palabra(C,W,C1) :-
	char_valido(C),
	!,
	get0(C2),
	resto_palabra(C2, Lc, C1),
	name(W,[C|Lc]).

leer_palabra(_,W,C1) :-
	get0(C2),
	leer_palabra(C2,W,C1).


resto_palabra(C,[C|Lc], C1) :-
	char_valido(C),
	!,
	get0(C2),
	resto_palabra(C2,Lc,C1).

resto_palabra(C,[],C).




