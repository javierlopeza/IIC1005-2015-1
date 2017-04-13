suma(0,X,X).
suma(s(X),Y,Z) :- suma(X,s(Y),Z).

menor(X,Y) :- aDecimal(X,A), aDecimal(Y,B), A < B.

aDecimal(0,0).
aDecimal(s(X),Y) :- aDecimal(X,Z), Y is Z+1.

suma_l([X],X).
suma_l([X|Y],S) :- suma_l(Y,Ss), suma(X,Ss,S).

lista_divisores(N,L) :- divisor(N,s(0),L).
divisor(N,N,[]).
divisor(N,Pd,[Pd|T]) :- aDecimal(N,A), aDecimal(Pd,B), A>B, 0 is A mod B, suma(Pd,s(0),PdN), divisor(N,PdN,T).
divisor(N,Pd,L) :- aDecimal(N,A), aDecimal(Pd,B), A>B, not(0 is A mod B), suma(Pd,s(0),PdN), divisor(N,PdN,L).

suma_divisores(N,S) :- lista_divisores(N,L), suma_l(L,S).

abundante(N) :- suma_divisores(N,SD), menor(N,SD).