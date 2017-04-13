:- consult(io).
:- dynamic es_un/2.
:- discontiguous entender_afirmacion/3.
:- discontiguous entender/2.

append(P1,P2,P3,P4,L):-
	append(P1,X,L),
	append(P2,Y,X),
	append(P3,P4,Y).

universal(todo).
universal(un).
universal(los).
verbo_ser(es).
verbo_ser(son).

conversar :-
    leer_oracion(L),
    entender(L,A),
    (A=continuar ->
        conversar
	;
	true).

entender(O,continuar) :-
	append(Sujeto,[Verbo],Predicado,['.'],O),
    entender_afirmacion(Sujeto,Verbo,Predicado),
    write('entiendo.'),nl.

entender(O,continuar) :-
    O=['que','es',X,'?'],
	Consulta = es_un(X,Clase),
    findall(Clase,Consulta,L),
    (L\=[]->
    write(X),write(' es '),pretty_print(L),write('.'),nl;
    write('no se quien es '),write(X),write('.'),nl).

entender(O,continuar) :-
    O=['quienes','son',Clase,'?'],
    Consulta=es_un(X,Clase),
    findall(X,Consulta,L),
    (L\=[]->
    pretty_print(L),write(' son '),write(Clase),write('.'),nl;
    write('No conozco ningun '),write(Clase),write('.'),nl).







agregar_regla(X, Relacion, Y) :-
    Cabeza =.. [Relacion, Z, W],
    Cola1 = es_un(Z,X),
    Cola2 = es_un(W,Y),
    assertz((Cabeza:-(Cola1,Cola2))),
    dynamic((Cabeza:-(Cola1,Cola2))).

agregar_trans(Relacion) :-
    atom_concat(aux_,Relacion,Faaax),
    Rev =.. [Faaax, G,H],
    ((not(current_predicate(_, Rev)))->
    (atom_concat(aux_,Relacion,Ax),
    Aa =.. [Ax,A,B], Bb =.. [Relacion,A,B],
    Cc =.. [Ax,A,C], Dd =.. [Relacion,B,C], Ee =.. [Ax,A,B],
    dynamic(Aa), dynamic(Cc),
    assert(Aa:-Bb),
    assert((Cc:-(Dd,Ee))));write('')).

entender_afirmacion(Sujeto,Verbo,Predicado) :-
    (Sujeto=['Los',X]; Sujeto=['los',X]),
    Verbo='son',
    Predicado=[Relacion, 'que', 'los', Y],
    Aux =.. [X,'Z'],
    Auxi =.. [Y,'W'],

    atom_concat(aux_,Relacion,Faux),
    Aaa =.. [Faux,Q,R], Bbb =.. [Relacion,Q,R],
    Rev = (Aaa:-Bbb),

    ((current_predicate(_, Aux), current_predicate(_, Auxi))->
    (agregar_regla(X, Relacion, Y)),(agregar_trans(Relacion)); 
    (write("No "))).




entender(O,continuar) :-
    (O=['quien','es',Relacion,'?']; O=['Quien','es',Relacion,'?']),
    atom_concat(aux_,Relacion,Revaux),
    RDOSaux =.. [Revaux, U, P],
    (current_predicate(_, RDOSaux)->
    findall(U,RDOSaux,Ll),findall(P,RDOSaux,Hh),
    mostrar1(Ll,Hh,Relacion);
    write('No conozco nadie '),write(Relacion),write('.'),nl).

mostrar1(L,H,R) :-
    (L\=[], H\=[]->
    L = [E|M],
    H = [F|N],
    write(E),write(' es '),write(R),write(' que '),write(F),write('.'),nl,
    mostrar2(M,N,R); write('')).

mostrar2(L,H,R) :-
    (L\=[], H\=[]->
    L = [E|M],
    H = [F|N],
    write(E),write(' es '),write(R),write(' que '),write(F),write('.'),nl,
    mostrar1(M,N,R); write('')).








entender([chao,'.'],parar) :-
    write('Conversemos otro dia.'),nl.

entender(_,continuar) :-
    write('No entiendo.'),nl.

entender_afirmacion(Sujeto,Verbo,Predicado) :-
    Sujeto=[Objeto],
    verbo_ser(Verbo),
    Predicado=[un,Clase],
	Cabeza=es_un(Objeto,Clase),
    assert(Cabeza),
    Aux =.. [Clase, Objeto],
    assert(Aux).

entender_afirmacion(Sujeto,Verbo,Predicado) :-
    Sujeto=[Todo,SubClase],universal(Todo),
    verbo_ser(Verbo),
    Predicado=[un,Clase],
	Cabeza = es_un(X,Clase),
	Cola = es_un(X,SubClase),
    assert((Cabeza:-Cola)).
	

pretty_print([X]) :-
    write(X).

pretty_print([X|L]) :-
    write(X), pretty_print_commas(L).

pretty_print_commas([X]) :-
    write(' y '),write(X).

pretty_print_commas([X,Y|L]) :-
    write(', '),write(X),pretty_print_commas([Y|L]).

