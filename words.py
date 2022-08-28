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

