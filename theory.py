#Pasar de present perfect a perfect present en la estructuras básicas (confirmar)

from asyncore import write
from ctypes import pointer

def main_theory():
    print("----------------------------")
    print("#1: Normal execution")
    print("#2: Run from the numbers")
    print("#3: Run from the months")
    print("#4: Run from the basic sentence structure")
    print("#5: Run from the simple rules")
    print("#6: Run from the noun subject")
    print("#7: Run from the pronouns")
    print("#8: Run from the article")
    print("#9: Run from the adjective")
    print("#10: Run from the verb")
    print("#11: Run from the verb auxilary")
    print("----------------------------")
    selection_option=input("selection an option: ")

    if(selection_option=="1"):
        abecedary()
        numbers()
        months()
        basic_sentence_structure()  
        simple_rules()
        noun_subject()
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="2"):
        numbers()
        months()
        basic_sentence_structure() 
        simple_rules()
        noun_subject()
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb() 
    elif(selection_option=="3"):
        months()
        basic_sentence_structure()  
        simple_rules()
        noun_subject()
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="4"):
        basic_sentence_structure()
        simple_rules()
        noun_subject()
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="5"):
        simple_rules()
        noun_subject()
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="6"):
        noun_subject()
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="7"):
        pronouns()
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="8"):
        articles()
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="9"):
        adjective()
        verb()
        aux_verb()
    elif(selection_option=="10"):
        verb()
        aux_verb()
    elif(selection_option=="11"):
        aux_verb() 

def recorrer_lista(list_test):    
    for x in list_test:
        print(x)

def list_correct_abecedary():
    print()
    print("letter--pronunciation")
    print("A--ei")
    print("B--bi")
    print("C--ci")
    print("D--di")
    print("E--i")
    print("F--ef")
    print("G--yi")
    print("H--eich")
    print("I--ai")
    print("J--jei")
    print("K--kei")
    print("L--el")
    print("M--em")
    print("N--en")
    print("O--ou")
    print("P--pi")
    print("K--kiu")
    print("R--er")
    print("S--es")
    print("T--ti")
    print("U--iu")
    print("V--vi")
    print("W--dabliu")
    print("X--ex")
    print("Y--uai")
    print("Z--set")

def list_correct_numbers():
    print()
    print("#--número--number")
    print("0--cero--zero")
    print("1--uno--one")
    print("2--dos--two")
    print("3--tres--three")
    print("4--cuatro--four")
    print("5--cinco--five")
    print("6--seis--six")
    print("7--siete--seven")
    print("8--ocho--eight")
    print("9--nueve--nine")
    print("10--diez--ten")
    print("11--once--eleven")
    print("12--doce--twelve")
    print("13--trece--thirteen")
    print("14--catorce--fourteen")
    print("15--quince--fiveteen")
    print("16--diesiseis--sixteen")
    print("17--diesisiete--seventeen")
    print("18--diesiocho--eighteen")
    print("19--diesinueve--nineteen")
    print("20--veinte--twenty")
    print("25--veinticinco--twenty-five")
    print("30--treinta--thirty")
    print("35--teinta y cinco--thirty-five")
    print("40--cuarenta--forty")
    print("45--cuarenta y cinco--forty-five")
    print("50--cincuenta--fifty")
    print("55--cincuenta y cinco--fifty-five")
    print("60--sesenta--sixty")
    print("65--sesenta y cinco--sixty-five")
    print("70--setenta--seventy")
    print("75--setenta y cinco--seventy-five")
    print("80--ochenta--eighty")
    print("85--ochenta y cinco--eighty-five")
    print("90--noventa--ninety")
    print("95--noventa y cinco--ninety-five")
    print("100--cien--one hundred")
    print("105--ciento cinco--one hundred and five")
    print("110--ciento diez--one hundred and ten")
    print("200--docientos--two hundred")
    print("205--docientos cinco--two hundred and five")
    print("210--docientos diez--two hundred and ten")
    print("300--trecientos--three hundred")
    print("305--trecientos cinco--three hundred and five")
    print("310--trecientos diez--three hundred and ten")
    print("400--cuatrocientos--four hundred")
    print("405--cuatrocientos cinco--four hundred and five")
    print("410--cuatrocientos diez--four hundred and ten")
    print("500--quinientos--five hundred")
    print("505--quinientos cinco--five hundred and five")
    print("510--quinientos diez--five hundred and ten")
    print("600--seisientos--six hundred")
    print("605--seisientos cinco--six hundred and five")
    print("610--seisientos diez--six hundred and ten")
    print("700--setecientos--seven hundred")
    print("705--setecientos cinco--seven hundred and five")
    print("710--setecientos diez--seven hundred and ten")
    print("800--ochocientos--eight hundred")
    print("805--ochocientos cinco--eight hundred and five")
    print("810--ochocientos diez--eight hundred and ten")
    print("900--novecientos--nine hundred ")
    print("905--novecientos cinco--nine hundred and five")
    print("910--novecientos diez--nine hundred and ten")
    print("1.000--mil--one thousand")
    print("1.005--mil cinco--one thousand five")
    print("1.010--mil diez--one thousand ten")
    print("1.100--mil cien--one thousand one hundred")
    print("10.000--diez mil--ten thousand")
    print("10.005--diez mil cinco--ten thousand and five")
    print("10.010--diez mil diez--ten thousand and ten")
    print("10.100--diez mil cien--the thousand and one hundred")
    print("100.000--cien mil--one hundred thousand")
    print("100.005--cien mil cinco--one hundred thousand and five")
    print("100.010--cien mil diez--one hundred thousand and ten")
    print("100.100--cien mil cien--one hndred thousand one hundred")
    print("1.000.000--un millon--one million")
    print("10.000.000--diez millones--ten million")
    print("100.000.000--cien millones--one hundred million")
    print("1.000.000.000--mil millones(Col)/un billon(usa)--one billion")
    print()

def correct_list_test_noun_subject():
    print()
    print('lista correcta del test noun_subject')
    print('spanish--english--pronunciation')
    print('corner--esquina')
    print('cousin--esposo')
    print('umbrella--sombrilla')
    print('rubbish--basura')
    print('trash--basura(music)')
    print('glasses--gafas')
    print('glass--vidrio/vaso/copa')
    print('rings--aro')
    print('countryside--campo')
    print('drought--sequía')
    print('relics--reliquias')
    print('footprints--huellas')
    print('layers--capas')
    print('sediment--sedimiento')
    print('clay--arcilla')
    print('downtown--centro')
    print('integers--enteros')
    print('current--actual')
    print('lot--lote/terreno')
    print('everything--todo')
    print('parent--padre/progenitor')
    print('ownership--propiedad/posesión')
    print('constraint--restrinción/limitación')
    print('target--objetivo/proposito/meta')
    print('frame--marco/estructura')
    print('patterns--patrones/estampados/adorno')
    print('chart--gráfica/historia medica/ranking')
    print('layout--diseño')
    print('wheel--rueda')
    print('lightness--claridad')
    print('shade--sombra/oscuridad')
    print('degree--grado')
    print('light--luz')
    print('sense--sentido/juicio/sentido(rational thinking)/presentimiento/sensación')
    print('edge--borde/ventaja')
    print('account--cuenta')
    print('nuance--matiz/tonalidad')
    print('bulb--bombilla/canaleta')
    print('landscape--panorma/vista/paisaje')
    print('deal--acuerdo/trato')
    print('gutter--alcantarilla/canaleta')
    print('brethren--hermanos')
    print('vendor--comerciante/vendedor(a)')
    print('draft--borrador/boceto/bosquejo/corriente/cerveza de barril/caña/jarra')
    print('nast--nido')
    print('feature--característica/distintivo/rasgo')
    print('parther--socio/socia/pareja/compañero(a)')
    print('bunch--racismo/agrupar/amontonar')
    print('ellipsis--puntos suspensivos')
    print('spot--mancha/granito/lugar(informal)/sitio(informal)/roncha')
    print('stitch--punto/puntada/pinchazo')
    print('sitting--sesión/horario/turno/periodo')
    print('brunch--almuerzo/desayuno armuerzo')
    print('portrait--retrato')
    print('couple--par/pareja')
    print('gap--hueco/espacio/intervalo/interrupción/lapso')
    print('spring--primavera')
    print('heir--heredero')
    print("--")

def list_correct_adjective():
    print()
    print("Adjectives:")
    print("angry--enojado")
    print("happy--feliz")
    print("sad--triste")
    print("thoughtful--considerado/atento")
    print("arrogant--creído")
    print("ambitious--ambicioso")
    print("smooth--liso")
    print("bumpy--irregular//con baches/con hoyos")
    print("soft--blando/suave")
    print("spicy--picante")
    print("sweet--dulce")
    print("sour--agrio/ácido")
    print("remaining--restante")
    print("lightweight--liviano/ligero/peso ligero/de poco peso/persona que se emborracha fácilmente/pelagatos/don nadie")
    print("wanting--deficiente/insuficiente")
    print("spent--gastado/vacío/usado")
    print("able--poder/capaz/talenotos(a)")
    print("silly--tonto(a)/bobo(a)/absurdo(a)")
    print("funky--en la onda/en la moda/apestosó(a)/fétido(a)")
    print("halfway--por la mitad/a medias")
    print("further--más lejos/más lejano/más extenso/más a fondo")    
    print("enough--suficiente/bastante/")
    print("feasible--viable/factible/probable")
    print("bold--vailiente/audaz/atrevido/")
    print("paid--pagado/pago(a)/remunerado")
    print("nested--anidado/dentro de una cosa/alojado")
    print("tricky--complicado(a)/delicado(a)/que tiene su maña/difícil/complicado(a)/tramposo(a)/falso(a)")
    print("fixed--fijo(a)/inamovible/inalterable/reparado/areglado(a)/")    
    print("desired--deseado/anhelado/apropiado(a)")
    print("overlapping--superpuesto/solapado(a)")
    print("pretty--bonito(a)/lindo(a)/precioso(a)/guapo(a)")
    print("narrow--angosto/estrecho/corto/reducido")    
    print("accurate--preciso(a)/exato(a)/certero(a)/riguroso(a)/acertado(a)")
    print("meaningful--significativo(a)")
    print("deep--profundo/hondo/grave")
    print("unexpected--inesperado(a)/imprevisto(a)")
    print("related--relacionado/familiar/pariente")
    print("entire--entero(a)/todo(a)")    
    print("several--varios/varias")
    print("readable--ameno(a)/entrenido(a)/legible")
    print("another--otro/distinto")
    print("whole--entero/total/todo/completo")    
    print("complex--complicado/complejo")
    print("those--aquellos/esos/esas")
    print("shortest--mas bajo/más corto")
    print("subtle--sutil/disimulado/desimulada")    
    print()

def list_correct_adverb():
    print()
    print("Adverb place")
    print("aquí--here")
    print("ahí--there")
    print("allí--there")
    print("cerca--near")
    print("lejos--far")
    print("arriba--up")
    print("abajo--down")
    print("adentro--inside")
    print("afuera--outside")
    print("")
    print("Adverb time")
    print("ahora--now")
    print("luego--then")
    print("después--after")
    print("pronto--promptly")
    print("tarde--late")
    print("ayer--yesterday")
    print("hoy--today")
    print("mañana--tomorrow")
    print("")
    print("Adverb mode")
    print("bien--well")
    print("mal--wrong")
    print("así--so")
    print("deprisa--fast")
    print("despacio--slowly")
    print("")
    print("Adverb amount")
    print("mucho--much")
    print("poco--little")
    print("bastante--quite")
    print("casi--almost")
    print("más--more")
    print("menos--less")
    print("muy--very")
    print("")
    print("Adverb affirmation")
    print("sí--yes")
    print("also--también")
    print("")
    print("Adverb denial")
    print("no--no")
    print("tampoco--either")
    print("")
    print("Adverb doubt")
    print("quizás--possibly/maybe")
    print("acaso--perhaps")

def list_correct_basic_sentence_strcture():
    print()
    print("question---answer")
    print("what the basic sentence structure?---subject+verb+object")
    print()
    list_correct_simple_rules()
    print()
    print("what is a subject?---a subject is a part of a sentence that contains the person or thing performing the action in a sentence")
    correct_list_test_noun_subject()
    print("what are pronouns?--pronouns are the words we often use to talk about a person when we are not using their name")
    print()
    list_correct_adjective()
    print()
    print("what is a adverb?--an adverb is a word that modifies or describes a verb")
    list_correct_adverb()
    
def list_correct_months():
    print()
    print("Months:")
    print("january--enero-->31 days")
    print("february--febrero-->28 days-->leap-year 29 days")
    print("march--marzo-->31 days")
    print("april--abril-->30 days")
    print("may--mayo-->31 days")
    print("june--junio-->30 days")
    print("july--julio-->31 days")
    print("august--agosto-->31 days")
    print("september--septiembre-->30 days")
    print("october--octubre-->31 days")
    print("november--noviembre-->30 days")
    print("december--diciembre-->31 days")

def list_correct_simple_rules():
    print("SIMPLE RULES:")    
    print("noun-->object/place/animal/personal name")
    print("Mr-->señor/Sr")
    print("Mrs-->señora/Sra")
    print("pronouns-->i/you/he/she/it/we/you/they")
    print("pronoun 1st person singular-->i")
    print("pronoun 1st person plural-->we")
    print("pronoun 2nd person singular-->you")
    print("pronoun 2nd person plural-->you")
    print("pronoun 3rd person singular-->he/she/it")
    print("pronoun 3rd person plural-->they")
    print("adjective-->quality/characteristic --> form/size/color/origin")
    print("article-->define the noun--> a/an/the")
    print("noun and adjective rule-->adjective+noun")
    print("noun and article rule-->article+noun=subject")
    print("types of verb-->regulars and irregulars")
    print("#1 rule of the verb in the past-->ed is never pronounced")
    print("infinitive verb structure-->to+verb")
    print("gerund verb structure-->verb+ing")
    print("auxiliary verbs-->be/do/modals/have(perfect tenses)/verb to-be")
    print("adverbs-->describes the verb")
    print("frequency adverb--intensity/quantity --> always/often/normally/sometimes/never")
    print("prepositions-->time/place --> at/in/on/of/with/that/than/against")
    print("structure of the phrasal verb-->verb+preposition")
    print("time expresion-->today/tomorrow/yesterdaylast night")
    print("conjunctions/coordinators-->fanboys(for/and/nor/but/or/yet/so)")
    print("connectors-->preposition/conjunctions-coordinators(fanboys)")
    print("separate structures-->,/preposition/conjunctions-coordinators(fanboys)")
    print("rule voz pasiva--><--voz activa: passive voice to active voice and active voice to passive voice")
    print("structure of the simple present-->is/am/are+p.p(verb past participle)")
    print("structure of the simple past-->was/were+p.p(verb past participle)")
    print("structure of the simple future-->will be+p.p(verb past participle)")
    print("structure of the perfect present-->have/has been+p.p(verb past participle)")

def list_correct_verbs():
    ("List correct verbs: ")    
    ("verbo-->verb")
    print("preguntar --> ask")    
    print("ser/estar-->be")
    print("romper/quebrar-->break")
    print("llevar/traer/jalar/transladar/transportar-->bring")
    print("llamar-->call")
    print("llevar/cargar-->carry")
    print("chequear/verificar/comprobar/revisar-->check")
    print("cortar-->cut")
    print("venir/llegar/entrar/acercarse-->come")
    print("hacer-->do")
    print("caerse/dejar/caer-->drop")
    print("caerse/caer-->fall")
    print("llenar/rellenar/llenarse-->fill")
    print("encontrar/encontrarse-->find")
    print("conseguir/obtener/llegar-->get")
    print("pasar/dar/alcanzar-->give")
    print("irse/partir-->go")
    print("crecer-->grown")
    print("dar/pasar/entregar-->hand")
    print("exponer/colgar/ahorcar-->hang")
    print("agarrar/sostener/retener/tener-->hold")
    print("guardar/conservar/mantener-->keep")
    print("dejar/permitir-->let")
    print("registrar/anotar/talar/loguearse-->log")
    print("mirar-->look")
    print("hacer-->make")
    print("pasar-->pass")
    print("correr/recorrer-->run")
    print("ponerse/poner/colocar/ajustar-->set")
    print("poner/colocar-->put")
    print("escoger/coger/recolectar/recoger-->pick")
    print("pagar-->pay")
    print("decir/contar-->tell")
    print("girar/rotar-->turn")
    print("agarrar/coger/tomar-->take")
    print("hablar-->talk")
    print("trabajar-->work")
    print()

def list_correct_verbs_regular():
    print("List correct verbs regulars: ")
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Grabar-->record-->recorded-->recorded")
    
def abecedary():
    good=0
    vec_abe=["------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------"]
    print()
    print("ABECEDARY")    
    good=0
    letter_abe=input("write the letter [A] in english: ")
    if(letter_abe=="ei"):
        print("correct")
        good+=1
        vec_abe[0]="A"
    else:
        print("incorrect")
    letter_abe=input("write the letter [B] in english: ")
    if(letter_abe=="bi"):
        print("correct")
        good+=1
        vec_abe[1]="B"
    else:
        print("incorrect")
    letter_abe=input("write the letter [C] in english: ")
    if(letter_abe=="ci"):
        print("correct")
        good+=1
        vec_abe[2]="C"
    else:
        print("incorrect")
    letter_abe=input("write the letter [D] in english: ")
    if(letter_abe=="di"):
        print("correct")
        good+=1
        vec_abe[3]="D"
    else:
        print("incorrect")
    letter_abe=input("write the letter [E] in english: ")
    if(letter_abe=="i"):
        print("correct")
        good+=1
        vec_abe[4]="E"
    else:
        print("incorrect")
    letter_abe=input("write the letter [F] in english: ")
    if(letter_abe=="ef"):
        print("correct")
        good+=1
        vec_abe[5]="F"
    else:
        print("incorrect")
    letter_abe=input("write the letter [G] in english: ")
    if(letter_abe=="yi"):
        print("correct")
        good+=1
        vec_abe[6]="G"
    else:
        print("incorrect")
    letter_abe=input("write the letter [H] in english: ")
    if(letter_abe=="eich"):
        print("correct")
        good+=1
        vec_abe[7]="H"
    else:
        print("incorrect")
    
    letter_abe=input("write the letter [I] in english: ")
    if(letter_abe=="ai"):
        print("correct")
        good+=1
        vec_abe[8]="I"
    else:
        print("incorrect")
    letter_abe=input("write the letter [J] in english: ")
    if(letter_abe=="jei"):
        print("correct")
        good+=1
        vec_abe[9]="J"
    else:
        print("incorrect")
    letter_abe=input("write the letter [K] in english: ")
    if(letter_abe=="kei"):
        print("correct")
        good+=1
        vec_abe[10]="K"
    else:
        print("incorrect")
    letter_abe=input("write the letter [L] in english: ")
    if(letter_abe=="el"):
        print("correct")
        good+=1
        vec_abe[11]="L"
    else:
        print("incorrect")
    letter_abe=input("write the letter [M] in english: ")
    if(letter_abe=="em"):
        print("correct")
        good+=1
        vec_abe[12]="M"
    else:
        print("incorrect")
    letter_abe=input("write the letter [N] in english: ")
    if(letter_abe=="en"):
        print("correct")
        good+=1
        vec_abe[13]="N"
    else:
        print("incorrect")
    letter_abe=input("write the letter [O] in english: ")
    if(letter_abe=="ou"):
        print("correct")
        good+=1
        vec_abe[14]="O"
    else:
        print("incorrect")
    letter_abe=input("write the letter [P] in english: ")
    if(letter_abe=="pi"):
        print("correct")
        good+=1
        vec_abe[15]="P"
    else:
        print("incorrect")
    letter_abe=input("write the letter [Q] in english: ")
    if(letter_abe=="kiu"):
        print("correct")
        good+=1
        vec_abe[16]="Q"
    else:
        print("incorrect")
    letter_abe=input("write the letter [R] in english: ")
    if(letter_abe=="ar"):
        print("correct")
        good+=1
        vec_abe[17]="R"
    else:
        print("incorrect")
    
    letter_abe=input("write the letter [S] in english: ")
    if(letter_abe=="es"):
        print("correct")
        good+=1
        vec_abe[18]="S"
    else:
        print("incorrect")
    letter_abe=input("write the letter [T] in english: ")
    if(letter_abe=="ti"):
        print("correct")
        good+=1
        vec_abe[19]="T"
    else:
        print("incorrect")
    letter_abe=input("write the letter [U] in english: ")
    if(letter_abe=="iu"):
        print("correct")
        good+=1
        vec_abe[20]="U"
    else:
        print("incorrect")
    letter_abe=input("write the letter [V] in english: ")
    if(letter_abe=="vi"):
        print("correct")
        good+=1
        vec_abe[21]="V"
    else:
        print("incorrect")
    letter_abe=input("write the letter [W] in english: ")
    if(letter_abe=="dabliu"):
        print("correct")
        good+=1
        vec_abe[22]="W"
    else:
        print("incorrect")
    letter_abe=input("write the letter [X] in english: ")
    if(letter_abe=="ex"):
        print("correct")
        good+=1
        vec_abe[23]="X"
    else:
        print("incorrect")
    letter_abe=input("write the letter [Y] in english: ")
    if(letter_abe=="uai"):
        print("correct")
        good+=1
        vec_abe[24]="Y"
    else:
        print("incorrect")
    letter_abe=input("write the letter [Z] in english: ")
    if(letter_abe=="set"):
        print("correct")
        good+=1
        vec_abe[25]="Z"
    else:
        print("incorrect")
        
    print("Answers:")
    recorrer_lista(vec_abe)
    print(f"result: {good}/26")
    print()
    list_correct_abecedary()
    print()

def numbers():
    print()
    var_num=0
    vec_num=["----","----","----","----""----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----"]
    print("The numbers")
    str_13_to_19=input("What is structure of the numbers from 13 to 19?: ")
    if(str_13_to_19=="number+teen"):
        print("perfect")
        vec_num[0]="Structure 13 to 19"
        var_num+=1
    else:
        print("incorrect")
    print()

    str_rou_num=input("what is the structure of round numbers? ")
    if(str_rou_num=="number+ty"):
        print("correct")
        vec_num[1]="round numbers"
        var_num+=1
    else:
        print("incorrect")
    print()

    str_100_to_999=input("what is the structure of the numbers from 100 to 999?: ")
    if(str_100_to_999=="number+hundred"):
        print("correct")
        vec_num[2]="structure 100 to 999"
        var_num+=1
    else:
        print("incorrect")
    print()

    str_1000_to_999000=input("what is the structure of the numbers from 1.000 to 999.000?: ")
    if(str_1000_to_999000=="number+thousand"):
        print("correct")
        vec_num[3]="structure 1.000 to 999.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    str_1000000_to_999000000=input("what is the structure of the numbers from 1.000.000 to 999.000.000?: ")
    if(str_1000000_to_999000000=="number+million"):
        print("correct")
        vec_num[4]="structure 1.000.000 to 999.000.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    print()
    print("Answers:")
    print("What is structure of the numbers from 13 to 19?: number+teen")
    print("what is the structure of round numbers?: number+ty")
    print("what is the structure of the numbers from 100 to 999?: number+hundred")
    print("what is the structure of the numbers from 1.000 to 999.000?: number+thousand")
    print()
    
    num_zer=input("0 in english: ")
    if(num_zer=="zero"):
        print("correct")
        vec_num[5]="0"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one=input("1 in english: ")
    if(num_one=="one"):
        print("correct")
        vec_num[6]="1"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_two=input("2 in english: ")
    if(num_two=="two"):
        print("correct")
        vec_num[7]="2"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_three=input("3 in english: ")
    if(num_three=="three"):
        print("correct")
        vec_num[8]="3"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fou=input("4 in english: ")
    if(num_fou=="four"):
        print("correct")
        vec_num[9]="4"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fiv=input("5 in english: ")
    if(num_fiv=="five"):
        print("correct")
        vec_num[10]="5"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six=input("6 in english: ")
    if(num_six=="six"):
        print("correct")
        vec_num[11]="6"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_sev=input("7 in english: ")
    if(num_sev=="seven"):
        print("correct")
        vec_num[12]="7"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_eig=input("8 in english: ")
    if(num_eig=="eight"):
        print("correct")
        vec_num[13]="8"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_nin=input("9 in english: ")
    if(num_nin=="nine"):
        print("correct")
        vec_num[14]="9"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ten=input("10 in english: ")
    if(num_ten=="ten"):
        print("correct")
        vec_num[15]="10"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ele=input("11 in english: ")
    if(num_ele=="eleven"):
        print("correct")
        vec_num[16]="11"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_twe=input("12 in english: ")
    if(num_twe=="twelve"):
        print("correct")
        vec_num[17]="12"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_thi_t=input("13 in english: ")
    if(num_thi_t=="thirteen"):
        print("correct")
        vec_num[18]="13"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fou_t=input("14 in english: ")
    if(num_fou_t=="fourteen"):
        print("correct")
        vec_num[19]="14"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fif_t=input("15 in english: ")
    if(num_fif_t=="fiveteen"):
        print("correct")
        vec_num[20]="15"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six_t=input("16 in english: ")
    if(num_six_t=="sixteen"):
        print("correct")
        vec_num[21]="16"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_sev_t=input("17 in english: ")
    if(num_sev_t=="seventeen"):
        print("correct")
        vec_num[22]="17"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_eig_t=input("18 in english: ")
    if(num_eig_t=="eighteen"):
        print("correct")
        vec_num[23]="18"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_nin_t=input("19 in english: ")
    if(num_nin_t=="nineteen"):
        print("correct")
        vec_num[24]="19"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_twe_ty=input("20 in english: ")
    if(num_twe_ty=="twenty"):
        print("correct")
        vec_num[25]="20"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_twe_ty_fiv=input("25 in english: ")
    if(num_twe_ty_fiv=="twenty-five"):
        print("correct")
        vec_num[26]="25"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_thi_ty=input("30 in english: ")
    if(num_thi_ty=="thirty"):
        print("correct")
        vec_num[27]="30"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_thi_ty_fiv=input("35 in english: ")
    if(num_thi_ty_fiv=="thirty-five"):
        print("correct")
        vec_num[28]="35"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_for_ty=input("40 in english: ")
    if(num_for_ty=="forty"):
        print("correct")
        vec_num[29]="40"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_for_ty_fiv=input("45 in english: ")
    if(num_for_ty_fiv=="forty-five"):
        print("correct")
        vec_num[30]="45"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fif_ty=input("50 in english: ")
    if(num_fif_ty=="fifty"):
        print("correct")
        vec_num[31]="50"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fif_ty_fiv=input("55 in english: ")
    if(num_fif_ty_fiv=="fifty-five"):
        print("correct")
        vec_num[32]="55"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six_ty=input("60 in english: ")
    if(num_six_ty=="sixty"):
        print("correct")
        vec_num[33]="60"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six_ty_fiv=input("65 in english: ")
    if(num_six_ty_fiv=="sixty-five"):
        print("correct")
        vec_num[34]="65"
        var_num+=1
    else:
        print("incorrect")
    print()
    
    num_sev_ty=input("70 in english: ")
    if(num_sev_ty=="seventy"):
        print("correct")
        vec_num[35]="70"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_sev_ty_fiv=input("75 in english: ")
    if(num_sev_ty_fiv=="seventy-five"):
        print("correct")
        vec_num[36]="75"
        var_num+=1
    else:
        print("incorrect")
    print()
    
    num_eig_ty=input("80 in english: ")
    if(num_eig_ty=="eighty"):
        print("correct")
        vec_num[37]="80"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_eig_ty_fiv=input("85 in english: ")
    if(num_eig_ty_fiv=="eighty-five"):
        print("correct")
        vec_num[38]="85"
        var_num+=1
    else:
        print("incorrect")
    print()
    
    num_nin_ty=input("90 in english: ")
    if(num_nin_ty=="ninety"):
        print("correct")
        vec_num[39]="90"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_nin_ty_fiv=input("95 in english: ")
    if(num_nin_ty_fiv=="ninety-five"):
        print("correct")
        vec_num[40]="95"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun=input("100 in english: ")
    if(num_one_hun=="one hundred"):
        print("correct")
        vec_num[41]="100"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_and_fiv=input("105 in english: ")
    if(num_one_hun_and_fiv=="one hundred and five" or num_one_hun_and_fiv=="one hundred five"):
        print("correct")
        vec_num[42]="105"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_and_ten=input("110 in english: ")
    if(num_one_hun_and_ten=="one hundred and ten" or num_one_hun_and_ten=="one hundred ten"):
        print("correct")
        vec_num[43]="110"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_two_hun=input("200 in english: ")
    if(num_two_hun=="two hundred"):
        print("correct")
        vec_num[44]="200"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_two_hun_and_fiv=input("205 in english: ")
    if(num_two_hun_and_fiv=="two hundred and five" or num_two_hun_and_fiv=="two hundred five"):
        print("correct")
        vec_num[45]="205"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_two_hun_and_ten=input("210 in english: ")
    if(num_two_hun_and_ten=="two hundred and ten" or num_two_hun_and_ten=="two hundred ten"):
        print("correct")
        vec_num[46]="210"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_thr_hun=input("300 in english: ")
    if(num_thr_hun=="three hundred"):
        print("correct")
        vec_num[47]="300"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_three_hun_and_fiv=input("305 in english: ")
    if(num_three_hun_and_fiv=="three hundred and five" or num_three_hun_and_fiv=="three hundred five"):
        print("correct")
        vec_num[48]="305"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_three_hun_and_ten=input("310 in english: ")
    if(num_three_hun_and_ten=="three hundred and ten" or num_three_hun_and_ten=="three hundred ten"):
        print("correct")
        vec_num[49]="310"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fou_hun=input("400 in english: ")
    if(num_fou_hun=="four hundred"):
        print("correct")
        vec_num[50]="400"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fou_hun_and_fiv=input("405 in english: ")
    if(num_fou_hun_and_fiv=="four hundred and five" or num_fou_hun_and_fiv=="four hundred five"):
        print("correct")
        vec_num[51]="405"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fou_hun_and_ten=input("410 in english: ")
    if(num_fou_hun_and_ten=="four hundred and ten" or num_fou_hun_and_ten=="four hundred ten"):
        print("correct")
        vec_num[52]="410"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fiv_hun=input("500 in english: ")
    if(num_fiv_hun=="five hundred"):
        print("correct")
        vec_num[53]="500"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fiv_hun_and_fiv=input("505 in english: ")
    if(num_fiv_hun_and_fiv=="five hundred and five" or num_fiv_hun_and_fiv=="five hundred five"):
        print("correct")
        vec_num[54]="505"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_fiv_hun_and_ten=input("510 in english: ")
    if(num_fiv_hun_and_ten=="five hundred and ten" or num_fiv_hun_and_ten=="five hundred ten"):
        print("correct")
        vec_num[55]="510"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six_hun=input("600 in english: ")
    if(num_six_hun=="six hundred"):
        print("correct")
        vec_num[56]="600"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six_hun_and_fiv=input("605 in english: ")
    if(num_six_hun_and_fiv=="six hundred and five" or num_six_hun_and_fiv=="six hundred five"):
        print("correct")
        vec_num[57]="605"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_six_hun_and_ten=input("610 in english: ")
    if(num_six_hun_and_ten=="six hundred and ten" or num_six_hun_and_ten=="six hundred ten"):
        print("correct")
        vec_num[58]="610"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_sev_hun=input("700 in english: ")
    if(num_sev_hun=="seven hundred"):
        print("correct")
        vec_num[59]="700"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_sev_hun_and_fiv=input("705 in english: ")
    if(num_sev_hun_and_fiv=="seven hundred and five" or num_sev_hun_and_fiv=="seven hundred five"):
        print("correct")
        vec_num[60]="705"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_sev_hun_and_ten=input("710 in english: ")
    if(num_sev_hun_and_ten=="seven hundred and ten" or num_sev_hun_and_ten=="seven hundred ten"):
        print("correct")
        vec_num[61]="710"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_eig_hun=input("800 in english: ")
    if(num_eig_hun=="eight hundred"):
        print("correct")
        vec_num[62]="800"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_eig_hun_and_fiv=input("805 in english: ")
    if(num_eig_hun_and_fiv=="eight hundred and five" or num_eig_hun_and_fiv=="eight hundred five"):
        print("correct")
        vec_num[63]="805"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_eig_hun_and_ten=input("810 in english: ")
    if(num_eig_hun_and_ten=="eight hundred and ten" or num_eig_hun_and_ten=="eight hundred ten"):
        print("correct")
        vec_num[64]="810"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_nin_hun=input("900 in english: ")
    if(num_nin_hun=="nine hundred"):
        print("correct")
        vec_num[65]="900"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_nin_hun_and_fiv=input("905 in english: ")
    if(num_nin_hun_and_fiv=="nine hundred and five" or num_nin_hun_and_fiv=="nine hundred five"):
        print("correct")
        vec_num[66]="905"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_nin_hun_and_ten=input("910 in english: ")
    if(num_nin_hun_and_ten=="nine hundred and ten" or num_nin_hun_and_ten=="nine hundred ten"):
        print("correct")
        vec_num[67]="910"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_tho=input("1.000 in english: ")
    if(num_one_tho=="one thousand"):
        print("correct")
        vec_num[68]="1.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_tho_fiv=input("1.005 in english: ")
    if(num_one_tho_fiv=="one thousand five"):
        print("correct")
        vec_num[69]="1.005"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_tho_ten=input("1.010 in english: ")
    if(num_one_tho_ten=="one thousand ten"):
        print("correct")
        vec_num[70]="1.010"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_tho_one_hun=input("1.100 in english: ")
    if(num_one_tho_one_hun=="one thousand one hundred"):
        print("correct")
        vec_num[71]="1.100"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ten_tho=input("10.000 in english: ")
    if(num_ten_tho=="ten thousand"):
        print("correct")
        vec_num[72]="10.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ten_tho_fiv=input("10.005 in english: ")
    if(num_ten_tho_fiv=="ten thousand five" or num_ten_tho_fiv=="ten thousand and five"):
        print("correct")
        vec_num[73]="10.005"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ten_tho_ten=input("10.010 in english: ")
    if(num_ten_tho_ten=="ten thousand ten" or num_ten_tho_ten=="ten thousand and ten"):
        print("correct")
        vec_num[74]="10.010"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ten_tho_one_hun=input("10.100 in english: ")
    if(num_ten_tho_one_hun=="ten thousand one hundred" or num_ten_tho_one_hun=="ten thousand and one hundred"):
        print("correct")
        vec_num[75]="10.100"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_tho=input("100.000 in english: ")
    if(num_one_hun_tho=="one hundred thousand"):
        print("correct")
        vec_num[76]="100.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_tho_fiv=input("100.005 in english: ")
    if(num_one_hun_tho_fiv=="one hundred thousand five" or num_ten_tho_fiv=="one hundred thousand and five"):
        print("correct")
        vec_num[77]="100.005"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_tho_ten=input("100.010 in english: ")
    if(num_one_hun_tho_ten=="one hundred thousand ten" or num_one_hun_tho_ten=="one hundred thousand and ten"):
        print("correct")
        vec_num[78]="100.010"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_tho_one_hun=input("100.100 in english: ")
    if(num_one_hun_tho_one_hun=="one hundred thousand one hundred" or num_one_hun_tho_one_hun=="one hundred thousand and one hundred"):
        print("correct")
        vec_num[79]="100.100"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_mill=input("1.000.000 in english: ")
    if(num_one_mill=="one million"):
        print("correct")
        vec_num[80]="1.000.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_ten_mill=input("10.000.000 in english: ")
    if(num_ten_mill=="ten million"):
        print("correct")
        vec_num[81]="10.000.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_one_hun_mill=input("100.000.000 in english: ")
    if(num_one_hun_mill=="one hundred million"):
        print("correct")
        vec_num[82]="1.000.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    num_bill=input("1.000.000.000 in english: ")
    if(num_bill=="billion"):
        print("correct")
        vec_num[83]="1.000.000.000"
        var_num+=1
    else:
        print("incorrect")
    print()

    print("Answers:")
    print(f"result: {var_num}/84")
    print("List of correct: ")
    recorrer_lista(vec_num)
    print()
    see_ans_num=input("you want to see the list of answers?(yes/not): ")
    if(see_ans_num=="yes"):
        list_correct_numbers()
    print()

def months():
    good=0
    vec_mon=["------","------","------","------","------","------","------","------","------","------","------","------"]
    print()
    print("MONTHS")    
    good=0
    ene_in_eng=input("enero in english: ")
    day_of_ene=input("how many days are there in enero: ")
    if(ene_in_eng=="january" and day_of_ene=="31 days"):
        print("correct")
        good+=1
        vec_mon[0]="january"
    else:
        print("incorrect")
    print()
    
    feb_in_eng=input("febrero in english: ")
    day_of_feb=input("how many days are there in febrero: ")
    day_of_feb_lep=input("how many days are the in febrero when is leap-year: ")
    if(feb_in_eng=="february" and day_of_feb=="28 days" and day_of_feb_lep=="29 days"):
        print("correct")
        good+=1
        vec_mon[1]="february"
    else:
        print("incorrect")
    print()
    mar_in_eng=input("marzo in english: ")
    day_of_mar=input("how many days are ther in marzo: ")
    if(mar_in_eng=="march" and day_of_mar=="31 days"):
        print("correct")
        good+=1
        vec_mon[2]="march"
    else:
        print("incorrect")
    print()
    apr_in_eng=input("abril in english: ")
    day_of_apr=input("how many days are there in abril: ")
    if(apr_in_eng=="april" and day_of_apr=="30 days"):
        print("correct")
        good+=1
        vec_mon[3]="april"
    else:
        print("incorrect")
    print()
    may_in_eng=input("mayo in english: ")
    day_of_may=input("how many days are their in mayo: ")
    if(may_in_eng=="may" and day_of_may=="31 days"):
        print("correct")
        good+=1
        vec_mon[4]="may"
    else:
        print("incorrect")
    print()
    jun_in_eng=input("junio in english: ")
    day_of_jun=input("how many days are there in junio: ")
    if(jun_in_eng=="june" and day_of_jun=="30 days"):
        print("correct")
        good+=1
        vec_mon[5]="june"
    else:
        print("incorrect")
    print()
    jul_in_eng=input("julio in english: ")
    day_of_jul=input("how many days are their in julio: ")
    if(jul_in_eng=="july" and day_of_jul=="31 days"):
        print("correct")
        good+=1
        vec_mon[6]="july"
    else:
        print("incorrect")
    print()
    
    aug_in_eng=input("agosto in english: ")
    day_of_agu=input("how many days are their in agosto: ")
    if(aug_in_eng=="august" and day_of_agu=="31 days"):
        print("correct")
        good+=1
        vec_mon[7]="august"
    else:
        print("incorrect")
    print()
    sep_in_eng=input("septiembre in english: ")
    day_of_sep=input("how many days are their in septiembre: ")
    if(sep_in_eng=="september" and day_of_sep=="30 days"):
        print("correct")
        good+=1
        vec_mon[8]="september"
    else:
        print("incorrect")
    print()
    
    oct_in_eng=input("octubre in english: ")
    day_of_oct=input("how many days are their in octubre: ")
    if(oct_in_eng=="october" and day_of_oct=="31 days"):
        print("correct")
        good+=1
        vec_mon[9]="october"
    else:
        print("incorrect")
    print()
    nov_in_eng=input("noviembre in english: ")
    day_of_nov=input("how many days are their in noviembre: ")
    if(nov_in_eng=="november" and day_of_nov=="30 days"):
        print("correct")
        good+=1
        vec_mon[10]="november"
    else:
        print("incorrect")
    print()
    dec_in_eng=input("diciembre in english: ")
    day_of_dec=input("how many days are their in diciembre: ")
    if(dec_in_eng=="december" and day_of_dec=="31 days"):
        print("correct")
        good+=1
        vec_mon[11]="december"
    else:
        print("incorrect")
    print()
    
    print("Answers:")
    recorrer_lista(vec_mon)
    print(f"result: {good}/12")
    print()
    list_correct_months()
    print()

def noun_subject():
    print()
    answer_wh_sub=input("what is a subject?: ")
    if(answer_wh_sub=="a subject is a part of a sentence that contains the person or thing performing the action in a sentence"):
        print("correct")
    else: 
        print("incorrect")

    print()
    print("what is a subject?---a subject is a part of a sentence that contains the person or thing performing the action in a sentence")
    print()

    point=False
    list_test_noun_subject=["----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----","----"]
    good=0
    print('write esquina in english')
    corner_word=input()    
    if(corner_word=='corner'):
        print('correct')
        good=good+1
        list_test_noun_subject[0]='corner'
    else:
        print('incorrect')
    print('')

    print('write Esposo in english')
    cousin_word=input()    
    if(cousin_word=='cousin'):
        print('correct')
        good=good+1
        list_test_noun_subject[1]='cousin'
    else:
        print('incorrect')
    print('')

    print('write Sombrilla in english')
    umbrella_word=input()    
    if(umbrella_word=='umbrella'):
        print('correct')
        good=good+1
        list_test_noun_subject[2]='umbrella'
    else:
        print('incorrect')
    print('')

    print('write Basura(music) in english')
    trash_word=input()
    print('write Basura in english')
    rubbish_word=input()
    if(trash_word=='trash' and rubbish_word=='rubbish'):
        print('correct')
        good=good+1
        list_test_noun_subject[3]='trash'
    else:
        print('incorrect')
    print('')

    print('write Gafas in english')
    glasses_word=input()    
    if(glasses_word=='glasses'):
        print('correct')
        good=good+1
        list_test_noun_subject[4]='glasses'
    else:
        print('incorrect')
    print('')

    print('write Vidrio/Vaso/copa in english')
    glass_word=input()    
    if(glass_word=='glass'):
        print('correct')
        good=good+1
        list_test_noun_subject[5]='glass'
    else:
        print('incorrect')
    print('')

    print('write Aro in english')
    rings_word=input()    
    if(rings_word=='rings'):
        print('correct')
        good=good+1
        list_test_noun_subject[6]='rings'
    else:
        print('incorrect')
    print('')

    print('write Campo in english')
    countryside_word=input()    
    if(countryside_word=='countryside'):
        print('correct')
        good=good+1
        list_test_noun_subject[7]='countryside'
    else:
        print('incorrect')
    print('')
    
    print('write Sequía in english')
    drought_word=input()    
    if(drought_word=='drought'):
        print('correct')
        good=good+1
        list_test_noun_subject[8]='drought'
    else:
        print('incorrect')
    print('')

    print('write Reliquias in english')
    relics_word=input()    
    if(relics_word=='relics'):
        print('correct')
        good=good+1
        list_test_noun_subject[9]='relics'
    else:
        print('incorrect')
    print('')

    print('write Huellas in english')
    footprints_word=input()    
    if(footprints_word=='footprints'):
        print('correct')
        good=good+1
        list_test_noun_subject[10]='footprints'
    else:
        print('incorrect')
    print('')

    print('write Capas in english')
    layers_word=input()    
    if(layers_word=='layers'):
        print('correct')
        good=good+1
        list_test_noun_subject[11]='layers'
    else:
        print('incorrect')
    print('')

    print('write Sedimento in english')
    sediment_word=input()    
    if(sediment_word=='sediment'):
        print('correct')
        good=good+1
        list_test_noun_subject[12]='sediment'
    else:
        print('incorrect')
    print('')

    print('write Arcilla in english')
    clay_word=input()    
    if(clay_word=='clay'):
        print('correct')
        good=good+1
        list_test_noun_subject[13]='clay'
    else:
        print('incorrect')
    print('')

    print('write Centro in english')
    downtown_word=input()    
    if(downtown_word=='downtown'):
        print('correct')
        good=good+1
        list_test_noun_subject[14]='downtown'
    else:
        print('incorrect')
    print('')

    print('write enteros in english')
    integers_word=input()
    if(integers_word=='integers'):
        print('correct')
        good=good+1
        list_test_noun_subject[15]='integers'
    else:
        print('incorrect')
    print('')

    print("wirte actual in english")
    current_word=input()
    if(current_word=="current"):
        print("correct")
        good=good+1
        list_test_noun_subject[16]='current'
    else:
        print("incorrect")
    print("")

    print("write lote/terreno in english")
    lot_word=input()
    if(lot_word=="lot"):
        print("correct")
        good=good+1
        list_test_noun_subject[17]="lot"
    else:
        print("incorrect")
    print("")

    print("wirte todo in english")
    everything_word=input()    
    if(everything_word=="everything"):
        print("correct")
        good=good+1
        list_test_noun_subject[18]="everything"
    else:
        print("incorrect")
    print("")

    print("write padre/progenitor in englis")
    parent_word=input()
    if(parent_word=="parent"):
        print("correct")
        good=good+1
        list_test_noun_subject[19]="parent"
    else:
        print("incorrect")
    print("")

    print('write propiedad/posesión in english')
    ownership_word=input()
    if(ownership_word=='ownership'):
        print('correct')
        good=good+1
        list_test_noun_subject[20]='ownership'
    else:
        print('incorrect')
    print('')

    print('write restrinción/limitación in english')
    constraint_word=input()
    if(constraint_word=='constraint'):
        print('correct')
        good=good+1
        list_test_noun_subject[21]='constraint'
    else:
        print('incorrect')
    print('')

    print('write objetivo/meta/proposito in english')
    target_word=input()
    if(target_word=='target'):
        print('correct')
        good=good+1
        list_test_noun_subject[22]='target'
    else:
        print('incorrect')
    print('')

    print('write marco/estructura in english')
    frame_word=input()
    if(frame_word=='frame'):
        print('correct')
        good=good+1
        list_test_noun_subject[23]='frame'
    else:
        print('incorrect')
    print('')

    print('write patrones/estampados/adorno in english')
    patterns_word=input()
    if(patterns_word=='patterns'):
        print('correct')
        good=good+1
        list_test_noun_subject[24]='patterns'
    else:
        print('incorrect')
    print('')

    print('write gráfica/historia medica/ranking in english')
    chart_word=input()    
    if(chart_word=='chart'):
        print('correct')
        good=good+1
        list_test_noun_subject[25]='chart'
    else:
        print('incorrect')
    print('')

    print('write diseño in english')
    layout_word=input()
    if(layout_word=='layout'):
        print('correct')
        good=good+1
        list_test_noun_subject[26]='layout'
    else:
        print('incorrect')
    print('')

    print('write rueda in english')
    wheel_word=input()    
    if(wheel_word=='wheel'):
        print('correct')
        good=good+1
        list_test_noun_subject[27]='wheel'
    else:
        print('incorrect')
    print('')

    print("write claridad in english")
    lightness_word=input()
    if(lightness_word=="lightness"):
        print("correct")
        good=good+1
        list_test_noun_subject[28]="lightness"
    else:
        print("incorrect")
    print()        

    print('write sombra/oscuridad in english')
    shade_word=input()    
    if(shade_word=='shade'):
        print('correct')
        good=good+1
        list_test_noun_subject[29]='shade'
    else:
        print('incorrect')
    print('')

    print('write grado in english')
    degree_word=input()    
    if(degree_word=='degree'):
        print('correct')
        good=good+1
        list_test_noun_subject[30]='degree'
    else:
        print('incorrect')
    print('')

    print('write luz in english')
    light_word=input()    
    if(light_word=='light'):
        print('correct')
        good=good+1
        list_test_noun_subject[31]='light'
    else:
        print('incorrect')
    print('')

    print('write sentido/juicio/sentido(rational thinking)/presentimiento/sensación in english')
    sense_word=input()    
    if(sense_word=='sense'):
        print('correct')
        good=good+1
        list_test_noun_subject[32]='sense'
    else:
        print('incorrect')
    print('')

    print('write borde/ventaja in english')
    edge_word=input()    
    if(edge_word=='edge'):
        print('correct')
        good=good+1
        list_test_noun_subject[33]='edge'
    else:
        print('incorrect')
    print('')

    print('write cuenta in english')
    account_word=input()    
    if(account_word=='account'):
        print('correct')
        good=good+1
        list_test_noun_subject[34]='account'
    else:
        print('incorrect')
    print('')

    print('write matiz/tonalidad in english')
    nuance_word=input()    
    if(nuance_word=='nuance'):
        print('correct')
        good=good+1
        list_test_noun_subject[35]='nuance'
    else:
        print('incorrect')
    print('')

    print('write bombilla/canaleta in english')
    bulb_word=input()    
    if(bulb_word=='bulb'):
        print('correct')
        good=good+1
        list_test_noun_subject[36]='bulb'
    else:
        print('incorrect')
    print('')

    print('write panorama/vista/paisaje in english')
    landscape_word=input()    
    if(landscape_word=='landscape'):
        print('correct')
        good=good+1
        list_test_noun_subject[37]='landscape'
    else:
        print('incorrect')
    print('')

    print('write acuerdo/trato in english')
    deal_word=input()    
    if(deal_word=='deal'):
        print('correct')
        good=good+1
        list_test_noun_subject[38]='deal'
    else:
        print('incorrect')
    print('')

    print('write alcantarilla/canaleta in english')
    gutter_word=input()    
    if(gutter_word=='gutter'):
        print('correct')
        good=good+1
        list_test_noun_subject[39]='gutter'
    else:
        print('incorrect')
    print('')

    print('write hermanos in english')
    brethren_word=input()    
    if(brethren_word=='brethren'):
        print('correct')
        good=good+1
        list_test_noun_subject[40]='brethren'
    else:
        print('incorrect')
    print('')

    print('write comerciante/vendedor(a) in english')
    vendor_word=input()    
    if(vendor_word=='vendor'):
        print('correct')
        good=good+1
        list_test_noun_subject[41]='vendor'
    else:
        print('incorrect')
    print('')

    print('write borrador/boceto/bosquejo/corriente/cerveza de barril/caña/jarra in english')
    draft_word=input()    
    if(draft_word=='draft'):
        print('correct')
        good=good+1
        list_test_noun_subject[42]='draft'
    else:
        print('incorrect')
    print('')

    print('write nido in english')
    nast_word=input()    
    if(nast_word=='nast'):
        print('correct')
        good=good+1
        list_test_noun_subject[43]='nast'
    else:
        print('incorrect')
    print('')

    print('write característica/distintivo/rasgo/ in english')
    feature_word=input()    
    if(feature_word=='feature'):
        print('correct')
        good=good+1
        list_test_noun_subject[44]='feature'
    else:
        print('incorrect')
    print('')

    print('write socia/socio/pareja/compañero(a) in english')
    parther_word=input()    
    if(parther_word=='partner'):
        print('correct')
        good=good+1
        list_test_noun_subject[45]='partner'
    else:
        print('incorrect')
    print('')

    print('write racismo/agrupar/amontonar in english')
    bunch_word=input()    
    if(bunch_word=='bunch'):
        print('correct')
        good=good+1
        list_test_noun_subject[46]='bunch'
    else:
        print('incorrect')
    print('')

    print('write puntos suspensivos in english')
    ellipsis_word=input()    
    if(ellipsis_word=='ellipsis'):
        print('correct')
        good=good+1
        list_test_noun_subject[47]='ellipsis'
    else:
        print('incorrect')
    print('')

    print('write mancha/granito/lugar(informal)/sitio(informal)/roncha in english')
    spot_word=input()    
    if(spot_word=='spot'):
        print('correct')
        good=good+1
        list_test_noun_subject[48]='spot'
    else:
        print('incorrect')
    print('')

    print('write punto/puntada/pinchazo in english')
    stitch_word=input()    
    if(stitch_word=='stitch'):
        print('correct')
        good=good+1
        list_test_noun_subject[49]='stitch'
    else:
        print('incorrect')
    print('')

    print('write sesión/horario/turno/periodo in english')
    sitting_word=input()    
    if(sitting_word=='sitting'):
        print('correct')
        good=good+1
        list_test_noun_subject[50]='sitting'
    else:
        print('incorrect')
    print('')

    print('write armuerzo/desayuno armuerzo in english')
    brunch_word=input()    
    if(brunch_word=='brunch'):
        print('correct')
        good=good+1
        list_test_noun_subject[51]='brunch'
    else:
        print('incorrect')
    print('')

    print('write retrato in english')
    portrait_word=input()
    if(portrait_word=='portrait'):
        print('correct')
        good=good+1
        list_test_noun_subject[52]='portrait'
    else:
        print('incorrect')
    print('')

    print('write par/pareja in english')
    couple_word=input()    
    if(couple_word=='couple'):
        print('correct')
        good=good+1
        list_test_noun_subject[53]='couple'
    else:
        print('incorrect')
    print('')

    print('write hueco/espacio/intervalo/interrupción/lapso in english')
    gap_word=input()    
    if(gap_word=='gap'):
        print('correct')
        good=good+1
        list_test_noun_subject[54]='gap'
    else:
        print('incorrect')
    print('')   

    print('write primavera in english')
    spring_word=input()    
    if(spring_word=='spring'):
        print('correct')
        good=good+1
        list_test_noun_subject[55]='spring'
    else:
        print('incorrect')
    print('')

    print('write heredero in english')
    heir_word=input()    
    if(heir_word=='heir'):
        print('correct')
        good=good+1
        list_test_noun_subject[56]='heir'
    else:
        print('incorrect')
    print('')

    if(good==57):
        point=True
        print("Congratulations, you have a point")
    else:
        print("you not have point")
    print()
    correct_list_test_noun_subject()
    print()

def pronouns():    
    print()
    answer_wh_ar_pro=input("what are pronouns?: ")
    if(answer_wh_ar_pro=="pronouns are the words we often use to talk about a person when we are not using their name"):
        print("correct")
    else:
        print("incorrect")

    print()
    print("what are pronouns?--pronouns are the words we often use to talk about a person when we are not using their name")
    print()


    good_pro=0
    point=False
    print("write the pronouns")
    i_var=input("write yo: ")
    if(i_var=="i"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    you_sing_var=input("write tu: ")
    if(you_sing_var=="you"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    he_var=input("write él: ")
    if(he_var=="he"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    she_var=input("write ella: ")
    if(she_var=="she"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    it_var=input("write eso: ")
    if(it_var=="it"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    we_var=input("write nosotros/as: ")
    if(we_var=="we"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    you_plu_var=input("write ustedes: ")
    if(you_plu_var=="you"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    they_var=input("write ellas/ellos: ")
    if(they_var=="they"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("---------------------")
    print("Pronouns:")
    print("i--yo")
    print("you--tú")
    print("he --él")
    print("she--ella")
    print("it--eso")
    print("we--nosotros/as")
    print("you--ustedes")
    print("they--ellas/ellos")
    print("---------------------")
    print()


    print()
    print("write object pronouns")
    me_var_obj_pro=input("write conmigo/a mi: ")
    if(me_var_obj_pro=="me"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    you_sin_var_obj_pro=input("write contigo/a ti: ")
    if(you_sin_var_obj_pro=="you"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    him_var_obj_pro=input("write el/a el: ")
    if(him_var_obj_pro=="him"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    her_var_obj_pro=input("write a ella: ")
    if(her_var_obj_pro=="her"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    it_var_obj_pro=input("write a eso/esa: ")
    if(it_var_obj_pro=="it"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    us_var_obj_pro=input("write a nosotros/nos: ")
    if(us_var_obj_pro=="us"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    you_plu_var_obj_pro=input("write a ustedes: ")
    if(you_plu_var_obj_pro=="you"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    them_var_obj_pro=input("write ellos/ellas: ")
    if(them_var_obj_pro=="them"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    print()
    print("examples object pronouns:")
    exa_1_obj_pro=input("how would the sentence with object pronoun? [susan calls sexilio]: ")
    if(exa_1_obj_pro=="she calls him"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_2_obj_pro=input("how would the sentence with object pronoun? [paul works with kelly]: ")
    if(exa_2_obj_pro=="he works with her"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    exa_3_obj_pro=input("how would the sentence with object pronoun? [peter and victor play with their friend]: ")
    if(exa_3_obj_pro=="they play with them"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    exa_4_obj_pro=input("how would the sentence with object pronoun? [mrs.gonzales feeds the dog]: ")
    if(exa_4_obj_pro=="she feeds it"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    exa_5_obj_pro=input("how would the sentence with object pronouns? [mr.smith feeds the cats]: ")
    if(exa_5_obj_pro=="he feeds them"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")


    exa_6_obj_pro=input("how would the sentence with object pronouns? [mary and charlie talk to my sister and me]: ")
    if(exa_6_obj_pro=="they talk to us"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("---------------------")
    print("Object pronouns:")
    print("me--conmigo/a mi")
    print("you--contigo/a ti")
    print("him--el/a el")
    print("her--a ella")
    print("it--a eso/esa")
    print("us--nosotros/nos")
    print("you--a ustedes")
    print("them--ellos/ellas")
    print()
    print("examples object pronouns")
    print("susan calls sexilio--she calls him")
    print("paul works with kelly--he works with her")
    print("peter and victor play with their friend--they play with them")
    print("mrs.gonzales feeds the dog--she feeds it")
    print("mr.smith feeds the cats--he feeds them")
    print("mary and charlie talk to my sister and me--they talk to us")
    print("---------------------")
    print()

    print()
    print("possessive adjective")
    print("what are possessive adjectives?: ")
    wh_ar_pos_adj=input()
    if(wh_ar_pos_adj=="a possessive adjective is an adjective that modifies a noun by identifying who has ownership or possession of it"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("what are possessive adjectives?--a possessive adjective is an adjective that modifies a noun by identifying who has ownership or possession of it")
    print()

    print()
    print("write possessive adjective")
    my_var_pos_adj=input("write mi/mis: ")
    if(my_var_pos_adj=="my"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    your_sin_var_pos_adj=input("write su(de usted): ")
    if(your_sin_var_pos_adj=="your"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    his_var_pos_adj=input("write su/sus(de el): ")
    if(his_var_pos_adj=="his"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    her_var_pos_adj=input("write su/sus(de ella): ")
    if(her_var_pos_adj=="her"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    its_var_pos_adj=input("write su/sus(de eso(animal o cosa)): ")
    if(its_var_pos_adj=="its"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    our_var_pos_adj=input("wirte nuestro/a/as: ")
    if(our_var_pos_adj=="our"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    your_plu_var_pos_adj=input("write sus(de ustedes): ")
    if(your_plu_var_pos_adj=="your"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    their_var_pos_adj=input("write su/sus(de ellos): ")
    if(their_var_pos_adj=="their"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("examples possessive adjective")
    exa_1_pos_adj=input("i'm brushing ___ teeth: ")
    if(exa_1_pos_adj=="my"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_2_pos_adj=input("pablo is cleaning ___ bedroom: ")
    if(exa_2_pos_adj=="his"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    exa_3_pos_adj=input("gloria is feeding __ dog: ")
    if(exa_3_pos_adj=="her"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_4_pos_adj=input("you are painting ___ living room: ")
    if(exa_4_pos_adj=="your"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_5_pos_adj=input("the monkey is reading ___ book: ")
    if( exa_5_pos_adj=="its"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_6_pos_adj=input("Mr and Mrs melgar are cooking ___ dinner: ")
    if(exa_6_pos_adj=="their"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_7_pos_adj=input("my sister and i are eating ___ lunch: ")
    if(exa_7_pos_adj=="our"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("---------------------")
    print("possessive adjective")
    print()
    print("my--mi/mis")
    print("your--su(de usted)")
    print("his--su/sus(de el)")
    print("her--su/sus(de ella)")
    print("its--su/sus(de eso(animal o cosa))")
    print("our--nuestro/a/as")
    print("your--sus(de ustedes)")
    print("their--su/sus(de ellos)")
    print()
    print("Examples possessive adjective")
    print("i'm beushing __ teeth--my")
    print("pablo is cleaning __ bedroom--his")
    print("gloria is feeding __ dog--her")
    print("you are painting __ living room--your")
    print("the monkey is reading __ book--its")
    print("Mr and Mrs melgar are cooking __ dinner--their")
    print("My sister and i are eating __ lunch--our")
    print("---------------------")
    print()

    print()
    print("Possessive pronouns")
    mine_var_pos_pro=input("write mía/mío(s): ")
    if(mine_var_pos_pro=="mine"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    yours_sin_var_pos_pro=input("write tuya/tuyo(s)/suyo(s): ")
    if(yours_sin_var_pos_pro=="yours"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    his_var_pos_pro=input("write de él/suyo(s): ")
    if(his_var_pos_pro=="his"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    hers_var_pos_pro=input("write de ella/suyo(s): ")
    if(hers_var_pos_pro=="hers"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    ours_var_pos_pro=input("write nuestra/nuestro(s): ")
    if(ours_var_pos_pro=="ours"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    yours_plu_var_pos_pro=input("write ustedes: ")
    if(yours_plu_var_pos_pro=="yours"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    theirs_var__pos_pro=input("write ellos/suyo(s):")
    if(theirs_var__pos_pro=="theirs"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("examples possessive pronouns")
    exa_1_pos_pro=input("write in english:[La casa es tuya]: ")
    if(exa_1_pos_pro=="the house is yours"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_2_pos_pro=input("write in english:[La casa es de él]: ")
    if(exa_2_pos_pro=="the house is his"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    exa_3_pos_pro=input("write in english:[La casa es de ella]: ")
    if(exa_3_pos_pro=="the house is hers"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("---------------------")
    print("Possessive adjective:")
    print("mine--mía/mío(s)")
    print("yours--tuya/tuyo(s)/suyo(s)")
    print("his--de él/suyo(s)")
    print("hers--ella/suyo(s)")
    print("ours--nuestra/nuestro(s)")
    print("yours--ustedes")
    print("theirs--ellos/suyo(s)")
    print()
    print("Examples:")
    print("the house is yours--La casa es tuya")
    print("the house is his--La casa de él")
    print("the house is hers--La casa es de ella")
    print("---------------------")
    print()

    print()
    print("Reflexives pronouns")
    wha_ref_pro=input("what are reflexives pronouns?: ")
    if(wha_ref_pro=="these pronouns are used when we want to refer to ourselves or to something itself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("what are reflexives pronouns--these pronouns are used whe we want to refer to ourselves or to something itself")
    print()

    print("write reflexives pronouns")
    mys_var_ref_pro=input("write yo mismo/a mi: ")
    if(mys_var_ref_pro=="myself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    you_var_ref_pro=input("write tu mismo(a tí)/usted mismo(a usted): ")
    if(you_var_ref_pro=="yourself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    him_var_ref_pro=input("write él mismo/a sí mismo: ")
    if(him_var_ref_pro=="himself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    her_var_ref_pro=input("write ella misma/a sí misma: ")
    if(her_var_ref_pro=="herself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    its_var_ref_pro=input("write él mismo/a sí mismo: ")
    if(its_var_ref_pro=="itself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    our_var_ref_pro=input("write nosotros mismos: ")
    if(our_var_ref_pro=="ourselves"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    you_var_ref_pro=input("write vosotros mismos/ustedes mismos: ")
    if(you_var_ref_pro=="yourselves"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    the_var_ref_pro=input("write ellos mismos: ")
    if(the_var_ref_pro=="themselves"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

    print()
    print("examples reflexives pronouns")
    exa_1_ref_pro=input("how would the sentence with reflexive pronouns? [él viaja solo]: ")
    if(exa_1_ref_pro=="he travels by himself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()
    
    exa_4_ref_pro=input("how would the sentence with reflexive pronouns? [mé corte con un cuchillo]: ")
    if(exa_4_ref_pro=="i cut myself with a knife"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    exa_5_ref_pro=input("how would the sentence with reflexive pronouns? [te vas a lastimar]: ")
    if(exa_5_ref_pro=="you are going to hurt yourself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    exa_6_ref_pro=input("how would the sentence with reflexive pronouns? [él mismo preparó todo]: ")
    if(exa_6_ref_pro=="he prepared everything himself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    exa_7_ref_pro=input("how would the sentence with reflexive pronouns? [ella misma reparo su carro]: ")
    if(exa_7_ref_pro=="she fixed her car herself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    print("how would the sentence with reflexive pronouns? [ellos quieren crear un robot que se mueva por sí mismo]: ")
    exa_8_ref_pro=input()
    if(exa_8_ref_pro=="they want to create a robot that can move by itself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    print("how would the sentence with reflexive pronouns? [nos pusimos en gran riesgo en esta situación]: ")
    exa_9_ref_pro=input()
    if(exa_9_ref_pro=="we put ourselves at great risk in that situation"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    exa_10_ref_pro=input("how would the sentence with reflexive pronouns? [ellos se encontraron en serios problemas]: ")
    if(exa_10_ref_pro=="they found themselves in serious trouble"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    print("how would the sentence with reflexive pronouns? [como ustedes mismos pueden ver, esto ha sido muy fácil]: ")
    exa_11_ref_pro=input()
    if(exa_11_ref_pro=="as you yourselves can see,this has been very easy"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    print()
    print("----------------------------")
    print("reflexives pronouns")
    print()
    print("myself--yo mismo/a mi")
    print("yourself--tu mismo(a tí)/usted mismo(a usted)")
    print("himself--él mismo/a sí mismo")
    print("herself--ella misma/a sí misma")
    print("itself--él mismo/a sí mismo")
    print("ourselves--nosotros mismos")
    print("yourselves--vosotros mismos/ustedes mismos")
    print("themselves--ellos mismos")
    print()
    print("examples reflexives pronouns")
    print("él viaja solo--he travles by himself")
    print("mé corte con un cuchillo--i cut myself with a knife")
    print("te vas a lastimar--you are going to hurt yourself")
    print("él mismo preparó todo--he prepared everything himself")
    print("ella misma reparo su carro--she fixed her car herself")
    print("ellos quieren crear un robot que se mueva por sí mismo--they want to create a robot that can move by itself")
    print("nos pusimos en gran riesgo en esta situación--we put orselves at great risk in that situation")
    print("ellos se encontraron en serios problemas--they found themselves in serious trouble")
    print("como ustedes mismos pueden ver, esto ha sido muy fácil--as you yourselves can see,this has been very easy")
    print("----------------------------")
    print()

    if(good_pro==66):
        print("Congratulations, you have a point")
        point=True
    else:
        print("you not have point")
    
    print()

def examples_articles_ind():
    var_art_exa=0
    example=False
    exa_1_ind_art=input("tell me [un gato] in english: ")
    if(exa_1_ind_art=="a cat"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_2_ind_art=input("tell me [un perro] in english: ")
    if(exa_2_ind_art=="a dog"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_3_ind_art=input("tell me [una foto] in english: ")
    if(exa_3_ind_art=="a picture"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_4_ind_art=input("tell me [una mesa] in english: ")
    if(exa_4_ind_art=="a table"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()        

    exa_5_ind_art=input("tell me [un elefante] in english: ")
    if(exa_5_ind_art=="an elephant"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_6_ind_art=input("tell me [una sombrilla] in english: ")
    if(exa_6_ind_art=="an umbrella"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_7_ind_art=input("tell me [una manzana] in english: ")
    if(exa_7_ind_art=="an apple"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_8_ind_art=input("tell me [un perros] in english: ")
    if(exa_8_ind_art==""):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_9_ind_art=input("tell me [un uniforme] in english: ")
    if(exa_9_ind_art=="a uniform"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_10_ind_art=input("tell me [una universidad] in english: ")
    if(exa_10_ind_art=="a university"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_11_ind_art=input("tell me [un europeo] in english: ")
    if(exa_11_ind_art=="a european"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_12_ind_art=input("tell me [un euro] in english: ")
    if(exa_12_ind_art=="a euro"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_13_ind_art=input("tell me [un tio] in english: ")
    if(exa_13_ind_art=="an uncle"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_14_ind_art=input("tell me [un imperio] in english: ")
    if(exa_14_ind_art=="an empire"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_15_ind_art=input("tell me [un hospital] in english: ")
    if(exa_15_ind_art=="a hospital"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_16_ind_art=input("tell me [una hora] in english: ")
    if(exa_16_ind_art=="an hour"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()
    
    exa_17_ind_art=input("tell me [una casa] in english: ")
    if(exa_17_ind_art=="a home"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_18_ind_art=input("tell me [un agujero] in english: ")
    if(exa_18_ind_art=="a hole"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_19_ind_art=input("tell me [un honor] in english: ")
    if(exa_19_ind_art=="an honor"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_20_ind_art=input("tell me [un sombrero] in english: ")
    if(exa_20_ind_art=="a hat"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_21_ind_art=input("tell me [un/una honest@] in english: ")
    if(exa_21_ind_art=="an honest"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    exa_22_ind_art=input("tell me [un honorario] in english: ")
    if(exa_22_ind_art=="an honorary"):
        print("correct")
        var_art_exa+=1
    else:
        print("incorrect")
    print()

    print("Examples indefinite articles")
    print("tell me [un gato] in english --> a cat")
    print("tell me [un perro] in english --> a dog")
    print("tell me [una foto] in english --> a picture")
    print("tell me [una mesa] in english --> a table")
    print("tell me [un elefante] in english --> an elephant")
    print("tell me [una sombrilla] in english --> an umbrella")
    print("tell me [una manzana] in english--> an apple ")
    print("tell me [un perros] in english --> '[nada]'")
    print("tell me [un uniforme] in english --> a uniform")
    print("tell me [una universidad] in english --> a university")
    print("tell me [un europeo] in english --> a european")
    print("tell me [un euro] in english --> a euro")
    print("tell me [un tio] in english --> an uncle")
    print("tell me [un imperio] in english --> an empire")
    print("tell me [un hospital] in english --> a hospital")
    print("tell me [una hora] in english --> an hour")
    print("tell me [una casa] in english --> a home")
    print("tell me [un agujero] in english --> a hole")
    print("tell me [un honor] in english --> an honor")
    print("tell me [un sombrero] in english --> a hat")
    print("tell me [un/una honest@] in english --> an honest")
    print("tell me [un honorario] in english --> an honorary")
    print()

    if(var_art_exa==22):
        example=True
    
    return(example)

def examples_articles_def():
    var_def_art=0
    example=False
    exa_1_art_def=input("tell me [el gato] in english: ")
    if(exa_1_art_def=="the cat"):
        print("correct")
        var_def_art+=1
    else:
        print("incorrect")
    print()
    
    exa_2_art_def=input("tell me [el elefante] in english: ")
    if(exa_2_art_def=="the elephant"):
        print("correct")
        var_def_art+=1
    else:
        print("incorrect")
    print()
    
    exa_3_art_def=input("tell me [los gatos] in english: ")
    if(exa_3_art_def=="the cats"):
        print("correct")
        var_def_art+=1
    else:
        print("incorrect")
    print()

    exa_4_art_def=input("tell me [los elefantes] in english: ")
    if(exa_4_art_def=="the elephants"):
        print("correct")
        var_def_art+=1
    else:
        print("incorrect")
    print()

    exa_5_art_def=input("tell me [los estados unidos] in english: ")
    if(exa_5_art_def=="the united states"):
        print("correct")
        var_def_art+=1
    else:
        print("incorrect")
    print()

    exa_6_art_def=input("tell me [la republica dominicana] in english: ")
    if(exa_6_art_def=="the dominican republic"):
        print("correct")
        var_def_art+=1
    else:
        print("incorrect")
    print()

    print("Examples articles defined")
    print("tell me [el gato] in english --> the cat")
    print("tell me [el elefante] in english --> the elephant")
    print("tell me [los gatos] in english --> the cats")
    print("tell me [los elefantes] in english --> the elephants")
    print("tell me [los estados unidos] in english --> the united states")
    print("tell me [la republica dominicana] in english--> the dominican republic")
    print()

    if(exa_6_art_def==6):
        print("correct")
        example=True
    
    return example

def articles():
    articles_var=False
    var_art=0
    vec_art=["----","----","----","----","----","----","----"]
    print("Articles:")
    print()
    print("indefinite articles")

    rul_1_ind_art=input("Rule #1: when should it be used the (a)?: ")
    if(rul_1_ind_art=="the (a) is used when the noun begins with a consonant"):
        print("correct")
        var_art+=1
        vec_art[0]="rule #1 indefinite articles"
    else:
        print("incorrect")
    
    print()

    rul_2_ind_art=input("Rule #2: when should it be used the (an)?: ")
    if(rul_2_ind_art=="the (an) is used when the noun begins with a vowel (a/e/i/o/u)"):
        print("correct")
        var_art+=1
        vec_art[1]="rule #2 indefinite articles"
    else:
        print("incorrect")
    
    print()
    print("Rule #1: when should it be used the (a)? --> the (a) is used when the noun begins with a consonant")
    print("Rule #2: when should it be used the (an)? --> the (an) is used when the noun begins with a vowel (a/e/i/o/u)")
    print()

    rul_3_ind_art=input("rule #3: where is the indefinite article located?: ")
    if(rul_3_ind_art=="the article is put before singular nouns"):
        print("correct")
        var_art+=1
        vec_art[2]="rule #3 indefinite articles"
    else:
        print("incorrect")
    
    print()
    print("rule #3: where is the indefinite article located? --> the article is put before singular nouns")
    print()

    art_ind=input("what are the indefinite articles?: ")
    if(art_ind=="a/an"):
        print("correct")
        var_art+=1
        vec_art[3]="indefinite articles"
    else:
        print("incorrect")
    print()
    print("what are the indefinite articles? --> a/an")
    print()

    example_ind=examples_articles_ind()
    if(example_ind):
        print("correct")
        var_art+=1
        vec_art[4]="examples indefinite articles"
    else:
        print("incorrect")
    print()


    
    print("defined articles")
    def_art_wha=input("what are the definite articles?: ")
    def_art_spa=input("what does (the) mean in spanish?: ")
    if(def_art_wha=="the" and def_art_spa=="el/la/los/las"):
        print("correct")
        var_art+=1
        vec_art[5]="definite articles"
    else:
        print("incorrect")
    print()

    print("what are the definite articles? --> the ||| what does (the) mean in spanish? --> el/la/los/las")
    print()

    example_def=examples_articles_def()
    if(example_def):
        print("correct")
        var_art+=1
        vec_art[6]="examples defined"
    else:
        print("incorrect")
    print()

    if(var_art==7):
        print("correct you have a point")
        articles_var=True
    else:
        print("incorrect you have not point")

    print("answers")
    print(f"results: {var_art}/7")
    print()
    recorrer_lista(vec_art)
    print()

def adjective():
    print()
    answer_wh_adj=input("what is a adjective?: ")
    if(answer_wh_adj=="an adjective is a word that describes the traits,qualities or number of a noun"):
        print("correct")
    else:
        print("incorrect")
    print()
    print("what is a adjective--an adjective is a word that describes the traits,qualities or number of a noun")
    print()


    point=False
    list_test_adjective=["------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------""------","------","------","------","------","------","------","------","------","------","------","------""------","------","------","------","------","------","------","------","------","------","------","------","------"]
    good=0
    print('write enfadado in english')
    angry_word=input()    
    if(angry_word=='angry'):
        print('correct')
        good=good+1
        list_test_adjective[0]='angry'
    else:
        print('incorrect')
    print('')

    print('write feliz in english')
    happy_word=input()
    if(happy_word=='happy'):
        print('correct')
        good=good+1
        list_test_adjective[1]='happy'
    else:
        print('incorrect')
    print('')

    print('write triste in english')
    sad_word=input()
    if(sad_word=='sad'):
        print('correct')
        good=good+1
        list_test_adjective[2]='sad'
    else:
        print('incorrect')
    print('')

    print('write considerado/atento in english')
    thoughtful_word=input()
    if(thoughtful_word=='thoughtful'):
        print('correct')
        good=good+1
        list_test_adjective[3]='thoughtful'
    else:
        print('incorrect')
    print('')

    print('write creído in english')
    arrogant_word=input()
    if(arrogant_word=='arrogant'):
        print('correct')
        good=good+1
        list_test_adjective[4]='arrogant'
    else:
        print('incorrect')
    print('')

    print('write ambicioso in english')
    ambitious_word=input()
    if(ambitious_word=='ambitious'):
        print('correct')
        good=good+1
        list_test_adjective[5]='ambitious'
    else:
        print('incorrect')
    print('')

    print('write liso in english')
    smooth_word=input()
    if(smooth_word=='smooth'):
        print('correct')
        good=good+1
        list_test_adjective[6]='smooth'
    else:
        print('incorrect')
    print('')

    print('write irregular/con baches/con hoyos in english')
    bumpy_word=input()
    if(bumpy_word=='bumpy'):
        print('correct')
        good=good+1
        list_test_adjective[7]='bumpy'
    else:
        print('incorrect')
    print('')

    print('write blando/suave in english')
    soft_word=input()
    if(soft_word=='soft'):
        print('correct')
        good=good+1
        list_test_adjective[8]='soft'
    else:
        print('incorrect')
    print('')

    print('write picante in english')
    spicy_word=input()
    if(spicy_word=='spicy'):
        print('correct')
        good=good+1
        list_test_adjective[9]='spicy'
    else:
        print('incorrect')
    print('')

    print('write dulce in english')
    sweet_word=input()
    if(sweet_word=='sweet'):
        print('correct')
        good=good+1
        list_test_adjective[10]='sweet'
    else:
        print('incorrect')
    print('')

    print('write agrio/ácido in english')
    sour_word=input()
    if(sour_word=='sour'):
        print('correct')
        good=good+1
        list_test_adjective[11]='sour'
    else:
        print('incorrect')
    print('')

    print('write restante in english')
    remaining_word=input()
    if(remaining_word=='remaining'):
        print('correct')
        good=good+1
        list_test_adjective[12]='remaining'
    else:
        print('incorrect')
    print('')

    print('write liviano/ligero/peso ligero/de poco peso/persona que se emborracha fácilmente/pelagatos/don nadie in english')
    lightweight_word=input()
    if(lightweight_word=='lightweight'):
        print('correct')
        good=good+1
        list_test_adjective[13]='lightweight'
    else:
        print('incorrect')
    print('')

    print('write deficiente/insuficiente in english')
    wanting_word=input()
    if(wanting_word=='wanting'):
        print('correct')
        good=good+1
        list_test_adjective[14]='wanting'
    else:
        print('incorrect')
    print('')

    print('write gastado/usado/vacío in english')
    spent_word=input()
    if(spent_word=='spent'):
        print('correct')
        good=good+1
        list_test_adjective[15]='spent'
    else:
        print('incorrect')
    print('')

    print('write poder/capaz/talentoso(a) in english')
    able_word=input()
    if(able_word=='able'):
        print('correct')
        good=good+1
        list_test_adjective[16]='able'
    else:
        print('incorrect')
    print('')

    print('write tonto(a)/bobo(a)/absurdo(a) in english')
    silly_word=input()
    if(silly_word=='silly'):
        print('correct')
        good=good+1
        list_test_adjective[17]='silly'
    else:
        print('incorrect')
    print('')

    print('write en la onda/en la moda/apestosó(a)/fétido(a) in english')
    funky_word=input()
    if(funky_word=='funky'):
        print('correct')
        good=good+1
        list_test_adjective[18]='funky'
    else:
        print('incorrect')
    print('')

    print('write por la mitad/a medias in english')
    halfway_word=input()
    if(halfway_word=='halfway'):
        print('correct')
        good=good+1
        list_test_adjective[19]='halfway'
    else:
        print('incorrect')
    print('')

    print('write mas lejos/más lejano/más extenso/más a fondo in english')
    further_word=input()
    if(further_word=='further'):
        print('correct')
        good=good+1
        list_test_adjective[20]='further'
    else:
        print('incorrect')
    print('')

    print('write suficiente/bastante in english')
    enough_word=input()
    if(enough_word=='enough'):
        print('correct')
        good=good+1
        list_test_adjective[21]='enough'
    else:
        print('incorrect')
    print('')

    print('write viable/factible/probable in english')
    feasible_word=input()
    if(feasible_word=='feasible'):
        print('correct')
        good=good+1
        list_test_adjective[22]='feasible'
    else:
        print('incorrect')
    print('')

    print('write valiente/audaz/atrevido in english')
    bold_word=input()
    if(bold_word=='bold'):
        print('correct')
        good=good+1
        list_test_adjective[23]='bold'
    else:
        print('incorrect')
    print('')

    print('write pagado/pago(a)/remunerado in english')
    paid_word=input()
    if(paid_word=='paid'):
        print('correct')
        good=good+1
        list_test_adjective[24]='paid'
    else:
        print('incorrect')
    print('')

    print('write anidado/dentro de una cosa/alojado in english')
    nested_word=input()
    if(nested_word=='nested'):
        print('correct')
        good=good+1
        list_test_adjective[25]='nested'
    else:
        print('incorrect')
    print('')

    print('write complicado(a)/delicado(a)/que tiene su maña/difícil/complicado(a)/tramposo(a)/falso(a) in english')
    tricky_word=input()
    if(tricky_word=='tricky'):
        print('correct')
        good=good+1
        list_test_adjective[26]='tricky'
    else:
        print('incorrect')
    print('')

    print('write fijo(a)/inamovible/inalterable/reparado/areglado(a) in english')
    fixed_word=input()
    if(fixed_word=='fixed'):
        print('correct')
        good=good+1
        list_test_adjective[27]='fixed'
    else:
        print('incorrect')
    print('')

    print('write deseado/anhelado/apropiado(a) in english')
    desired_word=input()
    if(desired_word=='desired'):
        print('correct')
        good=good+1
        list_test_adjective[28]='desired'
    else:
        print('incorrect')
    print('')   

    print('write superpuesto/solapado(a) in english')
    overlapping_word=input()
    if(overlapping_word=='overlapping'):
        print('correct')
        good=good+1
        list_test_adjective[29]='overlapping'
    else:
        print('incorrect')
    print('')

    print('write bonito(a)/lindo(a)/precioso(a)/guapo(a) in english')
    pretty_word=input()
    if(pretty_word=='pretty'):
        print('correct')
        good=good+1
        list_test_adjective[30]='pretty'
    else:
        print('incorrect')
    print('')

    print('write angosto/estrecho/corto/reducido in english')
    narrow_word=input()
    if(narrow_word=='narrow'):
        print('correct')
        good=good+1
        list_test_adjective[31]='narrow'
    else:
        print('incorrect')
    print('')

    print('write preciso(a)/exacto(a)/certero(a)/riguroso(a)/acertado(a) in english')
    accurate_word=input()
    if(accurate_word=='accurate'):
        print('correct')
        good=good+1
        list_test_adjective[32]='accurate'
    else:
        print('incorrect')
    print('')

    print('write significativo(a) in english')
    meaningful_word=input()
    if(meaningful_word=='meaningful'):
        print('correct')
        good=good+1
        list_test_adjective[33]='meaningful'
    else:
        print('incorrect')
    print('')

    print('write profundo/hondo/grave in english')
    deep_word=input()
    if(deep_word=='deep'):
        print('correct')
        good=good+1
        list_test_adjective[34]='deep'
    else:
        print('incorrect')
    print('')

    print('write inesperado(a)/imprevisto(a) in english')
    unexpected_word=input()
    if(unexpected_word=='unexpected'):
        print('correct')
        good=good+1
        list_test_adjective[35]='unexpected'
    else:
        print('incorrect')
    print('')

    print('write relacionado/familiar/pariente in english')
    related_word=input()
    if(related_word=='related'):
        print('correct')
        good=good+1
        list_test_adjective[36]='related'
    else:
        print('incorrect')
    print('')

    print('write varios/varias in english')
    several_word=input()
    if(several_word=='several'):
        print('correct')
        good=good+1
        list_test_adjective[37]='several'
    else:
        print('incorrect')
    print('')

    print('write ameno(a)/entretenido(a)/legible in english')
    readable_word=input()
    if(readable_word=='readable'):
        print('correct')
        good=good+1
        list_test_adjective[38]='readable'
    else:
        print('incorrect')
    print('')

    print('write otro/distinto in english')
    another_word=input()
    if(another_word=='another'):
        print('correct')
        good=good+1
        list_test_adjective[39]='another'
    else:
        print('incorrect')
    print('')

    print('write entero/total/todo/completo in english')
    whole_word=input()
    if(whole_word=='whole'):
        print('correct')
        good=good+1
        list_test_adjective[40]='whole'
    else:
        print('incorrect')
    print('')

    print('write complicado/complejo in english')
    complex_word=input()
    if(complex_word=='complex'):
        print('correct')
        good=good+1
        list_test_adjective[41]='complex'
    else:
        print('incorrect')
    print('')

    print('write aquellos/esas/esos in english')
    those_word=input()
    if(those_word=='those'):
        print('correct')
        good=good+1
        list_test_adjective[42]='those'
    else:
        print('incorrect')
    print('')

    print('write más bajo/más corto in english')
    shortest_word=input()
    if(shortest_word=='shortest'):
        print('correct')
        good=good+1
        list_test_adjective[43]='shortest'
    else:
        print('incorrect')
    print('')

    print('write sutil/disimulado/desimulada in english')
    subtle_word=input()
    if(subtle_word=='subtle'):
        print('correct')
        good=good+1
        list_test_adjective[44]='subtle'
    else:
        print('incorrect')
    print('')   

    if(good==45):
        point=True 
        print("congratulations")        
    else:
        print("you not have point")

    print()
    list_correct_adjective()
    print()

    adjective_example()
    print()
    print("examples")
    print("red car--carro rojo")
    print("red cars--carros rojos")
    print("gata--female cat")
    print("gato--male cat")
    print("i like the green car--me gusta el carro verde")
    print()

    

def adjective_example():
    point=False
    good=0
    ans_adj_exa_1=input("write in english [carro rojo]: ")
    if(ans_adj_exa_1=="red car"):
        print("correct")
        good+=1
    else:
        print("incorrect")

    ans_adj_exa_2=input("write in english [carros rojos]: ")
    if(ans_adj_exa_2=="red cars"):
        print("correct")
        good+=1
    else:
        print("incorrect")

    ans_adj_exa_3=input("write in english [gata]: ")
    if(ans_adj_exa_3=="female cat"):
        print("correct")
        good+=1
    else:
        print("incorrect")

    ans_adj_exa_4=input("write in english [gato]: ")
    if(ans_adj_exa_4=="male cat"):
        print("correct")
        good+=1
    else:
        print("incorrect")

    ans_adj_exa_5=input("write in english [me gusta el carro verde]: ")
    if(ans_adj_exa_5=="i like the green car"):
        print("correct")
        good+=1
    else:
        print("incorrect")

    if(good==5):
        print("congratulations")
        point=True
    else:
        print("error 404")

    return point

def test_verbs():
    var_tes_ver=0
    cor_or_inc=False

    ver_tes_1=input("preguntar in english:? ")
    if(ver_tes_1=="ask"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    

    ver_tes_2=input("ser/estar in english:? ")
    if(ver_tes_2=="be"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    

    ver_tes_3=input("romper/quebrar in english:? ")
    if(ver_tes_3=="break"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_4=input("llevar/traer/jalar/mover/trasladar/transportar in english:? ")
    if(ver_tes_4=="bring"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_5=input("llamar in english:? ")
    if(ver_tes_5=="call"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_6=input("llevar/cargar in english:? ")
    if(ver_tes_6=="carry"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_7=input("chequear/verificar/comprobar/revisar in english:? ")
    if(ver_tes_7=="check"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_8=input("cortar in english:? ")
    if(ver_tes_8=="cut"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_9=input("venir/llegar/entrar/acercarse in english:? ")
    if(ver_tes_9=="come"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_10=input("hacer in english:? ")
    if(ver_tes_10=="do"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_11=input("caerse/dejar/caer in english:? ")
    if(ver_tes_11=="drop"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_12=input("caerse/caer in english:? ")
    if(ver_tes_12=="fall"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_13=input("llenar/rellenar/llenarse in english:? ")
    if(ver_tes_13=="fill"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_14=input("encontrar/encontrarse in english:? ")
    if(ver_tes_14=="find"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_15=input("conseguir/obtener/llegar in english:? ")
    if(ver_tes_15=="get"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_16=input("pasar/dar/alcanzar in english:? ")
    if(ver_tes_16=="give"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_18=input("irse/partir in english:? ")
    if(ver_tes_18=="go"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_19=input("crecer in english:? ")
    if(ver_tes_19=="grown"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_20=input("dar/pasar/entregar in english:? ")
    if(ver_tes_20=="hand"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_21=input("exponer/colgar/ahorcar in english:? ")
    if(ver_tes_21=="hang"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_22=input("agarrar/sostener/retener/tener in english:? ")
    if(ver_tes_22=="hold"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_23=input("guardar/conservar/mantener in english:? ")
    if(ver_tes_23=="keep"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_24=input("dejar/permitir in english:? ")
    if(ver_tes_24=="let"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_25=input("registrar/anotar/talar/loguearse in english:? ")
    if(ver_tes_25=="log"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_26=input("mirar in english:? ")
    if(ver_tes_26=="look"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_27=input("hacer in english:? ")
    if(ver_tes_27=="make"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_28=input("pasar in english:? ")
    if(ver_tes_28=="pass"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_29=input("correr/recorrer in english:? ")
    if(ver_tes_29=="run"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_31=input("ponerse/poner/colocar/ajustar in english:? ")
    if(ver_tes_31=="set"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_32=input("poner/colocar in english:? ")
    if(ver_tes_32=="put"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_33=input("escoger/coger/recolectar/recoger in english:? ")
    if(ver_tes_33=="pick"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_34=input("pagar in english:? ")
    if(ver_tes_34=="pay"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_35=input("decir/contar in english:? ")
    if(ver_tes_35=="tell"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_36=input("girar/rotar in english:? ")
    if(ver_tes_36=="turn"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_37=input("agarrar/coger/tomar in english:? ")
    if(ver_tes_37=="take"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_38=input("hablar in english:? ")
    if(ver_tes_38=="talk"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    ver_tes_39=input("trabajar in english:? ")
    if(ver_tes_39=="work"):
        print("correct")
        var_tes_ver+=1
    else:
        print("incorrect")
    print()

    if(var_tes_ver==39):
        cor_or_inc=True

    list_correct_verbs()
    print()

def test_verbs_regular():
    var_tes_ver_reg=0
    cor_or_inc_reg=False

    ver_tes_reg_1_pre=input("grabar in present in english?: ")
    ver_tes_reg_1_pas=input("grabar in past in english?: ")
    ver_tes_reg_1_par=input("grabar in past participle in english?: ")
    if(ver_tes_reg_1_pre=="record" and ver_tes_reg_1_pas=="recorded" and ver_tes_reg_1_par=="recorded"):
        print("correct")
        var_tes_ver_reg+=1
    else:
        print("incorrect")
    print()

    if(var_tes_ver_reg==1):
        cor_or_inc_reg=True

    list_correct_verbs_regular()
    print()

    return cor_or_inc_reg
    
def test_verbs_irregulars():
    var_tes_ver_irre=0
    cor_or_inc_irre=False

    ver_tes_irre_1_pre=input("golpear in present in english?: ")
    ver_tes_irre_1_pas=input("golpear in past in english?: ")
    ver_tes_irre_1_par=input("golpear in past participle in english?: ")
    if(ver_tes_irre_1_pre=="hit" and ver_tes_irre_1_pas=="hit" and ver_tes_irre_1_par=="hit"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Golpear-->hit-->hit-->hit")
    print()

    ver_tes_irre_2_pre=input("Quedar/servir/entrar/valer in present in english?: ")
    ver_tes_irre_2_pas=input("Quedar/servir/entrar/valer in past in english?: ")
    ver_tes_irre_2_par=input("Quedar/servir/entrar/valer in past participle in english?: ")
    if(ver_tes_irre_2_pre=="fit" and ver_tes_irre_2_pas=="fit" and ver_tes_irre_2_par=="fit"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Quedar/Servir/entrar/valer-->fit-->fit-->fit")
    print()

    ver_tes_irre_3_pre=input("renunciar/dejar/abandonar in present in english?: ")
    ver_tes_irre_3_pas=input("renunciar/dejar/abandonar in past in english?: ")
    ver_tes_irre_3_par=input("renunciar/dejar/abandonar in past participle in english?: ")
    if(ver_tes_irre_3_pre=="quit" and ver_tes_irre_3_pas=="quit" and ver_tes_irre_3_par=="quit"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Renunciar/dejar/abandonar-->quit-->quit-->quit")
    print()

    ver_tes_irre_4_pre=input("dividir/apartar/partir in present in english?: ")
    ver_tes_irre_4_pas=input("dividir/apartar/partir in past in english?: ")
    ver_tes_irre_4_par=input("dividir/apartar/partir in past participle in english?: ")
    if(ver_tes_irre_4_pre=="split" and ver_tes_irre_4_pas=="split" and ver_tes_irre_4_par=="split"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Dividir/apartar/partir-->split-->split-->split")
    print()

    ver_tes_irre_5_pre=input("cortar in present in english?: ")
    ver_tes_irre_5_pas=input("cortar in past in english?: ")
    ver_tes_irre_5_par=input("cortar in past participle in english?: ")
    if(ver_tes_irre_5_pre=="slit" and ver_tes_irre_5_pas=="slit" and ver_tes_irre_5_par=="slit"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Cortar-->slit-->slit-->slit")
    print()

    ver_tes_irre_6_pre=input("deshacerse in present in english?: ")
    ver_tes_irre_6_pas=input("deshacerse in past in english?: ")
    ver_tes_irre_6_par=input("deshacerse in past participle in english?: ")
    if(ver_tes_irre_6_pre=="rid" and ver_tes_irre_6_pas=="rid" and ver_tes_irre_6_par=="rid"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Deshacerse-->rid-->rid-->rid")
    print()

    ver_tes_irre_7_pre=input("ofrecer/pujar(en una subasta) in present in english?: ")
    ver_tes_irre_7_pas=input("ofrecer/pujar(en una subasta) in past in english?: ")
    ver_tes_irre_7_par=input("ofrecer/pujar(en una subasta) in past participle in english?: ")
    if(ver_tes_irre_7_pre=="bid" and ver_tes_irre_7_pas=="bid" and ver_tes_irre_7_par=="bid"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("Ofrecer/pujar(en una subasta)-->bid-->bid-->bid")
    print()

    ver_tes_irre_8_pre=input("dejar in present in english?: ")
    ver_tes_irre_8_pas=input("dejar in past in english?: ")
    ver_tes_irre_8_par=input("dejar in past participle in english?: ")
    if(ver_tes_irre_8_pre=="let" and ver_tes_irre_8_pas=="let" and ver_tes_irre_8_par=="let"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("dejar-->let-->let-->let")
    print()
    

    ver_tes_irre_9_pre=input("ubicar/ajustar/cuadremos una cosa in present in english?: ")
    ver_tes_irre_9_pas=input("ubicar/ajustar/cuadremos una cosa in past in english?: ")
    ver_tes_irre_9_par=input("ubicar/ajustar/cuadremos una cosa in past participle in english?: ")
    if(ver_tes_irre_9_pre=="set" and ver_tes_irre_9_pas=="set" and ver_tes_irre_9_par=="set"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("ubicar/ajustar/cuadremos una cosa-->set-->set-->set")
    print()

    ver_tes_irre_10_pre=input("mojar in present in english?: ")
    ver_tes_irre_10_pas=input("mojar in past in english?: ")
    ver_tes_irre_10_par=input("mojar in past participle in english?: ")
    if(ver_tes_irre_10_pre=="wet" and ver_tes_irre_10_pas=="wet" and ver_tes_irre_10_par=="wet"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")    
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("mojar-->wet-->wet-->wet")
    print()

    ver_tes_irre_11_pre=input("apostar in present in english?: ")
    ver_tes_irre_11_pas=input("apostar in past in english?: ")
    ver_tes_irre_11_par=input("apostar in past participle in english?: ")
    if(ver_tes_irre_11_pre=="bet" and ver_tes_irre_11_pas=="bet" and ver_tes_irre_11_par=="bet"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("apostar-->bet-->bet-->bet")
    print()

    ver_tes_irre_12_pre=input("esparcir in present in english?: ")
    ver_tes_irre_12_pas=input("esparcir in past in english?: ")
    ver_tes_irre_12_par=input("esparcir in past participle in english?: ")
    if(ver_tes_irre_12_pre=="spread" and ver_tes_irre_12_pas=="spread" and ver_tes_irre_12_par=="spread"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle") 
    print("esparcir-->spread-->spread-->spread")
    print()

    ver_tes_irre_13_pre=input("sudar in present in english?: ")
    ver_tes_irre_13_pas=input("sudar in past in english?: ")
    ver_tes_irre_13_par=input("sudar in past participle in english?: ")
    if(ver_tes_irre_13_pre=="sweat" and ver_tes_irre_13_pas=="sweat" and ver_tes_irre_13_par=="sweat"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("sudar-->sweat-->sweat-->sweat")
    print()

    ver_tes_irre_14_pre=input("golpear in present in english?: ")
    ver_tes_irre_14_pas=input("golpear in past in english?: ")
    ver_tes_irre_14_par=input("golpear in past participle in english?: ")
    if(ver_tes_irre_14_pre=="beat" and ver_tes_irre_14_pas=="beat" and ver_tes_irre_14_par=="beat/beaten"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("golpear-->beat-->beat-->beat/beaten")
    print()

    ver_tes_irre_15_pre=input("poner in present in english?: ")
    ver_tes_irre_15_pas=input("poner in past in english?: ")
    ver_tes_irre_15_par=input("poner in past participle in english?: ")
    if(ver_tes_irre_15_pre=="put" and ver_tes_irre_15_pas=="put" and ver_tes_irre_15_par=="put"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("poner-->put-->put-->put")
    print()


    ver_tes_irre_16_pre=input("cortar in present in english?: ")
    ver_tes_irre_16_pas=input("cortar in past in english?: ")
    ver_tes_irre_16_par=input("cortar in past participle in english?: ")
    if(ver_tes_irre_16_pre=="cut" and ver_tes_irre_16_pas=="cut" and ver_tes_irre_16_par=="cut"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("cortar-->cut-->cut-->cut")
    print()

    ver_tes_irre_17_pre=input("cerrar in present in english?: ")
    ver_tes_irre_17_pas=input("cerrar in past in english?: ")
    ver_tes_irre_17_par=input("cerrar in past participle in english?: ")
    if(ver_tes_irre_17_pre=="shut" and ver_tes_irre_17_pas=="shut" and ver_tes_irre_17_par=="shut"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("cerrar-->shut-->shut-->shut")
    print()

    ver_tes_irre_18_pre=input("introducir/insertar/meter/penetrar in present in english?: ")
    ver_tes_irre_18_pas=input("introducir/insertar/meter/penetrar in past in english?: ")
    ver_tes_irre_18_par=input("introducir/insertar/meter/penetrar in past participle in english?: ")
    if(ver_tes_irre_18_pre=="thrust" and ver_tes_irre_18_pas=="thrust" and ver_tes_irre_18_par=="thrust"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("introducir/insertar/meter/penetrar-->thrust-->thrust-->thrust")
    print()

    ver_tes_irre_19_pre=input("costar in present in english?: ")
    ver_tes_irre_19_pas=input("costar in past in english?: ")
    ver_tes_irre_19_par=input("costar in past participle in english?: ")
    if(ver_tes_irre_19_pre=="cost" and ver_tes_irre_19_pas=="cost" and ver_tes_irre_19_par=="cost"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("costar-->cost-->cost-->cost")
    print()

    ver_tes_irre_20_pre=input("herir in present in english?: ")
    ver_tes_irre_20_pas=input("herir in past in english?: ")
    ver_tes_irre_20_par=input("herir in past participle in english?: ")
    if(ver_tes_irre_20_pre=="hurt" and ver_tes_irre_20_pas=="hurt" and ver_tes_irre_20_par=="hurt"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("herir-->hurt-->hurt-->hurt")
    print()

    ver_tes_irre_21_pre=input("reventar in present in english?: ")
    ver_tes_irre_21_pas=input("reventar in past in english?: ")
    ver_tes_irre_21_par=input("reventar in past participle in english?: ")
    if(ver_tes_irre_21_pre=="burst" and ver_tes_irre_21_pas=="burst" and ver_tes_irre_21_par=="burst"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("reventar-->burst-->burst-->burst")
    print()

    ver_tes_irre_22_pre=input("arrojar/lanzar in present in english?: ")
    ver_tes_irre_22_pas=input("arrojar/lanzar in past in english?: ")
    ver_tes_irre_22_par=input("arrojar/lanzar in past participle in english?: ")
    if(ver_tes_irre_22_pre=="cast" and ver_tes_irre_22_pas=="cast" and ver_tes_irre_22_par=="cast"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("arrojar/lanzar-->cast-->cast-->cast")
    print()

    ver_tes_irre_23_pre=input("transmitir in present in english?: ")
    ver_tes_irre_23_pas=input("transmitir in past in english?: ")
    ver_tes_irre_23_par=input("transmitir in past participle in english?: ")
    if(ver_tes_irre_23_pre=="broadcast" and ver_tes_irre_23_pas=="broadcast" and ver_tes_irre_23_par=="broadcast"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("transmitir-->broadcast-->broadcast-->broadcast")
    print()

    ver_tes_irre_24_pre=input("predecir in present in english?: ")
    ver_tes_irre_24_pas=input("predecir in past in english?: ")
    ver_tes_irre_24_par=input("predecir in past participle in english?: ")
    if(ver_tes_irre_24_pre=="forecast" and ver_tes_irre_24_pas=="forecast" and ver_tes_irre_24_par=="forecast"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("predecir-->forecast-->forecast-->forecast")
    print()

    ver_tes_irre_25_pre=input("mantener/guardar in present in english?: ")
    ver_tes_irre_25_pas=input("mantener/guardar in past in english?: ")
    ver_tes_irre_25_par=input("mantener/guardar in past participle in english?: ")
    if(ver_tes_irre_25_pre=="keep" and ver_tes_irre_25_pas=="kept" and ver_tes_irre_25_par=="kept"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("mantener/guardar-->keep-->kept-->kept")
    print()


    ver_tes_irre_26_pre=input("dormir in present in english?: ")
    ver_tes_irre_26_pas=input("dormir in past in english?: ")
    ver_tes_irre_26_par=input("dormir in past participle in english?: ")
    if(ver_tes_irre_26_pre=="sleep" and ver_tes_irre_26_pas=="slept" and ver_tes_irre_26_par=="slept"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("dormir-->sleep-->slept-->slept")
    print()

    ver_tes_irre_27_pre=input("barrer in present in english?: ")
    ver_tes_irre_27_pas=input("barrer in past in english?: ")
    ver_tes_irre_27_par=input("barrer in past participle in english?: ")
    if(ver_tes_irre_27_pre=="sweep" and ver_tes_irre_27_pas=="swept" and ver_tes_irre_27_par=="swept"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("barrer-->sweep-->swept-->swept")
    print()

    ver_tes_irre_28_pre=input("llorar in present in english?: ")
    ver_tes_irre_28_pas=input("llorar in past in english?: ")
    ver_tes_irre_28_par=input("llorar in past participle in english?: ")
    if(ver_tes_irre_28_pre=="weep" and ver_tes_irre_28_pas=="wept" and ver_tes_irre_28_par=="wept"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("llorar-->weep-->wept-->wept")
    print()

    ver_tes_irre_29_pre=input("sentir in present in english?: ")
    ver_tes_irre_29_pas=input("sentir in past in english?: ")
    ver_tes_irre_29_par=input("sentir in past participle in english?: ")
    if(ver_tes_irre_29_pre=="feel" and ver_tes_irre_29_pas=="felt" and ver_tes_irre_29_par=="felt"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("sentir-->feel-->felt-->felt")
    print()

    ver_tes_irre_30_pre=input("arrodillarse in present in english?: ")
    ver_tes_irre_30_pas=input("arrodillarse in past in english?: ")
    ver_tes_irre_30_par=input("arrodillarse in past participle in english?: ")
    if(ver_tes_irre_30_pre=="kneel" and ver_tes_irre_30_pas=="knelt" and ver_tes_irre_30_par=="knelt"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("arrodillarse-->kneel-->knelt-->knelt")
    print()

    ver_tes_irre_31_pre=input("alimentar in present in english?: ")
    ver_tes_irre_31_pas=input("alimentar in past in english?: ")
    ver_tes_irre_31_par=input("alimentar in past participle in english?: ")
    if(ver_tes_irre_31_pre=="feed" and ver_tes_irre_31_pas=="fed" and ver_tes_irre_31_par=="fed"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("alimentar-->feed-->fed-->fed")
    print()

    ver_tes_irre_32_pre=input("sangrar in present in english?: ")
    ver_tes_irre_32_pas=input("sangrar in past in english?: ")
    ver_tes_irre_32_par=input("sangrar in past participle in english?: ")
    if(ver_tes_irre_32_pre=="bleed" and ver_tes_irre_32_pas=="bled" and ver_tes_irre_32_par=="bled"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("sangrar-->bleed-->bled-->bled")
    print()

    ver_tes_irre_33_pre=input("crear/procrear in present in english?: ")
    ver_tes_irre_33_pas=input("crear/procrear in past in english?: ")
    ver_tes_irre_33_par=input("crear/procrear in past participle in english?: ")
    if(ver_tes_irre_33_pre=="breed" and ver_tes_irre_33_pas=="bred" and ver_tes_irre_33_par=="bred"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("crear/procrear-->breed-->bred-->bred")
    print()


    ver_tes_irre_34_pre=input("acelerar in present in english?: ")
    ver_tes_irre_34_pas=input("acelerar in past in english?: ")
    ver_tes_irre_34_par=input("acelerar in past participle in english?: ")
    if(ver_tes_irre_34_pre=="speed" and ver_tes_irre_34_pas=="sped" and ver_tes_irre_34_par=="sped"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("acelerar-->speed-->sped-->sped")
    print()

    ver_tes_irre_35_pre=input("conocer in present in english?: ")
    ver_tes_irre_35_pas=input("conocer in past in english?: ")
    ver_tes_irre_35_par=input("conocer in past participle in english?: ")
    if(ver_tes_irre_35_pre=="meet" and ver_tes_irre_35_pas=="met" and ver_tes_irre_35_par=="met"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("conocer-->meet-->met-->met")
    print()


    ver_tes_irre_36_pre=input("guiar in present in english?: ")
    ver_tes_irre_36_pas=input("guiar in past in english?: ")
    ver_tes_irre_36_par=input("guiar in past participle in english?: ")
    if(ver_tes_irre_36_pre=="lead" and ver_tes_irre_36_pas=="let" and ver_tes_irre_36_par=="let"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("guiar-->lead-->let-->let")
    print()


    ver_tes_irre_37_pre=input("repartir/dar in present in english?: ")
    ver_tes_irre_37_pas=input("repartir/dar in past in english?: ")
    ver_tes_irre_37_par=input("repartir/dar in past participle in english?: ")
    if(ver_tes_irre_37_pre=="deal" and ver_tes_irre_37_pas=="dealt" and ver_tes_irre_37_par=="dealt"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("repartir/dar-->deal-->dealt-->dealt")
    print()

    ver_tes_irre_38_pre=input("inclinarse in present in english?: ")
    ver_tes_irre_38_pas=input("inclinarse in past in english?: ")
    ver_tes_irre_38_par=input("inclinarse in past participle in english?: ")
    if(ver_tes_irre_38_pre=="lean" and ver_tes_irre_38_pas=="leant" and ver_tes_irre_38_par=="leant"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("inclinarse-->lean-->leant-->leant")
    print()

    ver_tes_irre_39_pre=input("aprender/memorizar in present in english?: ")
    ver_tes_irre_39_pas=input("aprender/memorizar in past in english?: ")
    ver_tes_irre_39_par=input("aprender/memorizar in past participle in english?: ")
    if(ver_tes_irre_39_pre=="learn" and ver_tes_irre_39_pas=="learnt/learned" and ver_tes_irre_39_par=="learnt/learned"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("aprender(memorizar-->learn-->learnt/learned-->learnt/learned")
    print()

    ver_tes_irre_40_pre=input("querer decir/significar in present in english?: ")
    ver_tes_irre_40_pas=input("querer decir/significar in past in english?: ")
    ver_tes_irre_40_par=input("querer decir/significar in past participle in english?: ")
    if(ver_tes_irre_40_pre=="mean" and ver_tes_irre_40_pas=="meant" and ver_tes_irre_40_par=="meant"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("querer decir/significar-->mean-->meant-->meant")
    print()

    ver_tes_irre_41_pre=input("saltar/brincar in present in english?: ")
    ver_tes_irre_41_pas=input("saltar/brincar in past in english?: ")
    ver_tes_irre_41_par=input("saltar/brincar in past participle in english?: ")
    if(ver_tes_irre_41_pre=="leap" and ver_tes_irre_41_pas=="leapt" and ver_tes_irre_41_par=="leapt"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("saltar/brincar-->leap-->leapt-->leapt")
    print()

    ver_tes_irre_42_pre=input("soñar in present in english?: ")
    ver_tes_irre_42_pas=input("soñar in past in english?: ")
    ver_tes_irre_42_par=input("soñar in past participle in english?: ")
    if(ver_tes_irre_42_pre=="dream" and ver_tes_irre_42_pas=="dreamt" and ver_tes_irre_42_par=="dreamt"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("soñar-->dream-->dreamt-->dreamt")
    print()

    ver_tes_irre_43_pre=input("oir/escuchar in present in english?: ")
    ver_tes_irre_43_pas=input("oir/escuchar in past in english?: ")
    ver_tes_irre_43_par=input("oir/escuchar in past participle in english?: ")
    if(ver_tes_irre_43_pre=="hear" and ver_tes_irre_43_pas=="heard" and ver_tes_irre_43_par=="heard"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("oir/escuchar-->hear-->heard-->heard")
    print()

    ver_tes_irre_44_pre=input("leer in present in english?: ")
    ver_tes_irre_44_pas=input("leer in past in english?: ")
    ver_tes_irre_44_par=input("leer in past participle in english?: ")
    if(ver_tes_irre_44_pre=="read" and ver_tes_irre_44_pas=="read" and ver_tes_irre_44_par=="read"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("leer-->read-->read-->read")
    print()

    ver_tes_irre_45_pre=input("encontrar in present in english?: ")
    ver_tes_irre_45_pas=input("encontrar in past in english?: ")
    ver_tes_irre_45_par=input("encontrar in past participle in english?: ")
    if(ver_tes_irre_45_pre=="find" and ver_tes_irre_45_pas=="found" and ver_tes_irre_45_par=="found"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("encontrar-->find-->found-->found")
    print()

    ver_tes_irre_46_pre=input("atar in present in english?: ")
    ver_tes_irre_46_pas=input("atar in past in english?: ")
    ver_tes_irre_46_par=input("atar in past participle in english?: ")
    if(ver_tes_irre_46_pre=="bind" and ver_tes_irre_46_pas=="bound" and ver_tes_irre_46_par=="bound"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("atar-->bind-->bound-->bound")
    print()

    ver_tes_irre_47_pre=input("moler in present in english?: ")
    ver_tes_irre_47_pas=input("moler in past in english?: ")
    ver_tes_irre_47_par=input("moler in past participle in english?: ")
    if(ver_tes_irre_47_pre=="grind" and ver_tes_irre_47_pas=="ground" and ver_tes_irre_47_par=="ground"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("moler-->grind-->ground-->ground")
    print()

    ver_tes_irre_48_pre=input("darle cuerda in present in english?: ")
    ver_tes_irre_48_pas=input("darle cuerda in past in english?: ")
    ver_tes_irre_48_par=input("darle cuerda in past participle in english?: ")
    if(ver_tes_irre_48_pre=="wind" and ver_tes_irre_48_pas=="wound" and ver_tes_irre_48_par=="wound"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("darle cuerda-->wind-->wound-->wound")
    print()

    ver_tes_irre_49_pre=input("desenrollar in present in english?: ")
    ver_tes_irre_49_pas=input("desenrollar in past in english?: ")
    ver_tes_irre_49_par=input("desenrollar in past participle in english?: ")
    if(ver_tes_irre_49_pre=="unwind" and ver_tes_irre_49_pas=="unwound" and ver_tes_irre_49_par=="unwound"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("desenrollar-->unwind-->unwound-->unwound")
    print()

    ver_tes_irre_50_pre=input("desatar/desabrochar in present in english?: ")
    ver_tes_irre_50_pas=input("desatar/desabrochar in past in english?: ")
    ver_tes_irre_50_par=input("desatar/desabrochar in past participle in english?: ")
    if(ver_tes_irre_50_pre=="unbind" and ver_tes_irre_50_pas=="unbound" and ver_tes_irre_50_par=="unbound"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("desatar/desabrochar-->unbind-->unbound-->unbound")
    print()

    ver_tes_irre_51_pre=input("enviar in present in english?: ")
    ver_tes_irre_51_pas=input("enviar in past in english?: ")
    ver_tes_irre_51_par=input("enviar in past participle in english?: ")
    if(ver_tes_irre_51_pre=="send" and ver_tes_irre_51_pas=="sent" and ver_tes_irre_51_par=="sent"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("enviar-->send-->sent-->sent")
    print()

    ver_tes_irre_52_pre=input("gastar in present in english?: ")
    ver_tes_irre_52_pas=input("gastar in past in english?: ")
    ver_tes_irre_52_par=input("gastar in past participle in english?: ")
    if(ver_tes_irre_52_pre=="spend" and ver_tes_irre_52_pas=="spent" and ver_tes_irre_52_par=="spent"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("gastar-->spend-->spent-->spent")
    print()

    ver_tes_irre_53_pre=input("doblar in present in english?: ")
    ver_tes_irre_53_pas=input("doblar in past in english?: ")
    ver_tes_irre_53_par=input("doblar in past participle in english?: ")
    if(ver_tes_irre_53_pre=="bend" and ver_tes_irre_53_pas=="bent" and ver_tes_irre_53_par=="bent"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("doblar-->bend-->bent-->bent")
    print()

    ver_tes_irre_54_pre=input("mezclar in present in english?: ")
    ver_tes_irre_54_pas=input("mezclar in past in english?: ")
    ver_tes_irre_54_par=input("mezclar in past participle in english?: ")
    if(ver_tes_irre_54_pre=="blend" and ver_tes_irre_54_pas=="blent" and ver_tes_irre_54_par=="blent"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("mezclar-->blend-->blent-->blent")
    print()

    ver_tes_irre_55_pre=input("prestar in present in english?: ")
    ver_tes_irre_55_pas=input("prestar in past in english?: ")
    ver_tes_irre_55_par=input("prestar in past participle in english?: ")
    if(ver_tes_irre_55_pre=="lend" and ver_tes_irre_55_pas=="lent" and ver_tes_irre_55_par=="lent"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("prestar-->lend-->lent-->lent")
    print()

    ver_tes_irre_56_pre=input("picar/arder in present in english?: ")
    ver_tes_irre_56_pas=input("picar/arder in past in english?: ")
    ver_tes_irre_56_par=input("picar/arder in past participle in english?: ")
    if(ver_tes_irre_56_pre=="sting" and ver_tes_irre_56_pas=="stung" and ver_tes_irre_56_par=="stung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("picar/arder-->sting-->stung-->stung")
    print()

    ver_tes_irre_57_pre=input("pegachento in present in english?: ")
    ver_tes_irre_57_pas=input("pegachento in past in english?: ")
    ver_tes_irre_57_par=input("pegachento in past participle in english?: ")
    if(ver_tes_irre_57_pre=="cling" and ver_tes_irre_57_pas=="clung" and ver_tes_irre_57_par=="clung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("pegachento-->cling-->clung-->clung")
    print()

    ver_tes_irre_58_pre=input("mecerse in present in english?: ")
    ver_tes_irre_58_pas=input("mecerse in past in english?: ")
    ver_tes_irre_58_par=input("mecerse in past participle in english?: ")
    if(ver_tes_irre_58_pre=="swing" and ver_tes_irre_58_pas=="swung" and ver_tes_irre_58_par=="swung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("mecerse-->swing-->swung-->swung")
    print()
    
    ver_tes_irre_59_pre=input("escaparse/escabullirse in present in english?: ")
    ver_tes_irre_59_pas=input("escaparse/escabullirse in past in english?: ")
    ver_tes_irre_59_par=input("escaparse/escabullirse in past participle in english?: ")
    if(ver_tes_irre_59_pre=="slink" and ver_tes_irre_59_pas=="slunk" and ver_tes_irre_59_par=="slunk"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("escaparse/escabullirse-->slink-->slunk-->slunk")
    print()

    ver_tes_irre_60_pre=input("pegar in present in english?: ")
    ver_tes_irre_60_pas=input("pegar in past in english?: ")
    ver_tes_irre_60_par=input("pegar in past participle in english?: ")
    if(ver_tes_irre_60_pre=="stick" and ver_tes_irre_60_pas=="stuck" and ver_tes_irre_60_par=="stuck"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("pegar-->stick-->stuck-->stuck")
    print()

    ver_tes_irre_61_pre=input("cavar in present in english?: ")
    ver_tes_irre_61_pas=input("cavar in past in english?: ")
    ver_tes_irre_61_par=input("cavar in past participle in english?: ")
    if(ver_tes_irre_61_pre=="dig" and ver_tes_irre_61_pas=="dug" and ver_tes_irre_61_par=="dug"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("cavar-->dig-->dug-->dug")
    print()

    ver_tes_irre_62_pre=input("colgar in present in english?: ")
    ver_tes_irre_62_pas=input("colgar in past in english?: ")
    ver_tes_irre_62_par=input("colgar in past participle in english?: ")
    if(ver_tes_irre_62_pre=="hang" and ver_tes_irre_62_pas=="hung" and ver_tes_irre_62_par=="hung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("colgar-->hang-->hung-->hung")
    print()

    ver_tes_irre_63_pre=input("decir in present in english?: ")
    ver_tes_irre_63_pas=input("decir in past in english?: ")
    ver_tes_irre_63_par=input("decir in past participle in english?: ")
    if(ver_tes_irre_63_pre=="say" and ver_tes_irre_63_pas=="said" and ver_tes_irre_63_par=="said"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("decir-->say-->said-->said")
    print()

    ver_tes_irre_64_pre=input("pagar in present in english?: ")
    ver_tes_irre_64_pas=input("pagar in past in english?: ")
    ver_tes_irre_64_par=input("pagar in past participle in english?: ")
    if(ver_tes_irre_64_pre=="pay" and ver_tes_irre_64_pas=="paid" and ver_tes_irre_64_par=="paid"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("pagar-->pay-->paid-->paid")
    print()

    ver_tes_irre_65_pre=input("extender/poner in present in english?: ")
    ver_tes_irre_65_pas=input("extender/poner in past in english?: ")
    ver_tes_irre_65_par=input("extender/poner in past participle in english?: ")
    if(ver_tes_irre_65_pre=="lay" and ver_tes_irre_65_pas=="laid" and ver_tes_irre_65_par=="laid"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("extender/poner-->lay-->laid-->laid")
    print()

    ver_tes_irre_66_pre=input("incrustar in present in english?: ")
    ver_tes_irre_66_pas=input("incrustar in past in english?: ")
    ver_tes_irre_66_par=input("incrustar in past participle in english?: ")
    if(ver_tes_irre_66_pre=="inlay" and ver_tes_irre_66_pas=="inlaid" and ver_tes_irre_66_par=="inlaid"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("incrustar-->inlay-->inlaid-->inlaid")
    print()

    ver_tes_irre_67_pre=input("decir/contar in present in english?: ")
    ver_tes_irre_67_pas=input("decir/contar in past in english?: ")
    ver_tes_irre_67_par=input("decir/contar in past participle in english?: ")
    if(ver_tes_irre_67_pre=="tell" and ver_tes_irre_67_pas=="told" and ver_tes_irre_67_par=="told"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("decir/contar-->tell-->told-->told")
    print()

    ver_tes_irre_68_pre=input("vender in present in english?: ")
    ver_tes_irre_68_pas=input("vender in past in english?: ")
    ver_tes_irre_68_par=input("vender in past participle in english?: ")
    if(ver_tes_irre_68_pre=="sell" and ver_tes_irre_68_pas=="sold" and ver_tes_irre_68_par=="sold"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("vender-->sell-->sold-->sold")
    print()


    ver_tes_irre_69_pre=input("agarrar in present in english?: ")
    ver_tes_irre_69_pas=input("agarrar in past in english?: ")
    ver_tes_irre_69_par=input("agarrar in past participle in english?: ")
    if(ver_tes_irre_69_pre=="hold" and ver_tes_irre_69_pas=="held" and ver_tes_irre_69_par=="held"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("agarrar-->hold-->held-->held")
    print()

    ver_tes_irre_70_pre=input("observar in present in english?: ")
    ver_tes_irre_70_pas=input("observar in past in english?: ")
    ver_tes_irre_70_par=input("observar in past participle in english?: ")
    if(ver_tes_irre_70_pre=="behold" and ver_tes_irre_70_pas=="beheld" and ver_tes_irre_70_par=="beheld"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("observar-->behold-->beheld-->beheld")
    print()

    ver_tes_irre_71_pre=input("sostener in present in english?: ")
    ver_tes_irre_71_pas=input("sostener in past in english?: ")
    ver_tes_irre_71_par=input("sostener in past participle in english?: ")
    if(ver_tes_irre_71_pre=="uphold" and ver_tes_irre_71_pas=="upheld" and ver_tes_irre_71_par=="upheld"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("sostener-->uphold-->upheld-->upheld")
    print()

    ver_tes_irre_72_pre=input("retener in present in english?: ")
    ver_tes_irre_72_pas=input("retener in past in english?: ")
    ver_tes_irre_72_par=input("retener in past participle in english?: ")
    if(ver_tes_irre_72_pre=="withhold" and ver_tes_irre_72_pas=="withheld" and ver_tes_irre_72_par=="withheld"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("retener-->withhold-->withheld-->withheld")
    print()

    ver_tes_irre_73_pre=input("estar de pie/aguantar in present in english?: ")
    ver_tes_irre_73_pas=input("estar de pie/aguantar in past in english?: ")
    ver_tes_irre_73_par=input("estar de pie/aguantar in past participle in english?: ")
    if(ver_tes_irre_73_pre=="stand" and ver_tes_irre_73_pas=="stood" and ver_tes_irre_73_par=="stood"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("estar de pie/aguantar-->stand-->stood-->stood")
    print()

    ver_tes_irre_74_pre=input("entender in present in english?: ")
    ver_tes_irre_74_pas=input("entender in past in english?: ")
    ver_tes_irre_74_par=input("entender in past participle in english?: ")
    if(ver_tes_irre_74_pre=="understand" and ver_tes_irre_74_pas=="understood" and ver_tes_irre_74_par=="understood"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("entender-->understand-->understood-->understood")
    print()

    ver_tes_irre_75_pre=input("soportar in present in english?: ")
    ver_tes_irre_75_pas=input("soportar in past in english?: ")
    ver_tes_irre_75_par=input("soportar in past participle in english?: ")
    if(ver_tes_irre_75_pre=="withstand" and ver_tes_irre_75_pas=="withstood" and ver_tes_irre_75_par=="withstood"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("soportar-->withstand-->withstood-->withstood")
    print()


    ver_tes_irre_76_pre=input("perder in present in english?: ")
    ver_tes_irre_76_pas=input("perder in past in english?: ")
    ver_tes_irre_76_par=input("perder in past participle in english?: ")
    if(ver_tes_irre_76_pre=="lose" and ver_tes_irre_76_pas=="lost" and ver_tes_irre_76_par=="lost"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("perder-->lose-->lost-->lost")
    print()

    ver_tes_irre_77_pre=input("disparar in present in english?: ")
    ver_tes_irre_77_pas=input("disparar in past in english?: ")
    ver_tes_irre_77_par=input("disparar in past participle in english?: ")
    if(ver_tes_irre_77_pre=="shoot" and ver_tes_irre_77_pas=="shot" and ver_tes_irre_77_par=="shot"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("disparar-->shoot-->shot-->shot")
    print()

    ver_tes_irre_78_pre=input("comprar in present in english?: ")
    ver_tes_irre_78_pas=input("comprar in past in english?: ")
    ver_tes_irre_78_par=input("comprar in past participle in english?: ")
    if(ver_tes_irre_78_pre=="buy" and ver_tes_irre_78_pas=="bought" and ver_tes_irre_78_par=="bought"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("comprar-->buy-->bought-->bought")
    print()

    ver_tes_irre_79_pre=input("llevar/traer/jalar/mover/trasladar/transportar in present in english?: ")
    ver_tes_irre_79_pas=input("llevar/traer/jalar/mover/trasladar/transportar in past in english?: ")
    ver_tes_irre_79_par=input("llevar/traer/jalar/mover/trasladar/transportar in past participle in english?: ")
    if(ver_tes_irre_79_pre=="bring" and ver_tes_irre_79_pas=="brought" and ver_tes_irre_79_par=="brought"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("llevar/traer/jalar/mover/trasladar/transportar-->bring-->brought-->brought")
    print()

    ver_tes_irre_80_pre=input("pensar/considerar/reflexionar/creer in present in english?: ")
    ver_tes_irre_80_pas=input("pensar/considerar/reflexionar/creer in past in english?: ")
    ver_tes_irre_80_par=input("pensar/considerar/reflexionar/creer in past participle in english?: ")
    if(ver_tes_irre_80_pre=="think" and ver_tes_irre_80_pas=="thought" and ver_tes_irre_80_par=="thought"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("pensar/considerar/reflexionar/creer-->think-->thought-->thought")
    print()

    ver_tes_irre_81_pre=input("luchar/pelear in present in english?: ")
    ver_tes_irre_81_pas=input("luchar/pelear in past in english?: ")
    ver_tes_irre_81_par=input("luchar/pelear in past participle in english?: ")
    if(ver_tes_irre_81_pre=="fight" and ver_tes_irre_81_pas=="fought" and ver_tes_irre_81_par=="fought"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("luchar/pelear-->fight-->fought-->fought")
    print()

    ver_tes_irre_82_pre=input("enseñar in present in english?: ")
    ver_tes_irre_82_pas=input("enseñar in past in english?: ")
    ver_tes_irre_82_par=input("enseñar in past participle in english?: ")
    if(ver_tes_irre_82_pre=="teach" and ver_tes_irre_82_pas=="taught" and ver_tes_irre_82_par=="taught"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("enseñar-->teach-->taught-->taught")
    print()

    ver_tes_irre_83_pre=input("coger/pillar/cachar/atrapar in present in english?: ")
    ver_tes_irre_83_pas=input("coger/pillar/cachar/atrapar in past in english?: ")
    ver_tes_irre_83_par=input("coger/pillar/cachar/atrapar in past participle in english?: ")
    if(ver_tes_irre_83_pre=="catch" and ver_tes_irre_83_pas=="caught" and ver_tes_irre_83_par=="caught"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("coger/pillar/cachar/atrapar-->catch-->caught-->caught")
    print()

    ver_tes_irre_84_pre=input("escupir in present in english?: ")
    ver_tes_irre_84_pas=input("escupir in past in english?: ")
    ver_tes_irre_84_par=input("escupir in past participle in english?: ")
    if(ver_tes_irre_84_pre=="spit" and ver_tes_irre_84_pas=="spit" and ver_tes_irre_84_par=="spit"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("escupir-->spit-->spit-->spit")
    print()

    ver_tes_irre_85_pre=input("tener in present in english?: ")
    ver_tes_irre_85_pas=input("tener in past in english?: ")
    ver_tes_irre_85_par=input("tener in past participle in english?: ")
    if(ver_tes_irre_85_pre=="have" and ver_tes_irre_85_pas=="had" and ver_tes_irre_85_par=="had"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("tener-->have-->had-->had")
    print()

    ver_tes_irre_86_pre=input("hacer in present in english?: ")
    ver_tes_irre_86_pas=input("hacer in past in english?: ")
    ver_tes_irre_86_par=input("hacer in past participle in english?: ")
    if(ver_tes_irre_86_pre=="make" and ver_tes_irre_86_pas=="made" and ver_tes_irre_86_par=="made"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("hacer-->make-->made-->made")
    print()

    ver_tes_irre_87_pre=input("escribir in present in english?: ")
    ver_tes_irre_87_pas=input("escribir in past in english?: ")
    ver_tes_irre_87_par=input("escribir in past participle in english?: ")
    if(ver_tes_irre_87_pre=="write" and ver_tes_irre_87_pas=="wrote" and ver_tes_irre_87_par=="written"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("escribir-->write-->wrote-->written")
    print()

    ver_tes_irre_88_pre=input("ir en/montar en/conducir/manejar in present in english?: ")
    ver_tes_irre_88_pas=input("ir en/montar en/conducir/manejar in past in english?: ")
    ver_tes_irre_88_par=input("ir en/montar en/conducir/manejar in past participle in english?: ")
    if(ver_tes_irre_88_pre=="ride" and ver_tes_irre_88_pas=="rode" and ver_tes_irre_88_par=="ridden"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("ir en/montar/conducir/manejar-->ride-->rode-->ridden")
    print()

    ver_tes_irre_89_pre=input("conducir/manejar in present in english?: ")
    ver_tes_irre_89_pas=input("conducir/manejar in past in english?: ")
    ver_tes_irre_89_par=input("conducir/manejar in past participle in english?: ")
    if(ver_tes_irre_89_pre=="drive" and ver_tes_irre_89_pas=="drove" and ver_tes_irre_89_par=="driven"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("conducir/manejar-->drive-->drove-->driven")
    print()

    ver_tes_irre_90_pre=input("subir in present in english?: ")
    ver_tes_irre_90_pas=input("subir in past in english?: ")
    ver_tes_irre_90_par=input("subir in past participle in english?: ")
    if(ver_tes_irre_90_pre=="rise" and ver_tes_irre_90_pas=="rose" and ver_tes_irre_90_par=="risen"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("subir-->rise-->rose-->risen")
    print()

    ver_tes_irre_91_pre=input("tratar de/esforzarse por in present in english?: ")
    ver_tes_irre_91_pas=input("tratar de/esforzarse por in past in english?: ")
    ver_tes_irre_91_par=input("tratar de/esforzarse por in past participle in english?: ")
    if(ver_tes_irre_91_pre=="strive" and ver_tes_irre_91_pas=="strove" and ver_tes_irre_91_par=="striven"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("tratar de/esforzarse por-->strive-->strove-->striven")
    print()

    ver_tes_irre_92_pre=input("dar zancadas/caminar con pasos largos in present in english?: ")
    ver_tes_irre_92_pas=input("dar zancadas/caminar con pasos largos in past in english?: ")
    ver_tes_irre_92_par=input("dar zancadas/caminar con pasos largos in past participle in english?: ")
    if(ver_tes_irre_92_pre=="stride" and ver_tes_irre_92_pas=="strode" and ver_tes_irre_92_par=="stridden"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("dar zancadas/caminar con pasos largos-->stride-->strode-->stridden")
    print()

    ver_tes_irre_93_pre=input("aniquilar/destruir/golpear/batir in present in english?: ")
    ver_tes_irre_93_pas=input("aniquilar/destruir/golpear/batir in past in english?: ")
    ver_tes_irre_93_par=input("aniquilar/destruir/golpear/batir in past participle in english?: ")
    if(ver_tes_irre_93_pre=="smite" and ver_tes_irre_93_pas=="smote" and ver_tes_irre_93_par=="smitten"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("aniquilar/destruir/golpear/batir-->smite-->smote-->smitten")
    print()

    ver_tes_irre_94_pre=input("hablar in present in english?: ")
    ver_tes_irre_94_pas=input("hablar in past in english?: ")
    ver_tes_irre_94_par=input("hablar in past participle in english?: ")
    if(ver_tes_irre_94_pre=="speak" and ver_tes_irre_94_pas=="spoke" and ver_tes_irre_94_par=="spoken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("hablar-->speak-->spoke-->spoken")
    print()

    ver_tes_irre_95_pre=input("robar in present in english?: ")
    ver_tes_irre_95_pas=input("robar in past in english?: ")
    ver_tes_irre_95_par=input("robar in past participle in english?: ")
    if(ver_tes_irre_95_pre=="steal" and ver_tes_irre_95_pas=="stole" and ver_tes_irre_95_par=="stolen"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("robar-->steal-->stole-->stolen")
    print()

    ver_tes_irre_96_pre=input("romper/quebrar in present in english?: ")
    ver_tes_irre_96_pas=input("romper/quebrar in past in english?: ")
    ver_tes_irre_96_par=input("romper/quebrar in past participle in english?: ")
    if(ver_tes_irre_96_pre=="break" and ver_tes_irre_96_pas=="broke" and ver_tes_irre_96_par=="broken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("romper/quebrar-->break-->broke-->broken")
    print()

    ver_tes_irre_97_pre=input("despertarse in present in english?: ")
    ver_tes_irre_97_pas=input("despertarse in past in english?: ")
    ver_tes_irre_97_par=input("despertarse in past participle in english?: ")
    if(ver_tes_irre_97_pre=="wake" and ver_tes_irre_97_pas=="woke" and ver_tes_irre_97_par=="woken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("despertarse-->wake-->woke-->woken")
    print()

    ver_tes_irre_98_pre=input("empezar/comenzar/iniciar in present in english?: ")
    ver_tes_irre_98_pas=input("empezar/comenzar/iniciar in past in english?: ")
    ver_tes_irre_98_par=input("empezar/comenzar/iniciar in past participle in english?: ")
    if(ver_tes_irre_98_pre=="begin" and ver_tes_irre_98_pas=="began" and ver_tes_irre_98_par=="begun"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("empezar/comenzar/iniciar-->begin-->began-->begun")
    print()

    ver_tes_irre_99_pre=input("tomar/beber in present in english?: ")
    ver_tes_irre_99_pas=input("tomar/beber in past in english?: ")
    ver_tes_irre_99_par=input("tomar/beber in past participle in english?: ")
    if(ver_tes_irre_99_pre=="drink" and ver_tes_irre_99_pas=="drank" and ver_tes_irre_99_par=="drunk"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("tomar/beber-->drink-->drank-->drunk")
    print()

    ver_tes_irre_100_pre=input("hundir in present in english?: ")
    ver_tes_irre_100_pas=input("hundir in past in english?: ")
    ver_tes_irre_100_par=input("hundir in past participle in english?: ")
    if(ver_tes_irre_100_pre=="sink" and ver_tes_irre_100_pas=="sank" and ver_tes_irre_100_par=="sunk"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("hundir-->sink-->sank-->sunk")
    print()

    ver_tes_irre_101_pre=input("apestar in present in english?: ")
    ver_tes_irre_101_pas=input("apestar in past in english?: ")
    ver_tes_irre_101_par=input("apestar in past participle in english?: ")
    if(ver_tes_irre_101_pre=="stink" and ver_tes_irre_101_pas=="stank" and ver_tes_irre_101_par=="stunk"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("apestar-->stink-->stank-->stunk")
    print()

    ver_tes_irre_102_pre=input("nadar in present in english?: ")
    ver_tes_irre_102_pas=input("nadar in past in english?: ")
    ver_tes_irre_102_par=input("nadar in past participle in english?: ")
    if(ver_tes_irre_102_pre=="swim" and ver_tes_irre_102_pas=="swam" and ver_tes_irre_102_par=="swum"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("nadar-->swim-->swam-->swum")
    print()

    ver_tes_irre_103_pre=input("brotar/florecer in present in english?: ")
    ver_tes_irre_103_pas=input("brotar/florecer in past in english?: ")
    ver_tes_irre_103_par=input("brotar/florecer in past participle in english?: ")
    if(ver_tes_irre_103_pre=="spring" and ver_tes_irre_103_pas=="sprang" and ver_tes_irre_103_par=="sprung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("brotar/florecer-->spring-->sprang-->sprung")
    print()

    ver_tes_irre_104_pre=input("encogido in present in english?: ")
    ver_tes_irre_104_pas=input("encogido in past in english?: ")
    ver_tes_irre_104_par=input("encogido in past participle in english?: ")
    if(ver_tes_irre_104_pre=="shrink" and ver_tes_irre_104_pas=="shrank" and ver_tes_irre_104_par=="shrunk"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("encogido-->shrink-->shrank-->shrunk")
    print()

    ver_tes_irre_105_pre=input("llamar a/hacer sonar/sonar/timbrar/repicar in present in english?: ")
    ver_tes_irre_105_pas=input("llamar a/hacer sonar/sonar/timbrar/repicar in past in english?: ")
    ver_tes_irre_105_par=input("llamar a/hacer sonar/sonar/timbrar/repicar in past participle in english?: ")
    if(ver_tes_irre_105_pre=="ring" and ver_tes_irre_105_pas=="rang" and ver_tes_irre_105_par=="rung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("llamar a/hacer sonar/sonar/timbrar/repicar-->ring-->rang-->rung")
    print()

    ver_tes_irre_106_pre=input("recorrer/correr/operar/hacer funcionar/ejecutar in present in english?: ")
    ver_tes_irre_106_pas=input("recorrer/correr/operar/hacer funcionar/ejecutar in past in english?: ")
    ver_tes_irre_106_par=input("recorrer/correr/operar/hacer funcionar/ejecutar in past participle in english?: ")
    if(ver_tes_irre_106_pre=="run" and ver_tes_irre_106_pas=="ran" and ver_tes_irre_106_par=="run"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("recorrer/correr/operar/hacer funcionar/ejecutar-->run-->ran-->run")
    print()

    ver_tes_irre_107_pre=input("usar/tener/llevar puesto/tener puesto/ponerse/vestir/usar in present in english?: ")
    ver_tes_irre_107_pas=input("usar/tener/llevar puesto/tener puesto/ponerse/vestir/usar in past in english?: ")
    ver_tes_irre_107_par=input("usar/tener/llevar puesto/tener puesto/ponerse/vestir/usar in past participle in english?: ")
    if(ver_tes_irre_107_pre=="wear" and ver_tes_irre_107_pas=="wore" and ver_tes_irre_107_par=="worn"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("usar/tener/llevar puesto/tener puesto/ponerse/vestir/usar-->wear-->wore-->worn")
    print()

    ver_tes_irre_108_pre=input("maldecir/jurar/decir groserias/decir malas palabras in present in english?: ")
    ver_tes_irre_108_pas=input("maldecir/jurar/decir groserias/decir malas palabras in past in english?: ")
    ver_tes_irre_108_par=input("maldecir/jurar/decir groserias/decir malas palabras in past participle in english?: ")
    if(ver_tes_irre_108_pre=="swear" and ver_tes_irre_108_pas=="swore" and ver_tes_irre_108_par=="sworn"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("maldecir/jurar/decir groserias/decir malas palabras-->swear-->swore-->sworn")
    print()

    ver_tes_irre_109_pre=input("tolerar in present in english?: ")
    ver_tes_irre_109_pas=input("tolerar in past in english?: ")
    ver_tes_irre_109_par=input("tolerar in past participle in english?: ")
    if(ver_tes_irre_109_pre=="bear" and ver_tes_irre_109_pas=="bore" and ver_tes_irre_109_par=="born"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("tolerar-->bear-->bore-->born")
    print()

    ver_tes_irre_110_pre=input("rasgar in present in english?: ")
    ver_tes_irre_110_pas=input("rasgar in past in english?: ")
    ver_tes_irre_110_par=input("rasgar in past participle in english?: ")
    if(ver_tes_irre_110_pre=="tear" and ver_tes_irre_110_pas=="tore" and ver_tes_irre_110_par=="torn"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("rasgar-->tear-->tore-->torn")
    print()

    ver_tes_irre_111_pre=input("agarrar/coger in present in english?: ")
    ver_tes_irre_111_pas=input("agarrar/coger in past in english?: ")
    ver_tes_irre_111_par=input("agarrar/coger in past participle in english?: ")
    if(ver_tes_irre_111_pre=="take" and ver_tes_irre_111_pas=="took" and ver_tes_irre_111_par=="taken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("agarrar/coger-->take-->took-->taken")
    print()

    ver_tes_irre_112_pre=input("emprender/comenzar/empezar in present in english?: ")
    ver_tes_irre_112_pas=input("emprender/comenzar/empezar in past in english?: ")
    ver_tes_irre_112_par=input("emprender/comenzar/empezar in past participle in english?: ")
    if(ver_tes_irre_112_pre=="undertake" and ver_tes_irre_112_pas=="undertook" and ver_tes_irre_112_par=="undertaken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("emprender/comenzar/empezar-->undertake-->undertook-->undertaken")
    print()

    ver_tes_irre_113_pre=input("participar in present in english?: ")
    ver_tes_irre_113_pas=input("participar in past in english?: ")
    ver_tes_irre_113_par=input("participar in past participle in english?: ")
    if(ver_tes_irre_113_pre=="partake" and ver_tes_irre_113_pas=="partook" and ver_tes_irre_113_par=="partaken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("practicar-->partake-->partook-->partaken")
    print()

    ver_tes_irre_114_pre=input("menear in present in english?: ")
    ver_tes_irre_114_pas=input("menear in past in english?: ")
    ver_tes_irre_114_par=input("menear in past participle in english?: ")
    if(ver_tes_irre_114_pre=="shake" and ver_tes_irre_114_pas=="shook" and ver_tes_irre_114_par=="shaken"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("menear-->shake-->shook-->shaken")
    print()

    ver_tes_irre_115_pre=input("conseguir in present in english?: ")
    ver_tes_irre_115_pas=input("conseguir in past in english?: ")
    ver_tes_irre_115_par=input("conseguir in past participle in english?: ")
    if(ver_tes_irre_115_pre=="get" and ver_tes_irre_115_pas=="got" and ver_tes_irre_115_par=="gotten"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("conseguir-->get-->got-->gotten")
    print()

    ver_tes_irre_116_pre=input("olvidar in present in english?: ")
    ver_tes_irre_116_pas=input("olvidar in past in english?: ")
    ver_tes_irre_116_par=input("olvidar in past participle in english?: ")
    if(ver_tes_irre_116_pre=="forget" and ver_tes_irre_116_pas=="forgot" and ver_tes_irre_116_par=="forgotten"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("olvidar-->forget-->forgot-->forgotten")
    print()

    ver_tes_irre_117_pre=input("dar in present in english?: ")
    ver_tes_irre_117_pas=input("dar in past in english?: ")
    ver_tes_irre_117_par=input("dar in past participle in english?: ")
    if(ver_tes_irre_117_pre=="give" and ver_tes_irre_117_pas=="gave" and ver_tes_irre_117_par=="given"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("dar-->give-->gave-->given")
    print()

    ver_tes_irre_118_pre=input("perdoname in present in english?: ")
    ver_tes_irre_118_pas=input("perdoname in past in english?: ")
    ver_tes_irre_118_par=input("perdoname in past participle in english?: ")
    if(ver_tes_irre_118_pre=="forgive" and ver_tes_irre_118_pas=="forgave" and ver_tes_irre_118_par=="forgiven"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("perdoname-->forgive-->forgave-->forgiven")
    print()

    ver_tes_irre_119_pre=input("prohibir in present in english?: ")
    ver_tes_irre_119_pas=input("prohibir in past in english?: ")
    ver_tes_irre_119_par=input("prohibir in past participle in english?: ")
    if(ver_tes_irre_119_pre=="forbid" and ver_tes_irre_119_pas=="forbade" and ver_tes_irre_119_par=="forbidden"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("prohibir-->forbid-->forbade-->forbidden")
    print()

    ver_tes_irre_120_pre=input("conocer/saber in present in english?: ")
    ver_tes_irre_120_pas=input("conocer/saber in past in english?: ")
    ver_tes_irre_120_par=input("conocer/saber in past participle in english?: ")
    if(ver_tes_irre_120_pre=="know" and ver_tes_irre_120_pas=="knew" and ver_tes_irre_120_par=="known"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("conocer/saber-->know-->knew-->known")
    print()

    ver_tes_irre_121_pre=input("crecer/hacerse más alto/expandirse/aumentar/desarrollarse in present in english?: ")
    ver_tes_irre_121_pas=input("crecer/hacerse más alto/expandirse/aumentar/desarrollarse in past in english?: ")
    ver_tes_irre_121_par=input("crecer/hacerse más alto/expandirse/aumentar/desarrollarse in past participle in english?: ")
    if(ver_tes_irre_121_pre=="grow" and ver_tes_irre_121_pas=="grew" and ver_tes_irre_121_par=="grown"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("crecer/hacerse más alto/expandirse/aumentar/desarrollarse-->grow-->grew-->grown")
    print()

    ver_tes_irre_122_pre=input("tirar/lanzar in present in english?: ")
    ver_tes_irre_122_pas=input("tirar/lanzar in past in english?: ")
    ver_tes_irre_122_par=input("tirar/lanzar in past participle in english?: ")
    if(ver_tes_irre_122_pre=="throw" and ver_tes_irre_122_pas=="threw" and ver_tes_irre_122_par=="thrown"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("tirar/lanzar-->throw-->threw-->thrown")
    print()

    ver_tes_irre_123_pre=input("soplar/explotar in present in english?: ")
    ver_tes_irre_123_pas=input("soplar/explotar in past in english?: ")
    ver_tes_irre_123_par=input("soplar/explotar in past participle in english?: ")
    if(ver_tes_irre_123_pre=="blow" and ver_tes_irre_123_pas=="blew" and ver_tes_irre_123_par=="blown"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("soplar/explotar-->blow-->blew-->blown")
    print()

    ver_tes_irre_124_pre=input("dibujar in present in english?: ")
    ver_tes_irre_124_pas=input("dibujar in past in english?: ")
    ver_tes_irre_124_par=input("dibujar in past participle in english?: ")
    if(ver_tes_irre_124_pre=="draw" and ver_tes_irre_124_pas=="drew" and ver_tes_irre_124_par=="drawn"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("dibujar-->draw-->drew-->drawn")
    print()

    ver_tes_irre_125_pre=input("retirar(de un cajero) in present in english?: ")
    ver_tes_irre_125_pas=input("retirar(de un cajero) in past in english?: ")
    ver_tes_irre_125_par=input("retirar(de un cajero) in past participle in english?: ")
    if(ver_tes_irre_125_pre=="withdraw" and ver_tes_irre_125_pas=="withdrew" and ver_tes_irre_125_par=="withdrawn"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("retirar(de un cajero)-->withdraw-->withdrew-->withdrawn")
    print()

    ver_tes_irre_126_pre=input("excederse in present in english?: ")
    ver_tes_irre_126_pas=input("excederse in past in english?: ")
    ver_tes_irre_126_par=input("excederse in past participle in english?: ")
    if(ver_tes_irre_126_pre=="overdraw" and ver_tes_irre_126_pas=="overdrew" and ver_tes_irre_126_par=="overdrawn"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("excederse-->overdraw-->overdrew-->overdrawn")
    print()

    ver_tes_irre_127_pre=input("volar in present in english?: ")
    ver_tes_irre_127_pas=input("volar in past in english?: ")
    ver_tes_irre_127_par=input("volar in past participle in english?: ")
    if(ver_tes_irre_127_pre=="fly" and ver_tes_irre_127_pas=="flew" and ver_tes_irre_127_par=="flown"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("volar-->fly-->flew-->flown")
    print()

    ver_tes_irre_128_pre=input("llego/vengo in present in english?: ")
    ver_tes_irre_128_pas=input("llego/vengo in past in english?: ")
    ver_tes_irre_128_par=input("llego/vengo in past participle in english?: ")
    if(ver_tes_irre_128_pre=="come" and ver_tes_irre_128_pas=="came" and ver_tes_irre_128_par=="come"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("llego/vengo-->come-->came-->come")
    print()

    ver_tes_irre_129_pre=input("volverse/convertirse en/hacerse in present in english?: ")
    ver_tes_irre_129_pas=input("volverse/convertirse en/hacerse in past in english?: ")
    ver_tes_irre_129_par=input("volverse/convertirse en/hacerse in past participle in english?: ")
    if(ver_tes_irre_129_pre=="become" and ver_tes_irre_129_pas=="became" and ver_tes_irre_129_par=="become"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("volverse/convertirse en/hacerse-->become-->became-->become")
    print()

    ver_tes_irre_130_pre=input("superar/vencer in present in english?: ")
    ver_tes_irre_130_pas=input("superar/vencer in past in english?: ")
    ver_tes_irre_130_par=input("superar/vencer in past participle in english?: ")
    if(ver_tes_irre_130_pre=="overcome" and ver_tes_irre_130_pas=="overcame" and ver_tes_irre_130_par=="overcome"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("superar/vencer-->overcome-->overcame-->overcome")
    print()

    ver_tes_irre_131_pre=input("ver in present in english?: ")
    ver_tes_irre_131_pas=input("ver in past in english?: ")
    ver_tes_irre_131_par=input("ver in past participle in english?: ")
    if(ver_tes_irre_131_pre=="see" and ver_tes_irre_131_pas=="saw" and ver_tes_irre_131_par=="seen"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("ver-->see-->saw-->seen")
    print()

    ver_tes_irre_132_pre=input("predecir/prever/anticipar in present in english?: ")
    ver_tes_irre_132_pas=input("predecir/prever/anticipar in past in english?: ")
    ver_tes_irre_132_par=input("predecir/prever/anticipar in past participle in english?: ")
    if(ver_tes_irre_132_pre=="foresee" and ver_tes_irre_132_pas=="foresaw" and ver_tes_irre_132_par=="foreseen"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("predecir/prever/anticipar-->foresee-->foresaw-->foreseen")
    print()

    ver_tes_irre_133_pre=input("supervisar/monitorear/monitorizar in present in english?: ")
    ver_tes_irre_133_pas=input("supervisar/monitorear/monitorizar in past in english?: ")
    ver_tes_irre_133_par=input("supervisar/monitorear/monitorizar in past participle in english?: ")
    if(ver_tes_irre_133_pre=="oversee" and ver_tes_irre_133_pas=="oversaw" and ver_tes_irre_133_par=="overseen"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("supervisar/monitorear/monitorizar-->oversee-->oversaw-->overseen")
    print()

    ver_tes_irre_134_pre=input("termine in present in english?: ")
    ver_tes_irre_134_pas=input("termine in past in english?: ")
    ver_tes_irre_134_par=input("termine in past participle in english?: ")
    if(ver_tes_irre_134_pre=="do" and ver_tes_irre_134_pas=="did" and ver_tes_irre_134_par=="done"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("termine-->do-->did-->done")
    print()

    ver_tes_irre_135_pre=input("irse/partir in present in english?: ")
    ver_tes_irre_135_pas=input("irse/partir in past in english?: ")
    ver_tes_irre_135_par=input("irse/partir in past participle in english?: ")
    if(ver_tes_irre_135_pre=="go" and ver_tes_irre_135_pas=="went" and ver_tes_irre_135_par=="gone"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("irse/partir-->go-->went-->gone")
    print()

    ver_tes_irre_136_pre=input("deshacer in present in english?: ")
    ver_tes_irre_136_pas=input("deshacer in past in english?: ")
    ver_tes_irre_136_par=input("deshacer in past participle in english?: ")
    if(ver_tes_irre_136_pre=="undo" and ver_tes_irre_136_pas=="undid" and ver_tes_irre_136_par=="undone"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("deshacer-->undo-->undid-->undone")
    print()

    ver_tes_irre_137_pre=input("hacer de mas in present in english?: ")
    ver_tes_irre_137_pas=input("hacer de mas in past in english?: ")
    ver_tes_irre_137_par=input("hacer de mas in past participle in english?: ")
    if(ver_tes_irre_137_pre=="overdo" and ver_tes_irre_137_pas=="overdid" and ver_tes_irre_137_par=="overdone"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("hacer de más-->overdo-->overdid-->overdone")
    print()

    ver_tes_irre_138_pre=input("pasar por dificultades/sufrir in present in english?: ")
    ver_tes_irre_138_pas=input("pasar por dificultades/sufrir in past in english?: ")
    ver_tes_irre_138_par=input("pasar por dificultades/sufrir in past participle in english?: ")
    if(ver_tes_irre_138_pre=="undergo" and ver_tes_irre_138_pas=="underwent" and ver_tes_irre_138_par=="undergone"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("pasar por dificultades/sufrir-->undergo-->underwent-->undergone")
    print()

    ver_tes_irre_139_pre=input("comer/alimentarse in present in english?: ")
    ver_tes_irre_139_pas=input("comer/alimentarse in past in english?: ")
    ver_tes_irre_139_par=input("comer/alimentarse in past participle in english?: ")
    if(ver_tes_irre_139_pre=="eat" and ver_tes_irre_139_pas=="ate" and ver_tes_irre_139_par=="eaten"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("comer/alimentarse-->eat-->ate-->eaten")
    print()

    ver_tes_irre_140_pre=input("caerse/caer in present in english?: ")
    ver_tes_irre_140_pas=input("caerse/caer in past in english?: ")
    ver_tes_irre_140_par=input("caerse/caer in past participle in english?: ")
    if(ver_tes_irre_140_pre=="fall" and ver_tes_irre_140_pas=="fell" and ver_tes_irre_140_par=="fallen"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("caerse/caer-->fall-->fell-->fallen")
    print()

    ver_tes_irre_141_pre=input("ser/estar/tener in present in english?: ")
    ver_tes_irre_141_pas=input("ser/estar/tener in past in english?: ")
    ver_tes_irre_141_par=input("ser/estar/tener in past participle in english?: ")
    if(ver_tes_irre_141_pre=="be" and ver_tes_irre_141_pas=="was/were" and ver_tes_irre_141_par=="been"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("ser/estar/tener-->be-->was/were-->been")
    print()

    ver_tes_irre_142_pre=input("cantar in present in english?: ")
    ver_tes_irre_142_pas=input("cantar in past in english?: ")
    ver_tes_irre_142_par=input("cantar in past participle in english?: ")
    if(ver_tes_irre_142_pre=="sing" and ver_tes_irre_142_pas=="sang" and ver_tes_irre_142_par=="sung"):
        print("correct")
        var_tes_ver_irre+=1
    else:
        print("incorrect")
    print()
    print("verbo --> verb in present --> verb in past --> verb in past participle")
    print("cantar-->sing-->sang-->sung")

    if(var_tes_ver_irre==142):
        cor_or_inc_irre=True

    print()
    
    return cor_or_inc_irre

def verb():
    var_verb=0
    vec_verb=["----","----","----","----"]
    corr_or_inco=False
    wh_ver=input("what is verb?: ")
    if(wh_ver=="a verb is a word expressing action or state"):
        print("correct")
        var_verb+=1
        vec_verb[0]="what is a verb"
    else:
        print("incorrect")
    print()
    print("what is a verb?-->a verb is a word expressing action or state")
    print()

    print("test verbs")
    var_tes_ver=test_verbs()
    if(var_tes_ver):
        print("correct")
        var_verb+=1
        vec_verb[1]="test verbs"
    else:
        print("incorrect")    
    print()

    print("test verbs regulars")
    var_tes_ver_reg=test_verbs_regular()
    if(var_tes_ver_reg):
        print("correct")
        var_verb+=1
        vec_verb[2]="test verbs regular"
    else:
        print("incorrect")
    print()
    
    print("test verbs irregulars")
    var_tes_ver_irr=test_verbs_irregulars()
    if(var_tes_ver_irr):
        print("correct")
        var_verb+=1
        vec_verb[3]="test verbs irregulars"
    else:
        print("incorrect")
    
    if(var_verb==4):
        corr_or_inco=True

    recorrer_lista(vec_verb)

    return corr_or_inco

def simple_test():
    good_sim_tes=0
    tru_or_fal_sim=False
    exa_1_sim=input("Yo comí in past: ")
    exa_2_sim=input("yo como in present: ")
    exa_3_sim=input("voy a comer in future: ")
    if(exa_1_sim=="i ate" and exa_2_sim=="i eat" and exa_3_sim=="i will eat"):
        print("perfect")
        good_sim_tes+=1
    else:
        print("incorrect")
    print()

    #Respuestas
    print("Answer: ")
    print("Yo comí in past: i ate")
    print("yo como in present: i eat ")
    print("voy a comer in future: i will eat")
    print()

    exa_4_sim=input("Yo como in affirmative and present simple: ")
    exa_5_sim=input("Él come in affirmative and present simple: ")
    exa_6_sim=input("Tú comes in affirmative and present simple: ")
    if(exa_4_sim=="i eat" and exa_5_sim=="he eats" and exa_6_sim=="you eat"):
        print("correct")
        good_sim_tes+=1
    else:
        print("incorrect")
    print()

    print("Answers: ")
    print("Yo como in affirmative and present simple: i eat")
    print("Él come in affirmative and present simple: he eats ")
    print("Tú comes in affirmative and present simple: you eat ")
    print()

    exa_7_sim=input("tú no comes in negative and present simple: ")
    exa_8_sim=input("no comistes in negative and past simple: ")
    if((exa_7_sim=="you don't eat" or exa_7_sim=="you do not eat") and (exa_8_sim=="you didn't eat" or exa_8_sim=="you did not eat") ):
        print("correct")
        good_sim_tes+=1
    else:
        print("incorrect")
    print()

    print("Answers: ")
    print("tú no comes in negative and present simple: you don't eat OR you do not eat")
    print("no comistes in negative and past simple: you didn't eat OR you did not eat")
    print()


    exa_9_sim=input("¿tú comes?/¿comes? in interrogative and present simple: ")
    exa_10_sim=input("¿comiste? in interrogative and past simple: ")
    if(exa_9_sim=="do you eat?" and exa_10_sim=="did you eat?"):
        print("correct")
        good_sim_tes+=1
    else:
        print("incorrect")
    print()

    #RESPUESTAS 
    print("Answers: ")
    print("¿tú comes?/¿comes? in interrogative and present simple: do you eat?")
    print("¿comiste? in interrogative and past simple: did you eat?")
    print()


    if(good_sim_tes==4):        
        tru_or_fal_sim=True

    return tru_or_fal_sim

def continuo_test():
    good_con_tes=0
    tru_or_fal_con=False

    exa_1_con=input("estaba comiendo in past and continuos: ")
    exa_2_con=input("estoy comiendo in present and continuos: ")
    exa_3_con=input("estaré comiendo in future and continuos: ")
    if(exa_1_con=="i was eating" and exa_2_con=="i am eating" and exa_3_con=="i will be eating"):
        print("correct")
        good_con_tes+=1
    else:
        print("incorrect")
    print()

    print("Answers: ")
    print("estaba comiendo in past and continuos: i was eating")
    print("estoy comiendo in present and continuos: i am eating")
    print("estaré comiendo in future and continuos: i will be eating")
    print()

    exa_4_con=input("yo estoy comiendo in affirmative and present continuos: ")
    exa_5_con=input("tú estás comiendo in affirmative and present continuos: ")
    if((exa_4_con=="i am eating" or exa_4_con=="i'm eating") and (exa_5_con=="you are eating" or exa_5_con=="you're eating") ):
        print("correct")
        good_con_tes+=1
    else:
        print("incorrect")
    print()

    print("Answers: ")
    print("yo estoy comiendo in affirmative and present continuos: i am eating OR i'm eating")
    print("tú estás comiendo in affirmative and present continuos: you are eating OR you're eating")
    print()

    if(good_con_tes==2):
        tru_or_fal_con=True

    return tru_or_fal_con

def perfect_test():
    good_per_tes=0
    tru_or_fal=False

    exa_1_per=input("tuve in past and perfect: ")
    exa_2_per=input("tengo in present and perfect: ")
    exa_3_per=input("tendré in past and perfect: ")
    if(exa_1_per=="i had" and exa_2_per=="i have" and exa_3_per=="i will have"):
        print("correct")
        good_per_tes+=1
    else:
        print("incorrect")
    print()

    print("Answers: ")
    print("tuve in past and perfect: I had")
    print("tengo in present and perfect: I have")
    print("tendré in past and perfect: I will have")
    print()

    exa_4_per=input("yo he comido in affirmative and present perfect: ")
    exa_5_per=input("nosotros hemos comido in affirmative and present perfect: ")
    exa_6_per=input("ella ha comido in affirmative and present perfect: ")
    if(exa_4_per=="i have eaten" and exa_5_per=="we have eaten" and exa_6_per=="she has eaten"):
        print("correct")
        good_per_tes+=1
    else:
        print("incorrect")
    print()

    print("Answers: ")
    print("yo he comido in affirmative and present perfect: I have eaten")
    print("nosotros hemos comido in affirmative and present perfect: We have eaten")
    print("ella ha comido in affirmative and present perfect: She has eaten")
    print()
    
    if(good_per_tes==2):
        tru_or_fal=True

    return tru_or_fal

def aux_verb():
    good_aux_verb=0
    tru_or_fal_aux_ver=False

    tim_ver=input("tell me the tenses in english: ")
    if(tim_ver=="past/present/future"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    asp_ver=input("what are the aspects of each tense: ")
    if(asp_ver=="simple/continuous/perfect/continuous perfect"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    aux_sim_str=input("how is the structure of the simple: ")
    if(aux_sim_str=="to do"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    aux_con_str=input("how is the structure of the continuo: ")
    if(aux_con_str=="to-be+gerundio"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    aux_per_str=input("how is the structure of the perfect: ")
    if(aux_per_str=="to have+past participle"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    aux_con_per_str=input("how is the structure of the continuo perfect: ")
    if(aux_con_per_str=="to-be+to have"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    
    #RESPUESTAS
    print("Answers: ")
    print("tell me the tenses in english: past/present/future")
    print("what are the aspects of each tense: simple/continuous/perfect/continuous perfect ")
    print("how is the structure of the simple: to do")
    print("how is the structure of the continuo: to-be+gerundio")
    print("how is the structure of the perfect: to have+past participle")
    print("how is the structure of the continuo perfect: to-be+to have")
    print()

    print("simple test:")
    tes_sim=simple_test()
    if(tes_sim):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    print("continuo test:")
    tes_con=continuo_test()
    if(tes_con):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    print("perfect test:")
    tes_per=perfect_test()
    if(tes_per):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
    print()

    if(good_aux_verb==9):
        tru_or_fal_aux_ver=True
        print("correct")

    return tru_or_fal_aux_ver

def adverb():
    answer_wh_adv=input("what is adverb?: ")
    if(answer_wh_adv=="an adverb is a word that modifies or describes a verb"):
        print("correct ")
    else:
        print("incorrect")
    print()
    print("what is adverb?: -->an adverb is a word that modifies or describes a verb")
    print()


    point=False
    list_test_adverb_place=["------","------","------","------","------","------","------","------","------"]
    list_test_adverb_time=["------","------","------","------","------","------","------","------","------"]
    list_test_adverb_mode=["------","------","------","------","------",]
    list_test_adverb_amount=["------","------","------","------","------","------","------",]
    list_test_adverb_affirmation=["------","------"]
    list_test_adverb_denial=["------","------"]
    list_test_adverb_doubt=["------","------"]
    good=0
    print("Adverb place")
    print('write aquí in english')
    here_word=input()
    if(here_word=='here'):
        print('correct')
        good=good+1
        list_test_adverb_place[0]='here'
    else:
        print('incorrect')
    print('')

    print('write ahí in english')
    there_word=input()
    if(there_word=='there'):
        print('correct')
        good=good+1
        list_test_adverb_place[1]='there'
    else:
        print('incorrect')
    print('')

    print('write allí in english')
    there_word=input()
    if(there_word=='there'):
        print('correct')
        good=good+1
        list_test_adverb_place[2]='there'
    else:
        print('incorrect')
    print('')

    print('write cerca in english')
    near_word=input()
    if(near_word=='near'):
        print('correct')
        good=good+1
        list_test_adverb_place[3]='near'
    else:
        print('incorrect')
    print('')

    print('write lejos in english')
    far_word=input()
    if(far_word=='far'):
        print('correct')
        good=good+1
        list_test_adverb_place[4]='far'
    else:
        print('incorrect')
    print('')

    print('write arriba in english')
    up_word=input()
    if(up_word=='up'):
        print('correct')
        good=good+1
        list_test_adverb_place[5]='up'
    else:
        print('incorrect')
    print('')

    print('write abajo in english')
    down_word=input()
    if(down_word=='down'):
        print('correct')
        good=good+1
        list_test_adverb_place[6]='down'
    else:
        print('incorrect')
    print('')

    print('write adentro in english')
    inside_word=input()
    if(inside_word=='inside'):
        print('correct')
        good=good+1
        list_test_adverb_place[7]='inside'
    else:
        print('incorrect')
    print('')

    print('write afuera in english')
    outside_word=input()
    if(outside_word=='outside'):
        print('correct')
        good=good+1
        list_test_adverb_place[8]='outside'
    else:
        print('incorrect')
    print('')
    
    print("Adverb time")
    print('write ahora in english')
    now_word=input()
    if(now_word=='now'):
        print('correct')
        good=good+1
        list_test_adverb_time[0]='now'
    else:
        print('incorrect')
    print('')

    print('write luego in english')
    then_word=input()
    if(then_word=='then'):
        print('correct')
        good=good+1
        list_test_adverb_time[1]='then'
    else:
        print('incorrect')
    print('')

    print('write después in english')
    after_word=input()
    if(after_word=='after'):
        print('correct')
        good=good+1
        list_test_adverb_time[2]='after'
    else:
        print('incorrect')
    print('')

    print('write pronto in english')
    promptly_word=input()
    if(promptly_word=='promptly'):
        print('correct')
        good=good+1
        list_test_adverb_time[3]='promptly'
    else:
        print('incorrect')
    print('')

    print('write tarde in english')
    late_word=input()
    if(late_word=='late'):
        print('correct')
        good=good+1
        list_test_adverb_time[4]='late'
    else:
        print('incorrect')
    print('')

    print('write ayer in english')
    yesterday_word=input()
    if(yesterday_word=='yesterday'):
        print('correct')
        good=good+1
        list_test_adverb_time[5]='yesterday'
    else:
        print('incorrect')
    print('')

    print('write hoy in english')
    today_word=input()
    if(today_word=='today'):
        print('correct')
        good=good+1
        list_test_adverb_time[6]='today'
    else:
        print('incorrect')
    print('')

    print('write mañana in english')
    tomorrow_word=input()
    if(tomorrow_word=='tomorrow'):
        print('correct')
        good=good+1
        list_test_adverb_time[7]='tomorrow'
    else:
        print('incorrect')
    print('')

    print("Adverb mode")
    print('write bien in english')
    well_word=input()
    if(well_word=='well'):
        print('correct')
        good=good+1
        list_test_adverb_mode[0]='well'
    else:
        print('incorrect')
    print('')

    print('write mal in english')
    wrong_word=input()
    if(wrong_word=='wrong'):
        print('correct')
        good=good+1
        list_test_adverb_mode[1]='wrong'
    else:
        print('incorrect')
    print('')

    print('write así in english')
    so_word=input()
    if(so_word=='so'):
        print('correct')
        good=good+1
        list_test_adverb_mode[2]='so'
    else:
        print('incorrect')
    print('')

    print('write deprisa in english')
    fast_word=input()
    if(fast_word=='fast'):
        print('correct')
        good=good+1
        list_test_adverb_mode[3]='fast'
    else:
        print('incorrect')
    print('')

    print('write despacio in english')
    slowly_word=input()
    if(slowly_word=='slowly'):
        print('correct')
        good=good+1
        list_test_adverb_mode[4]='slowly'
    else:
        print('incorrect')
    print('')

    print("Adverb amount")
    print('write mucho in english')
    much_word=input()
    if(much_word=='much'):
        print('correct')
        good=good+1
        list_test_adverb_amount[0]='much'
    else:
        print('incorrect')
    print('')

    print('write poco in english')
    little_word=input()
    if(little_word=='little'):
        print('correct')
        good=good+1
        list_test_adverb_amount[1]='little'
    else:
        print('incorrect')
    print('')

    print('write bastante in english')
    quite_word=input()
    if(quite_word=='quite'):
        print('correct')
        good=good+1
        list_test_adverb_amount[2]='quite'
    else:
        print('incorrect')
    print('')

    print('write casi in english')
    almost_word=input()
    if(almost_word=='almost'):
        print('correct')
        good=good+1
        list_test_adverb_amount[3]='almost'
    else:
        print('incorrect')
    print('')

    print('write más in english')
    more_word=input()
    if(more_word=='more'):
        print('correct')
        good=good+1
        list_test_adverb_amount[4]='more'
    else:
        print('incorrect')
    print('')

    print('write menos in english')
    less_word=input()
    if(less_word=='less'):
        print('correct')
        good=good+1
        list_test_adverb_amount[5]='less'
    else:
        print('incorrect')
    print('')       

    print('write muy in english')
    very_word=input()
    if(very_word=='very'):
        print('correct')
        good=good+1
        list_test_adverb_amount[6]='very'
    else:
        print('incorrect')
    print('')

    print("Adverb affirmation")
    print('write sí in english')
    yes_word=input()
    if(yes_word=='yes'):
        print('correct')
        good=good+1
        list_test_adverb_affirmation[0]='yes'
    else:
        print('incorrect')
    print('')

    print('write también in english')
    also_word=input()
    if(also_word=='also'):
        print('correct')
        good=good+1
        list_test_adverb_affirmation[1]='also'
    else:
        print('incorrect')
    print('')

    print("Adverb denial")
    print('write no in english')
    no_word=input()
    if(no_word=='no'):
        print('correct')
        good=good+1
        list_test_adverb_denial[0]='no'
    else:
        print('incorrect')
    print('')

    print('write tampoco in english')
    either_word=input()
    if(either_word=='either'):
        print('correct')
        good=good+1
        list_test_adverb_denial[1]='either'
    else:
        print('incorrect')
    print('')

    print("Adverb doubt")
    print('write quizás in english')
    possibly_maybe_word=input()
    if(possibly_maybe_word=='possibly/maybe'):
        print('correct')
        good=good+1
        list_test_adverb_doubt[0]='possibly/maybe'
    else:
        print('incorrect')
    print('')

    print('write acaso in english')
    perhaps_word=input()
    if(perhaps_word=='perhaps'):
        print('correct')
        good=good+1
        list_test_adverb_doubt[1]='perhaps'
    else:
        print('incorrect')
    print('')

    if(good==35):
        point=True
        print("congratulations")
    else:
        print("you not have point")

    return point
            
def simple_rules():
    print("SIMPLE RULES")
    vec_sim_rul=["------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------"]
    good_sim_rul=0
    bin_sim_rul=False
    noun_ans_sim_rul=input("how to identify the noun?: ")
    if(noun_ans_sim_rul=="object/place/animal/personal name"):
        print("correct")
        vec_sim_rul[0]="noun"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    mr_senor=input("how do you say señor: ")
    if(mr_senor=="mr"):
        print("correct")
        vec_sim_rul[1]="mr/señor"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    mr_senora=input("how do you say señora: ")
    if(mr_senora=="mrs"):
        print("correct")
        vec_sim_rul[2]="mrs/señora"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    pro_ans_sim_rul=input("what are the pronouns?: ")
    if(pro_ans_sim_rul=="i/you/he/she/it/we/you/they"):
        print("correct")
        vec_sim_rul[1]="pronouns"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    pro_fir_sin_ans=input("what are the pronouns in 1st person singular: ")
    if(pro_fir_sin_ans=="i"):
        print("correct")
        vec_sim_rul[2]="Pronouns 1st singular"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    pro_fir_plu_ans=input("what are the pronouns in 1st person plural: ")
    if(pro_fir_plu_ans=="we"):
        print("correct")
        vec_sim_rul[3]="pronouns 1st plural"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    pro_sec_sin_ans=input("what are the pronouns in 2nd person singular: ")
    if(pro_sec_sin_ans=="you"):
        print("correct")
        vec_sim_rul[4]="pronouns 2nd singular"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    pro_sec_plu_ans=input("what are the pronouns in 2nd person plural: ")
    if(pro_sec_plu_ans=="you"):
        print("correct")
        vec_sim_rul[5]="pronouns 2nd plural"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    pro_thi_sin_ans=input("what are the pronouns in 3rd person singular: ")
    if(pro_thi_sin_ans=="he/she/it"):
        print("correct")
        vec_sim_rul[6]="pronouns 3rd singular"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()


    pro_thi_plu_ans=input("what are the pronouns in 3rd person plural: ")
    if(pro_thi_plu_ans=="they"):
        print("correct")
        vec_sim_rul[7]="pronouns 3rd plural"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    adj_ide_ans_sim_rul=input("how to identify the adjective?: ")
    adj_wha_ans_sim_rul=input("what are the those characteristics and qualities?: ")
    if(adj_ide_ans_sim_rul=="quality/characteristic" and adj_wha_ans_sim_rul=="form/size/color/origin"):
        print("correct")
        vec_sim_rul[8]="adjective"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    art_ide_ans_sim_rul=input("how to identify the article?: ")
    art_wh_ans_sim_rul=input("what are the articles?: ")
    if(art_wh_ans_sim_rul=="a/an/the" and art_ide_ans_sim_rul=="define the noun"):
        print("correct")
        vec_sim_rul[9]="article"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    nou_and_adj_rul_ans_sim_rul=input("what is the rule of nouns and adjectives?: ")
    if(nou_and_adj_rul_ans_sim_rul=="adjective+noun"):
        print("correct")
        vec_sim_rul[10]="rule[noun and adjective]"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    nou_and_art_ans_sim_rul=input("what is the rule of noun and article?: ")
    if(nou_and_art_ans_sim_rul=="article+noun=subject"):
        print("correct")
        vec_sim_rul[11]="rule[noun and article]"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    typ_of_ver_ans_sim_rul=input("what are the types of verbs?: ")
    if(typ_of_ver_ans_sim_rul=="regulars and irregulars"):
        print("correct")
        vec_sim_rul[12]="types of verbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    rul_ver_pas_ans_sim_rul=input("write #1 rule of the verb in the past: ")
    if(rul_ver_pas_ans_sim_rul=="ed is never pronounced"):
        print("correct")
        vec_sim_rul[13]="rule of the verb in past"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    inf_ver_ans_sim_rul=input("what is the rule of the infinitive verb?: ")
    if(inf_ver_ans_sim_rul=="to+verb"):
        print("correct")
        vec_sim_rul[14]="infinitive verb"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    ger_ver_ans_sim_rul=input("what is the rule of the gerund verb?: ")
    if(ger_ver_ans_sim_rul=="verb+ing"):
        print("correct")
        vec_sim_rul[15]="gerund verb"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    aux_ver_ans_sim_rul=input("what are the auxiliary verbs?: ")
    if(aux_ver_ans_sim_rul=="be/do/modals/have(perfect tenses)/verb to-be"):
        print("correct")
        vec_sim_rul[16]="auxiliary verbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    adv_ans_sim_rul=input("how to identify adverbs?: ")
    if(adv_ans_sim_rul=="describes the verb"):
        print("correct")
        vec_sim_rul[17]="adverbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    fre_adv_ide_ans_sim_rul=input("how to idenfify the frequency adverbs?: ")
    fre_adv_wha_ans_sim_rul=input("what are the frequency adverbs?: ")
    if(fre_adv_ide_ans_sim_rul=="intensity/quantity" and fre_adv_wha_ans_sim_rul=="always/often/normally/sometimes/never"):
        print("correct")
        vec_sim_rul[18]="frequency adverbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    prep_ide_ans_sim_rul=input("how to identify the prepositions?: ")
    prep_wha_ans_sim_rul=input("what are the prepositions?: ")
    if(prep_ide_ans_sim_rul=="time/place" and prep_wha_ans_sim_rul=="at/in/on/of/with/that/than/against"):
        print("correct")
        vec_sim_rul[19]="prepositions"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    phr_ver_ans=input("what is the rule of phrasal verbs?: ")
    if(phr_ver_ans=="verb+preposition"):
        print("correct")
        vec_sim_rul[20]="phrasal verbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    tim_exp_ans_sim_rul=input("what are the time expresions?: ")
    if(tim_exp_ans_sim_rul=="today/tomorrow/yesterday/last night"):
        print("correct")
        vec_sim_rul[21]="time expresion"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    con_coo_ans_sim_rul=input("what are the [conjunctions/coordinators]?: ")
    if(con_coo_ans_sim_rul=="fanboys(for/and/nor/but/or/yet/so)"):
        print("correct")
        vec_sim_rul[22]="conjunctions/coordinators"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    con_ans_sim_rul=input("what are the connectors?: ")
    if(con_ans_sim_rul=="preposition/conjunctions-coordinators(fanboys)"):
        print("correct")
        vec_sim_rul[23]="connectors"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    sep_str_ans_sim_rul=input("what are the separate structures? [________[?]_______]: ")
    if(sep_str_ans_sim_rul==",/preposition/conjunctions-coordinators(fanboys)"):
        print("correct")
        vec_sim_rul[24]="separate structures"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    voz_pass_voz_act=input("Rule: voz pasiva --><-- voz activa: ")
    if(voz_pass_voz_act=="passive voice to active voice and active voice to passive voice"):
        print("correct")
        vec_sim_rul[25]="voz passive and active"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()
    
    str_sim_pre_ans=input("what is the structure of the simple present: ")
    if(str_sim_pre_ans=="is/am/are+p.p(verb past participle)"):
        print("correct")
        vec_sim_rul[26]="simple present"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    str_sim_pas_ans=input("what is the structure of the simple past: ")
    if(str_sim_pas_ans=="was/were+p.p(verb past participle)"):
        print("correct")
        vec_sim_rul[27]="simple past"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    str_sim_fut_ans=input("what is the structure of the simple future: ")
    if(str_sim_fut_ans=="will be+p.p(verb past participle)"):
        print("correct")
        vec_sim_rul[28]="simple future"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    str_pre_per_ans=input("what is the structure of the perfect present: ")
    if(str_pre_per_ans=="have/has been+p.p(verb past participle)"):
        print("correct")
        vec_sim_rul[29]="present perfect"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    print()
    print("Answers:")
    recorrer_lista(vec_sim_rul)
    print(f"result: {good_sim_rul}/32")
    if(good_sim_rul==32):
        print("Congratulations, do you have 1 point")
        bin_sim_rul=True
    else:
        print("Incorrect: keep trying")
    
    print()
    list_correct_simple_rules()

def basic_sentence_structure():
    print()
    print("BASIC SENTENCE STRUCTURE")
    answer_bas_sen_str=input("what the basic sentence structure?: ")
    if(answer_bas_sen_str=="subject+verb+object"):
        print("correct")
    else:
        print("incorrect")
    print()  
    print("what the basic sentence structure? -->subject+verb+object")
    print()


