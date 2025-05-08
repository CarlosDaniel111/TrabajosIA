sistema_experto:-
writeln("Sistema Experto para el Diagnostico de Enfermedades Respiratorias"),
hipotesis(Enfermedad),
write('Tu diagnostico es: '),
writeln(Enfermedad),
deshacer,!.

/*Hipotesis que deberia ser probada*/
hipotesis(resfriado_Comun) :- resfriado_Comun.
hipotesis(gripe) :- gripe.
hipotesis(bronquitis_Aguda) :- bronquitis_Aguda.
hipotesis(neumonia) :- neumonia.
hipotesis(asma) :- asma.
hipotesis(covid_19) :- covid_19.
hipotesis(rinitis_Alergica) :- rinitis_Alergica.
hipotesis(sinusitis) :- sinusitis.
hipotesis(faringitis) :- faringitis.
hipotesis(tuberculosis_Pulmonar) :- tuberculosis_Pulmonar.
hipotesis(desconocido).

/*Reglas de identificacion*/
resfriado_Comun :-
    antiverificar(tiene_fiebre), /*A*/
	verificar(tiene_congestion_nasal), /*B*/
    verificar(presenta_estornudos_frecuentes), /*C*/
    verificar(tiene_dolor_garganta), /*D*/
    verificar(presenta_tos_ocasional), /*E*/
    antiverificar(hay_dolor_de_cabeza), /*K*/
    verificar(tiene_sintomas_menores_a_2_semanas), /*F*/
    antiverificar(tiene_dificultad_respiratoria), /*R*/
    antiverificar(tiene_perdida_de_olfato), /*e*/
    antiverificar(presenta_dolores_musculares), /*H*/
	writeln('').

gripe :-
	verificar(tiene_fiebre), /*A*/
    verificar(presenta_dolores_musculares), /*H*/
    verificar(hay_escalofrios), /*I*/
    verificar(tiene_tos_persistente), /*J*/
    verificar(tiene_dolor_garganta), /*D*/
    verificar(hay_dolor_de_cabeza), /*K*/
    verificar(cuenta_con_fatiga), /*L*/
    verificar(tiene_sintomas_menores_a_2_semanas), /*F*/
    verificar(tiene_congestion_nasal), /*B*/
	writeln('').

bronquitis_Aguda :-	
	verificar(tiene_tos_persistente), /*J*/
    verificar(presenta_produccion_de_esputo_claro_o_amarillo), /*N*/
    verificar(tiene_molestias_en_el_pecho_al_toser), /*O*/
    antiverificar(tiene_fiebre), /*A*/
    verificar(cuenta_con_antecedentes_recientes_de_infeccion_viral), /*Q*/
	verificar(tiene_dificultad_respiratoria), /*R*/
    verificar(tiene_ausculacion_con_roncus), /*S*/
    antiverificar(tiene_perdida_de_olfato), /*e*/
	writeln('').

neumonia :-
	verificar(tiene_fiebre), /*A*/
    verificar(presenta_produccion_de_esputo_claro_o_amarillo), /*N*/
    verificar(tiene_dolor_toracico), /*U*/
    verificar(tiene_dificultad_respiratoria), /*R*/
    verificar(hay_escalofrios), /*I*/
    verificar(tiene_taquipnea), /*V*/
    verificar(cuenta_con_fatiga), /*L*/
    verificar(tiene_auscultacion_con_crepitaciones), /*W*/
	verificar(en_la_radiografia_presenta_infiltrado_pulmonar), /*X*/
    verificar(tiene_sintomas_menores_a_2_semanas), /*F*/
	writeln('').

asma :-
	verificar(tiene_dificultad_respiratoria), /*R*/
    verificar(tiene_silbidos_ocasionales), /*P*/
    verificar(tiene_tos_persistente), /*J*/
    antiverificar(tiene_fiebre), /*A*/
    verificar(empeora_con_clima_frio), /*Z*/
	verificar(tiene_antecedentes_con_alergia), /*a*/
	verificar(tiene_capacidad_pulmonar_reducida), /*b*/
	verificar(inicio_en_temprana_edad), /*c*/
	writeln('').

covid_19 :-
	verificar(tiene_fiebre), /*A*/
    verificar(tiene_tos_persistente), /*J*/
    verificar(tiene_perdida_de_olfato), /*e*/
    verificar(tiene_dolor_garganta), /*D*/
    verificar(tiene_congestion_nasal), /*B*/
    verificar(presenta_diarrea), /*f*/
    verificar(hay_dolor_de_cabeza), /*K*/
	writeln('').

rinitis_Alergica :-	
	verificar(presenta_estornudos_frecuentes), /*C*/
    verificar(tiene_congestion_nasal), /*B*/
    verificar(tiene_secrecion_nasal_espesa), /*m*/
    verificar(tiene_picazon_en_ojos_y_nariz), /*h*/
    verificar(presenta_lagrimeo_constante), /*i*/
    antiverificar(tiene_fiebre), /*A*/
    verificar(tiene_antecedentes_con_alergia), /*a*/
    verificar(mejora_con_anthistaminicos), /*j*/
    antiverificar(tiene_sintomas_menores_a_2_semanas), /*F*/
	writeln('').

sinusitis :-	
	verificar(tiene_dolor_facial), /*l*/
    verificar(tiene_congestion_nasal), /*B*/
    verificar(tiene_secrecion_nasal_espesa), /*m*/
    antiverificar(tiene_fiebre), /*A*/
    verificar(hay_dolor_de_cabeza), /*K*/
    verificar(hay_presion_facial_al_inclinarse), /*n*/
    verificar(tiene_tos_persistente), /*J*/
    antiverificar(tiene_sintomas_menores_a_2_semanas), /*F*/
	writeln('').

faringitis :-
	verificar(tiene_dolor_garganta), /*D*/
    verificar(tiene_fiebre), /*A*/
    antiverificar(presenta_tos_ocasional), /*E*/
    verificar(tiene_las_amigdalas_inflamadas), /*p*/
	verificar(los_ganglios_del_cuello_estan_inflamados), /*q*/
	verificar(tiene_mal_aliento), /*r*/
    verificar(tiene_dolor_garganta), /*D*/
	writeln('').

tuberculosis_Pulmonar :-
	verificar(tiene_tos_persistente), /*J*/
    verificar(tiene_esputo_con_sangre_ocasional), /*t*/
    verificar(tiene_fiebre), /*A*/
    verificar(hay_sudoracion_nocturna), /*u*/
    verificar(cuenta_con_fatiga), /*L*/
    verificar(su_radiografia_muestra_lesiones_cavitadas), /*v*/
	writeln('').

preguntar(Pregunta) :-
write('Sintoma: '),
write(Pregunta),
write('? '),
read(Respuesta),
nl,
((Respuesta == si) -> assert(si(Pregunta)) ;
assert(no(Pregunta)), fail).

anti_preguntar(Pregunta) :-
write('Sintoma: '),
write(Pregunta),
write('? '),
read(Respuesta),
nl,
((Respuesta == no) -> assert(no(Pregunta)) ;
assert(si(Pregunta)), fail).

:- dynamic si/1,no/1.

/*Como se verifica */
verificar(S) :-
(si(S) -> true ;
(no(S) ->fail ;
preguntar(S))).

antiverificar(S) :-
(no(S) -> true ;
(si(S) -> fail ;
anti_preguntar(S))).


/* deshacer all si/no assertions*/
deshacer :- retract(si(_)),fail.
deshacer :- retract(no(_)),fail.
deshacer.