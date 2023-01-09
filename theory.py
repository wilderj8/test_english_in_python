from asyncore import write
from ctypes import pointer

def main_theory():
    abecedary()
    months()
    basic_sentence_structure()

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
    print('bunch--racismo')
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

def list_correct_pronouns():
    print("")
    print("Pronouns:")
    print("i--yo")
    print("you--tú")
    print("he --él")
    print("she--ella")
    print("it--eso")
    print("we--nosotros/as")
    print("you--ustedes")
    print("they--ellas/ellos")
    print()

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
    print("mr.gonzales feeds the dog--she feed it")
    print("mr.smith feeds the cats--he feed them")
    print("mary and charlie talk to my sister and me--they talk to us")

    print()
    print("possessive adjective")
    print("what are possessive adjectives?--a possessive adjective is an adjective that modifies a noun by identifying who has ownership or possession of it")
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

    print()
    print("possessive pronouns")
    print("mine--mía/mío(s)")
    print("yours--tuya/tuyo(s)/suyo(s)")
    print("his--de él/suyo(s)")
    print("hers--de ella/suyo(s)")
    print("ours--nuestra/nuestro(s)")
    print("yours--ustedes")
    print("theirs--ellos/suyo(s)")
    print()
    print("Examples possessive pronouns")
    print("La casa es tuya--the house is yours")
    print("La casa es de él--the house is his")
    print("La casa es de ella--the house is hers")
    print()

    print("reflexives pronouns")
    print("what are reflexives pronouns--these pronouns are used whe we want to refer to ourselves or to something itself")
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
    print("ellos quieren crear un robot que se mueva por sí mismo--they wanto to create a robot that can move by itself")
    print("nos pusimos en gran riesgo en esta situación--we put orselves at great risk in that situation")
    print("ellos se encontraron en serios problemas--they found themselves in serious trouble")
    print("como ustedes mismos pueden ver, esto ha sido muy fácil--as you yourselves can see, this has been very easy")

def list_correct_adjective():
    print("what is a adjective--an adjective is a word that describes the traits,qualities or number of a noun")
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
    print("lightwight--liviano/ligero/peso ligero/de poco peso/persona que se emborracha fácilmente/pelagatos/don nadie")
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
    print("remaining--restante")
    print()
    print("examples")
    print("red car--carro rojo")
    print("red cars--carros rojos")
    print("gata--female cat")
    print("gato--male cat")
    print("i like the green car--me gusta el carro verde")

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
    list_correct_pronouns()
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
    print("pronouns-->i/you/he/she/it/we/you/they")
    print("adjective-->quality-characteristic/form-size-color-origin")
    print("article-->define the noun--> a/an/the")
    print("noun and adjective rule-->adjective+noun")
    print("noun and article rule-->article+noun=subject")
    print("types of verb-->regulars and irregulars")
    print("#1 rule of the verb in the past-->ed is never pronounced")
    print("infinitive verb structure-->to+verb")
    print("gerund verb structure-->verb+ing")
    print("auxiliary verbs-->be/do/modals/have(perfec tenses)")
    print("adverbs-->describes the verb")
    print("frequency adverb--intensity/quantity --> always/often/normally/sometimes/never")
    print("prepositions-->time/place --> in/on/at/with/of/that/than/against")
    print("time expresion-->today/tomorrow/yesterdaylast night")
    print("conjunctions/coordinators-->fanboys(for/and/nor/but/or/yet/so)")
    print("connectors-->preposition/conjunctions-coordinators(fanboys)")
    print("separate structures-->,/preposition/conjunctions-coordinators(fanboys)")

def abecedary():
    good=0
    vec_abe=["------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------",]
    print()
    print("ABECEDARY")
    exit="not"
    while(exit=="not"):
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
        print("you want to see the list of answers, but if you see them the test is over?yes/not")
        see_ans=input()
        if(see_ans=="yes"):
            list_correct_abecedary()
            exit="yes"
        elif(see_ans=="not"):
            print()            
            print("¿you want to leave the abecedary test yes/not?")
            see_ans=input()
            if(see_ans=="yes"):
                exit="yes"
            elif(see_ans=="not"):
                exit="not"

def months():
    good=0
    vec_mon=["------","------","------","------","------","------","------","------","------","------","------","------"]
    print()
    print("MONTHS")
    exit=True
    while(exit):
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
        see_ans=input("you want to see the list of answers, but if you see them the test is over?yes/not: ")
        if(see_ans=="yes"):
            list_correct_months()
            exit=False
        elif(see_ans=="not"):
            print()
            see_ans=input("you want to leave the months test yes/not?: ")
            if(see_ans=="yes"):
                exit=False
            elif(see_ans=="not"):
                exit=True

def noun_subject():
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

    print('write racismo in english')
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

    return point

def pronouns():    
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
    
    exa_4_obj_pro=input("how would the sentence with object pronoun? [mr.gonzales feeds the dog]: ")
    if(exa_4_obj_pro=="she feed it"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    
    exa_5_obj_pro=input("how would the sentence with object pronouns? [mr.smith feeds the cats]: ")
    if(exa_5_obj_pro=="he feed them"):
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
    print("possessive adjective")
    wh_ar_pos_adj=input("what are possessive adjectives?: ")
    if(wh_ar_pos_adj=="a possessive adjective is an adjective that modifies a noun by identifying who has ownership or possession of it"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

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
    print("Reflexives pronouns")
    wha_ref_pro=input("what are reflexives pronouns?: ")
    if(wha_ref_pro=="these pronouns are used when we want to refer to ourselves or to something itself"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")

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

    exa_8_ref_pro=input("how would the sentence with reflexive pronouns? [ellos quieren crear un robot que se mueva por sí mismo]: ")
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

    exa_11_ref_pro=input("how would the sentence with reflexive pronouns? [como ustedes mismos pueden ver, esto ha sido muy fácil]: ")
    if(exa_11_ref_pro=="as you yourselves can see, this has been very easy"):
        print("correct")
        good_pro+=1
    else:
        print("incorrect")
    print()

    if(good_pro==66):
        print("Congratulations, you have a point")
        point=True
    else:
        print("you not have point")
    
    print()
    return point

def adjective():
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
    lightwight_word=input()
    if(lightwight_word=='lightwight'):
        print('correct')
        good=good+1
        list_test_adjective[13]='lightwight'
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

    print('write entero(a)/todo(a) in english')
    entire_word=input()
    if(entire_word=='entire'):
        print('correct')
        good=good+1
        list_test_adjective[37]='entire'
    else:
        print('incorrect')
    print('')

    print('write varios/varias in english')
    several_word=input()
    if(several_word=='several'):
        print('correct')
        good=good+1
        list_test_adjective[38]='several'
    else:
        print('incorrect')
    print('')

    print('write ameno(a)/entretenido(a)/legible in english')
    readable_word=input()
    if(readable_word=='readable'):
        print('correct')
        good=good+1
        list_test_adjective[39]='readable'
    else:
        print('incorrect')
    print('')

    print('write otro/distinto in english')
    another_word=input()
    if(another_word=='another'):
        print('correct')
        good=good+1
        list_test_adjective[40]='another'
    else:
        print('incorrect')
    print('')

    print('write entero/total/todo/completo in english')
    whole_word=input()
    if(whole_word=='whole'):
        print('correct')
        good=good+1
        list_test_adjective[41]='whole'
    else:
        print('incorrect')
    print('')

    print('write complicado/complejo in english')
    complex_word=input()
    if(complex_word=='complex'):
        print('correct')
        good=good+1
        list_test_adjective[42]='complex'
    else:
        print('incorrect')
    print('')

    print('write aquellos/esas/esos in english')
    those_word=input()
    if(those_word=='those'):
        print('correct')
        good=good+1
        list_test_adjective[43]='those'
    else:
        print('incorrect')
    print('')

    print('write más bajo/más corto in english')
    shortest_word=input()
    if(shortest_word=='shortest'):
        print('correct')
        good=good+1
        list_test_adjective[44]='shortest'
    else:
        print('incorrect')
    print('')

    print('write sutil/disimulado/desimulada in english')
    subtle_word=input()
    if(subtle_word=='subtle'):
        print('correct')
        good=good+1
        list_test_adjective[45]='subtle'
    else:
        print('incorrect')
    print('')

    print('write restante in english')
    remaining_word=input()
    if(remaining_word=='remaining'):
        print('correct')
        good=good+1
        list_test_adjective[46]='remaining'
    else:
        print('incorrect')
    print('')

    if(good==45):
        point=True 
        print("congratulations")        
    else:
        print("you not have point")

    return point

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

def adverb():
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
    vec_sim_rul=["------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------","------"]
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

    pro_ans_sim_rul=input("what are the pronouns?: ")
    if(pro_ans_sim_rul=="i/you/he/she/it/we/you/they"):
        print("correct")
        vec_sim_rul[1]="pronouns"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    adj_ide_ans_sim_rul=input("how to identify the adjective?: ")
    adj_wha_ans_sim_rul=input("what are the those characteristics and qualities?: ")
    if(adj_ide_ans_sim_rul=="quality/characteristic" and adj_wha_ans_sim_rul=="form/size/color/origin"):
        print("correct")
        vec_sim_rul[2]="adjective"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    art_ide_ans_sim_rul=input("how to identify the article?: ")
    art_wh_ans_sim_rul=input("what are the articles?: ")
    if(art_wh_ans_sim_rul=="a/an/the" and art_ide_ans_sim_rul=="define the noun"):
        print("correct")
        vec_sim_rul[3]="article"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    nou_and_adj_rul_ans_sim_rul=input("what is the rule of nouns and adjectives?: ")
    if(nou_and_adj_rul_ans_sim_rul=="adjective+noun"):
        print("correct")
        vec_sim_rul[4]="rule[noun and adjective]"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    nou_and_art_ans_sim_rul=input("what is the rule of noun and article?: ")
    if(nou_and_art_ans_sim_rul=="article+noun=subject"):
        print("correct")
        vec_sim_rul[5]="rule[noun and article]"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    typ_of_ver_ans_sim_rul=input("what are the types of verbs?: ")
    if(typ_of_ver_ans_sim_rul=="regulars and irregulars"):
        print("correct")
        vec_sim_rul[6]="types of verbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    rul_ver_pas_ans_sim_rul=input("write #1 rule of the verb in the past: ")
    if(rul_ver_pas_ans_sim_rul=="ed is never pronounced"):
        print("correct")
        vec_sim_rul[7]="rule of the verb in past"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    inf_ver_ans_sim_rul=input("what is the rule of the infinitive verb?: ")
    if(inf_ver_ans_sim_rul=="to+verb"):
        print("correct")
        vec_sim_rul[8]="infinitive verb"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    ger_ver_ans_sim_rul=input("what is the rule of the gerund verb?: ")
    if(ger_ver_ans_sim_rul=="verb+ing"):
        print("correct")
        vec_sim_rul[9]="gerund verb"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    aux_ver_ans_sim_rul=input("what are the auxiliary verbs?: ")
    if(aux_ver_ans_sim_rul=="be/do/modals/have(perfect tenses)"):
        print("correct")
        vec_sim_rul[10]="auxiliary verbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    adv_ans_sim_rul=input("how to identify adverbs?: ")
    if(adv_ans_sim_rul=="describes the verb"):
        print("correct")
        vec_sim_rul[11]="adverbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    fre_adv_ide_ans_sim_rul=input("how to idenfify the frequency adverbs?: ")
    fre_adv_wha_ans_sim_rul=input("what are the frequency adverbs?: ")
    if(fre_adv_ide_ans_sim_rul=="intensity/quantity" and fre_adv_wha_ans_sim_rul=="always/often/normally/sometimes/never"):
        print("correct")
        vec_sim_rul[12]="frequency adverbs"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    prep_ide_ans_sim_rul=input("how to identify the prepositions?: ")
    prep_wha_ans_sim_rul=input("what are the prepositions?: ")
    if(prep_ide_ans_sim_rul=="time/place" and prep_wha_ans_sim_rul=="in/on/at/with/of/that/than/against"):
        print("correct")
        vec_sim_rul[13]="prepositions"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    tim_exp_ans_sim_rul=input("what are the time expresions?: ")
    if(tim_exp_ans_sim_rul=="today/tomorrow/yesterday/last night"):
        print("correct")
        vec_sim_rul[14]="time expresion"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    con_coo_ans_sim_rul=input("what are the [conjunctions/coordinators]?: ")
    if(con_coo_ans_sim_rul=="fanboys(for/and/nor/but/or/yet/so)"):
        print("correct")
        vec_sim_rul[15]="conjunctions/coordinators"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    con_ans_sim_rul=input("what are the connectors?: ")
    if(con_ans_sim_rul=="preposition/conjunctions-coordinators(fanboys)"):
        print("correct")
        vec_sim_rul[16]="connectors"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    sep_str_ans_sim_rul=input("what are the separate structures? [________[?]_______]: ")
    if(sep_str_ans_sim_rul==",/preposition/conjunctions-coordinators(fanboys)"):
        print("correct")
        vec_sim_rul[17]="separate structures"
        good_sim_rul+=1
    else:
        print("incorrect")
    print()

    print()
    print("Answers:")
    recorrer_lista(vec_sim_rul)
    print(f"result: {good_sim_rul}/16")
    if(good_sim_rul==16):
        print("Congratulations, do you have 1 point")
        bin_sim_rul=True
    else:
        print("keep trying")
    
    return bin_sim_rul

def basic_sentence_structure():
    print()
    print("BASIC SENTENCE STRUCTURE")
    vec_bas_sen_str=["------","------","------","------","------","------","------","------","------","------","------"]
    good_bas_sen_str=0
    answer_bas_sen_str=input("what the basic sentence structure?: ")
    if(answer_bas_sen_str=="subject+verb+object"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[0]="what the basic sentence structure"
    else:
        print("incorrect")
    print()

    print("SIMPLE RULES")
    var_sim_rul=simple_rules()
    if(var_sim_rul):
        print("Correct do you have 1 point")
        good_bas_sen_str+=1
        vec_bas_sen_str[1]="simple rules"
    else:
        print("Do you not have point")
    
    print()
    answer_wh_sub=input("what is a subject?: ")
    if(answer_wh_sub=="a subject is a part of a sentence that contains the person or thing performing the action in a sentence"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[2]="what is a subject"
    else: 
        print("incorrect")

    print()
        
    point_noun_subject=noun_subject()
    if(point_noun_subject):
        good_bas_sen_str+=1
        vec_bas_sen_str[3]="subjects/nouns words"

    print()
    answer_wh_ar_pro=input("what are pronouns?: ")
    if(answer_wh_ar_pro=="pronouns are the words we often use to talk about a person when we are not using their name"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[4]="what are pronouns"
    else:
        print("incorrect")

    print()
    pronouns_var=pronouns()
    if(pronouns_var):        
        good_bas_sen_str+=1
        vec_bas_sen_str[5]="Pronouns"        

    print()
    answer_wh_adj=input("what is a adjective?: ")
    if(answer_wh_adj=="an adjective is a word that describes the traits,qualities or number of a noun"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[6]="what is a adjective"
    else:
        print("incorrect")
    print()
        
    point_adjective=adjective()
    if(point_adjective):
        good_bas_sen_str+=1
        vec_bas_sen_str[7]="adjective words"
    print()
    

    point_adjective_example=adjective_example()
    if(point_adjective_example):
        good_bas_sen_str+=1
        vec_bas_sen_str[8]="example adjective"
    print()

    answer_wh_adv=input("what is adverb?: ")
    if(answer_wh_adv=="an adverb is a word that modifies or describes a verb"):
        print("correct ")
        good_bas_sen_str+=1
        vec_bas_sen_str[9]="what is a adverb"
    else:
        print("incorrect")
    print()

    point_adverb=adverb()
    if(point_adverb):
        good_bas_sen_str+=1
        vec_bas_sen_str[10]="adverb"

    print()    
    print("Answers:")
    recorrer_lista(vec_bas_sen_str)
    print(f"result: {good_bas_sen_str}/28")
    print()
    print("¿you want to see the list of answers, but if you see them the test is over?yes/not")
    see_ans=input()
    exit="not"
    while(exit=="not"):
        if(see_ans=="yes"):
            list_correct_basic_sentence_strcture()
            exit="yes"
        elif(see_ans=="not"):
            print()            
            print("¿you want to leave the basic sentense structure test yes/not?")
            see_ans=input()
            if(see_ans=="yes"):
                exit="yes"
            elif(see_ans=="not"):
                exit="not"
   
