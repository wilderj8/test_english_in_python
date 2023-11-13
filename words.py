#hay algo raro en firefighter
#funciones
def recorrer_lista_test(list_test):
    print("correct words")
    for x in list_test:
        print(x)

def correct_list_test_1():
    print()
    print('lista correcta del test 1')
    print('spanish--english--pronunciation')
    print('común--common--kamen')
    print('signifigar/medi@--mean--min')
    print('arrepentid@--regretted--regreded')
    print('quedate--stay--stey')
    print('lanzar--throw--trou')
    print('mediante--through--truu')
    print('más alla--beyond--bi-ant')
    print('cubrir--cover--coverd')
    print('tonelada--ton--ton')
    print('agoviado--overwhelmed--over-welt')

def correct_list_test_2():
    print()
    print('lista correcta del test 2')
    print('spanish--english--pronunciation')
    print('mejoras--improvements--in-pru-ments')
    print('debe/obligación/necesario--must--most')
    print('subsidios/becas--grants--grents')
    print('disponible--available--abei-lobo')
    print('algunos--some--som')
    print('cuidado--care--ker')
    print('mismo/igual--same--seim')
    print('proveer/prestar/disponer/suministrar--provide--pro-va-it')
    print('revelar/divulgar--disclose--dis-cous')
    print('liberado/publicado--released--ruilist')

def correct_list_test_3():
    print()
    print('lista correcta del test 3')
    print('spanish--english--pronunciation')
    print('Ejecutando--performing--per-for-ming')
    print('conciencia--awareness--o-wer-ness')
    print('entrenador/ra--trainer--trei-ner')
    print('rendimiento--performance--per-for-mens')
    print('debilidad--weakness--wik-ness')
    print('señora/dama--lady--ley-dii')
    print('poesía--poetry--pou-trii')
    print('coraje/valor/valentía--courage--co-ruich')
    print('bienes/inmuebles/finca--estate--steit')
    print('critica--criticism--cri-sici-um')

def correct_list_test_4():
    print()
    print('lista correcta del test 4')
    print("crown--corona--cra-un")
    print("interrupt--interrumpir--inter-rrapt")
    print("clearance--despeje/autorización--cle-rens")
    print("cower--acobardarce--cli-rens")
    print("firefighter--bombero--fair-or-faider")
    print("still--aún/todavía--ss-tel")
    print("mistake--error/equivocación--miss-tik")
    print("against--en contra de/contra--ege-nst")
    print("trait--caracteristica/cualidad/rasgo/atributo--trueit")
    print("chest--cofre/baúl/tetas/pecho/--chest")    

def correct_list_test_5():
    print()
    print('lista correcta del test 5')
    print("Acuerdo/convenio/tratado--agreement--a-gra-ment")
    print("llegada/aterrizaje--arrival--a-rai-bol")
    print("parecio--seemed--sit")
    print("aparentemente/supuestamente--seemingly--si-mi-li")
    print("embarazada/preñada--pregnant--pre-nent")
    print("algo de/alguna/algún/cualquier--any--eny")
    print("aún/incluso/hasta/todavía--even--i-ven")
    print("alguna vez/de todos los tiempos/nunca/sin duda--ever--ever")
    print("expedir/emitir/publicar/problema--issue--i-shu")
    print("alguna vez/antes/una vez/hace tiempo--once--wons")

def test1():
    list_test_1=["---------","---------","---------","---------","---------","---------","---------","---------","---------","---------"]
    good=0
    exit="not"
    while (good<10 and exit=="not"):
        print("write común in english")
        comun_word=input()
        print("write the pronunciation of común in english")
        comun_pronunciation=input()
        if(comun_word=="common" and comun_pronunciation=="kamen"):
            print("correct")
            good=good+1
            list_test_1[0]="Común"            
        else:
                print("incorrect")
        print('')
        
        print('write significar/medi@ in english')
        significar_word=input()
        print('write the pronunciation of significar/medi@ in english')
        significar_pronunciation=input()
        if(significar_word=='mean' and significar_pronunciation=='min'):
            print('correct')
            good=good+1
            list_test_1[1]="significar"
        else:
            print('incorrect')
        print('')

        print('write arrepentid@ in english')
        regretted_word=input()
        print('write the pronunciation of arrepentid@ in english')
        regretted_pronunciation=input()
        if(regretted_word=='regretted' and regretted_pronunciation=='regreded'):
            print('correct')
            good=good+1
            list_test_1[2]="arrepentid@"
        else:
            print('incorrect')
        print('')
        
        print('write quedate in english')
        stay_word=input()
        print('write the pronunciation of quedate in english')
        stay_pronunciation=input()
        if(stay_word=='stay' and stay_pronunciation=='stey'):
            print('correct')
            good=good+1
            list_test_1[3]="quedate"
        else:
            print('incorrect')
        print('')

        print('write tirar in english')
        throw_word=input()
        print('write the pronunciation of tirar in english')
        throw_pronunciation=input()
        if(throw_word=='throw' and throw_pronunciation=='trou'):
            print('correct')
            good=good+1
            list_test_1[4]="tirar"
        else:
            print('incorrect')
        print('')

        print('write mediante in english')
        through_word=input()
        print('write the pronunciation of mediante in english')
        through_pronunciation=input()
        if(through_word=='through' and through_pronunciation=='truu'):
            print('correct')
            good=good+1
            list_test_1[5]="mediante"
        else:
            print('incorrect')
        print('')

        print('write más alla in english')
        beyond_word=input()
        print('write the pronunciation of más alla in english')
        beyond_pronunciation=input()
        if(beyond_word=='beyond' and beyond_pronunciation=='bi-ant'):
            print('correct')
            good=good+1
            list_test_1[6]="más alla"
        else:
            print('incorrect')
        print('')

        print('write cubrir in english')
        cover_word=input()
        print('write the pronunciation of cubrir in english')
        cover_pronunciation=input()
        if(cover_word=='cover' and cover_pronunciation=='coverd'):
            print('correct')
            good=good+1
            list_test_1[7]="cubrir"
        else:
            print('incorrect')
        print('')

        print('write tonelada in english')
        ton_word=input()
        print('write the pronunciation of tonelada in english')
        ton_pronunciation=input()
        if(ton_word=='ton' and ton_pronunciation=='ton'):
            print('correct')
            good=good+1
            list_test_1[8]="tonelada"
        else:
            print('incorrect')
        print('')

        print('write agoviado in english')
        overwhelmed_word=input()
        print('write the pronunciation of agoviado in english')
        overwhelmed_pronunciation=input()
        if(overwhelmed_word=='overwhelmed' and overwhelmed_pronunciation=='over-welt'):
            print('correct')
            good=good+1
            list_test_1[9]="agoviado"
        else:
            print('incorrect')
        print('')

        recorrer_lista_test(list_test_1)
        print(f"{good}/10")
                
        print('')   
        print("¿you want to leave the test#1 yes/not?")
        exit=input()
        
        if(exit=='not'):
            list_test_1=["---------","---------","---------","---------","---------","---------","---------","---------","---------","---------"]
            good=0            

        print("¿you want to see the list of answers, but if you see them the test is over?yes/not")
        see_answers_test_1=input()
        if(see_answers_test_1=="yes"):
            correct_list_test_1()
            exit="yes"
        
        print("")
    return 1

def test2():
    list_test_2=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
    good=0
    exit='not'
    while (good<10 and exit=='not'):        
        print('write mejoras in english')
        improvements_word=input()
        print('write the pronunciation of mejoras in english')
        improvements_pronunciation=input()
        if(improvements_word=='improvements' and improvements_pronunciation=='in-pru-ments'):
            print('correct')
            good=good+1
            list_test_2[0]='improvements'
        else:
            print('incorrect')
        print('')

        print('write debe/obligación/necesario in english')
        must_word=input()
        print('write the pronunciation of debe/obligación/necesario in english')
        must_pronunciation=input()
        if(must_word=='must' and must_pronunciation=='most'):
            print('correct')
            good=good+1
            list_test_2[1]='must'
        else:
            print('incorrect')
        print('')
        
        print('write subsidios/becas in english')
        grants_word=input()
        print('write the pronunciation of subsidios/becas in english')
        grants_pronunciation=input()
        if(grants_word=='grants' and grants_pronunciation=='grents'):
            print('correct')
            good=good+1
            list_test_2[2]='grants'
        else:
            print('incorrect')
        print('')

        print('write disponible in english')
        available_word=input()
        print('write the pronunciation of disponible in english')
        available_pronunciation=input()
        if(available_word=='available' and available_pronunciation=='abei-lobo'):
            print('correct')
            good=good+1
            list_test_2[3]='available'
        else:
            print('incorrect')
        print('')

        print('write algunos in english')
        some_word=input()
        print('write the pronunciation of algunos in english')
        some_pronunciation=input()
        if(some_word=='some' and some_pronunciation=='som'):
            print('correct')
            good=good+1
            list_test_2[4]='some'
        else:
            print('incorrect')
        print('')

        print('write cuidado in english')
        care_word=input()
        print('write the pronunciation of cuidado in english')
        care_pronunciation=input()
        if(care_word=='care' and care_pronunciation=='ker'):
            print('correct')
            good=good+1
            list_test_2[5]='care'
        else:
            print('incorrect')
        print('')

        print('write mismo/igual in english')
        same_word=input()
        print('write the pronunciation of mismo/igual in english')
        same_pronunciation=input()
        if(same_word=='same' and same_pronunciation=='seim'):
            print('correct')
            good=good+1
            list_test_2[6]='same'
        else:
            print('incorrect')
        print('')

        print('write proveer/prestar/disponer/suministrar in english')
        provide_word=input()
        print('write the pronunciation of proveer/prestar/disponer/suministrar in english')
        provide_pronunciation=input()
        if(provide_word=='provide' and provide_pronunciation=='pro-va-it'):
            print('correct')
            good=good+1
            list_test_2[7]='provide'
        else:
            print('incorrect')
        print('')

        print('write revelar/divulgar in english')
        disclose_word=input()
        print('write the pronunciation of revelar/divulgar in english')
        disclose_pronunciation=input()
        if(disclose_word=='disclose' and disclose_pronunciation=='dis-cous'):
            print('correct')
            good=good+1
            list_test_2[8]='disclose'
        else:
            print('incorrect')
        print('')

        print('write liberado/publicado in english')
        released_word=input()
        print('write the pronunciation of liberado/publicado in english')
        released_pronunciation=input()
        if(released_word=='released' and released_pronunciation=='ruilist'):
            print('correct')
            good=good+1
            list_test_2[9]='released'
        else:
            print('incorrect')
        print('')

        recorrer_lista_test(list_test_2)
        print(f'{good}/10')
        print('')
        print('¿you want to leave the test#2 yes/not?')
        exit=input()
        if(exit=='not'):
            list_test_2=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
            good=0
        print('¿you want to see the list of answers, but if you see them the test is over?yes/not')
        see_answers_test_2=input()
        if(see_answers_test_2=='yes'):
            correct_list_test_2()
            exit='yes'
    print('')
    return 1

def test3():    
    list_test_3=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
    good=0
    exit='not'
    while (good<10 and exit=='not'):
        print('write ejecutando in english')
        performing_word=input()
        print('write the pronunciation of ejecutando in english')
        performing_pronunciation=input()
        if(performing_word=='performing' and performing_pronunciation=='per-for-ming'):
            print('correct')
            good=good+1
            list_test_3[0]='performing'
        else:
            print('incorrect')
        print('')
        
        print('write conciencia  in english')
        awareness_word=input()
        print('write the pronunciation of conciencia  in english')
        awareness_pronunciation=input()
        if(awareness_word=='awareness' and awareness_pronunciation=='o-wer-ness'):
            print('correct')
            good=good+1
            list_test_3[1]='awareness'
        else:
            print('incorrect')
        print('')

        print('write entrenador/ra in english')
        trainer_word=input()
        print('write the pronunciation of entrenador/ra in english')
        trainer_pronunciation=input()
        if(trainer_word=='trainer' and trainer_pronunciation=='trei-ner'):
            print('correct')
            good=good+1
            list_test_3[2]='trainer'
        else:
            print('incorrect')
        print('')

        print('write rendimiento/desempeño in english')
        performance_word=input()
        print('write the pronunciation of rendimiento/desempeño in english')
        performance_pronunciation=input()
        if(performance_word=='performance' and performance_pronunciation=='per-for-mens'):
            print('correct')
            good=good+1
            list_test_3[3]='performance'
        else:
            print('incorrect')
        print('')

        print('write debilidad in english')
        weakness_word=input()
        print('write the pronunciation of debilidad in english')
        weakness_pronunciation=input()
        if(weakness_word=='weakness' and weakness_pronunciation=='wik-ness'):
            print('correct')
            good=good+1
            list_test_3[4]='weakness'
        else:
            print('incorrect')
        print('')

        print('write señora/dama in english')
        lady_word=input()
        print('write the pronunciation of señora/dama in english')
        lady_pronunciation=input()
        if(lady_word=='lady' and lady_pronunciation=='ley-dii'):
            print('correct')
            good=good+1
            list_test_3[5]='lady'
        else:
            print('incorrect')
        print('')

        print('write poesía in english')
        poetry_word=input()
        print('write the pronunciation of poesía in english')
        poetry_pronunciation=input()
        if(poetry_word=='poetry' and poetry_pronunciation=='pou-trii'):
            print('correct')
            good=good+1
            list_test_3[6]='poetry'
        else:
            print('incorrect')
        print('')

        print('write coraje/valor/valentía in english')
        courage_word=input()
        print('write the pronunciation of coraje/valor/valentía in english')
        courage_pronunciation=input()
        if(courage_word=='courage' and courage_pronunciation=='co-ruich'):
            print('correct')
            good=good+1
            list_test_3[7]='courage'
        else:
            print('incorrect')
        print('')

        print('write bienes/inmuebles/finca in english')
        estate_word=input()
        print('write the pronunciation of bienes/inmuebles/finca in english')
        estate_pronunciation=input()
        if(estate_word=='estate' and estate_pronunciation=='steit'):
            print('correct')
            good=good+1
            list_test_3[8]='estate'
        else:
            print('incorrect')
        print('')

        print('write critica in english')
        criticism_word=input()
        print('write the pronunciation of critica in english')
        criticism_pronunciation=input()
        if(criticism_word=='criticism' and criticism_pronunciation=='cri-sici-um'):
            print('correct')
            good=good+1
            list_test_3[9]='criticism'
        else:
            print('incorrect')
        print('')

        recorrer_lista_test(list_test_3)
        print(f'{good}/10')
        print('')
        print('¿you want to leave the test#3 yes/not?')
        exit=input()
        if(exit=='not'):
            list_test_3=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
            good=0
        print('¿you want to see the list of answers, but if you see them the test is over?yes/not')
        see_answers_test_3=input()
        if(see_answers_test_3=='yes'):
            correct_list_test_3()
            exit='yes'
            
        print("")
    return 1

def test4():
    list_test_4=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
    good=0
    exit='not'
    while (good<10 and exit=='not'):
        print('write corona in english')
        crown_word=input()
        print('write the pronunciation of corona in english')
        crown_pronunciation=input()
        if(crown_word=='crown' and crown_pronunciation=='cra-un'):
            print('correct')
            good=good+1
            list_test_4[0]='crown'
        else:
            print('incorrect')
        print('')

        print('write interrumpir in english')
        interrupt_word=input()
        print('write the pronunciation of interrumpir in english')
        interrupt_pronunciation=input()
        if(interrupt_word=='interrupt' and interrupt_pronunciation=='inter-rrapt'):
            print('correct')
            good=good+1
            list_test_4[1]='interrupt'
        else:
            print('incorrect')
        print('')

        print('write autorización/despeje in english')
        clearance_word=input()
        print('write the pronunciation of autorización/despeje in english')
        clearance_pronunciation=input()
        if(clearance_word=='clearance' and clearance_pronunciation=='cle-rens'):
            print('correct')
            good=good+1
            list_test_4[2]='clearance'
        else:
            print('incorrect')
        print('')

        print('write acobardarce in english')
        cower_word=input()
        print('write the pronunciation of acobardarce in english')
        cower_pronunciation=input()
        if(cower_word=='cower' and cower_pronunciation=='cli-rens'):
            print('correct')
            good=good+1
            list_test_4[3]='cower'
        else:
            print('incorrect')
        print('')

        print('write bombero in english')
        firefighter_word=input()
        print('write the pronunciation of bombero in english')
        firefighter_pronunciation=input()
        if(firefighter_word=='firefighter' and firefighter_pronunciation=='fair-or-faider'):
            print('correct')
            good=good+1
            list_test_4[4]='firefighter'
        else:
            print('incorrect')
        print('')

        print('write aún/todavía in english')
        still_word=input()
        print('write the pronunciation of aún/todavía in english')
        still_pronunciation=input()
        if(still_word=='still' and still_pronunciation=='ss-tel'):
            print('correct')
            good=good+1
            list_test_4[5]='still'
        else:
            print('incorrect')
        print('')   

        print('write error/equivocarce in english')
        mistake_word=input()
        print('write the pronunciation of error/equivocarce in english')
        mistake_pronunciation=input()
        if(mistake_word=='mistake' and mistake_pronunciation=='miss-tik'):
            print('correct')
            good=good+1
            list_test_4[6]='mistake'
        else:
            print('incorrect')
        print('') 

        print('write en contra de/contra in english')
        against_word=input()
        print('write the pronunciation of en contra de/contra in english')
        against_pronunciation=input()
        if(against_word=='against' and against_pronunciation=='ege-nst'):
            print('correct')
            good=good+1
            list_test_4[7]='against'
        else:
            print('incorrect')
        print('')   

        print('write rasgo/atributo/caracteristica/cualidad in english')
        trait_word=input()
        print('write the pronunciation of rasgo/atributo/caracteristica/cualidad in english')
        trait_pronunciation=input()
        if(trait_word=='trait' and trait_pronunciation=='trueit'):
            print('correct')
            good=good+1
            list_test_4[8]='trait'
        else:
            print('incorrect')
        print('')

        print('write pecho/tetas/baúl/cofre in english')
        chest_word=input()
        print('write the pronunciation of pecho/tetas/baúl/cofre in english')
        chest_pronunciation=input()
        if(chest_word=='chest' and chest_pronunciation=='chest'):
            print('correct')
            good=good+1
            list_test_4[9]='chest'
        else:
            print('incorrect')
        print('')

        recorrer_lista_test(list_test_4)
        print(f'{good}/10')
        print('')
        print('¿you want to leave the test#4 yes/not?')
        exit=input()
        if(exit=='not'):
            list_test_4=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
            good=0
        print('¿you want to see the list of answers, but if you see them the test is over?yes/not')
        see_answers_test_4=input()
        if(see_answers_test_4=='yes'):
            correct_list_test_4()
            exit='yes'
        print('')
    return 1

def test5():
    list_test_5=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
    good=0
    exit='not'
    while (good<10 and exit=='not'):
        print('write Acuerdo/convenio/tratado in english')
        agreement_word=input()
        print('write the pronunciation of Acuerdo/convenio/tratado in english')
        agreement_pronunciation=input()
        if(agreement_word=='agreement' and agreement_pronunciation=='a-gra-ment'):
            print('correct')
            good=good+1
            list_test_5[0]='agreement'
        else:
            print('incorrect')
        print('')

        print('write llegada/aterrizaje in english')
        arrival_word=input()
        print('write the pronunciation of llegada/aterrizaje in english')
        arrival_pronunciation=input()
        if(arrival_word=='arrival' and arrival_pronunciation=='a-rai-bol'):
            print('correct')
            good=good+1
            list_test_5[1]='arrival'
        else:
            print('incorrect')
        print('')

        print('write parecio in english')
        seemed_word=input()
        print('write the pronunciation of parecio in english')
        seemed_pronunciation=input()
        if(seemed_word=='seemed' and seemed_pronunciation=='sit'):
            print('correct')
            good=good+1
            list_test_5[2]='seemed'
        else:
            print('incorrect')
        print('')

        print('write aparentemente/supuestamente in english')
        seemingly_word=input()
        print('write the pronunciation of aparentemente/supuestamente in english')
        seemingly_pronunciation=input()
        if(seemingly_word=='seemingly' and seemingly_pronunciation=='si-mi-li'):
            print('correct')
            good=good+1
            list_test_5[3]='seemingly'
        else:
            print('incorrect')
        print('')

        print('write embarazada/preñada in english')
        pregnant_word=input()
        print('write the pronunciation of embarazada/preñada in english')
        pregnant_pronunciation=input()
        if(pregnant_word=='pregnant' and pregnant_pronunciation=='pre-nent'):
            print('correct')
            good=good+1
            list_test_5[4]='pregnant'
        else:
            print('incorrect')
        print('')
        
        print('write algo de/alguna/algún/cualquier in english')
        any_word=input()
        print('write the pronunciation of algo de/alguna/algún/cualquier in english')
        any_pronunciation=input()
        if(any_word=='any' and any_pronunciation=='eny'):
            print('correct')
            good=good+1
            list_test_5[5]='any'
        else:
            print('incorrect')
        print('')

        print('write aún/incluso/hasta/todavía in english')
        even_word=input()
        print('write the pronunciation of aún/incluso/hasta/todavía in english')
        even_pronunciation=input()
        if(even_word=='even' and even_pronunciation=='i-ven'):
            print('correct')
            good=good+1
            list_test_5[6]='even'
        else:
            print('incorrect')
        print('')

        print('write alguna vez/de todos los tiempos/nunca/sin duda in english')
        ever_word=input()
        print('write the pronunciation of alguna vez/de todos los tiempos/nunca/sin duda in english')
        ever_pronunciation=input()
        if(ever_word=='ever' and ever_pronunciation=='ever'):
            print('correct')
            good=good+1
            list_test_5[7]='ever'
        else:
            print('incorrect')
        print('')
        
        print('write expedir/emitir/publicar/problema in english')
        issue_word=input()
        print('write the pronunciation of expedir/emitir/publicar/problema in english')
        issue_pronunciation=input()
        if(issue_word=='issue' and issue_pronunciation=='i-shu'):
            print('correct')
            good=good+1
            list_test_5[8]='issue'
        else:
            print('incorrect')
        print('')

        print('write alguna vez/antes/una vez/hace tiempo in english')
        once_word=input()
        print('write the pronunciation of alguna vez/antes/una vez/hace tiempo in english')
        once_pronunciation=input()
        if(once_word=='once' and once_pronunciation=='wons'):
            print('correct')
            good=good+1
            list_test_5[9]='once'
        else:
            print('incorrect')
        print('')

        recorrer_lista_test(list_test_5)
        print(f'{good}/10')
        print('')
        print('¿you want to leave the test#5 yes/not?')
        exit=input()
        if(exit=='not'):
            list_test_5=['---------','---------','---------','---------','---------','---------','---------','---------','---------','---------']
            good=0
        print('¿you want to see the list of answers, but if you see them the test is over?yes/not')
        see_answers_test_5=input()
        if(see_answers_test_5=='yes'):
            correct_list_test_5()
            exit='yes'
        print('')
    return 1

#main
def main():
    print("----------------------------------")
    print("Menu:")
    print("1: start in the Test #1")
    print("2: start in the Test #2")
    print("3: start in the Test #3")
    print("4: start in the Test #4")
    print("5: start in the Test #5")
    print("----------------------------------")
    option_select=int(input("select: "))
    if(option_select==1):
        print("Test#1")
        test_1=test1()
        print("Test#2")
        test_2=test2()
        print("Test#3")
        test_3=test3()
        print("Test#4")
        test_4=test4()
        print("Test#5")
        test_5=test5()
    elif(option_select==2):
        print("Test#2")
        test_2=test2()
        print("Test#3")
        test_3=test3()
        print("Test#4")
        test_4=test4()
        print("Test#5")
        test_5=test5()
    elif(option_select==3):
        print("Test#3")
        test_3=test3()
        print("Test#4")
        test_4=test4()
        print("Test#5")
        test_5=test5()
    elif(option_select==4):
        print("Test#4")
        test_4=test4()
        print("Test#5")
        test_5=test5()
    elif(option_select==5):
        print("Test#5")
        test_5=test5()
