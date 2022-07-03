#funciones
def recorrer_lista_test(list_test):
    print("correct words")
    for x in list_test:
        print(x)

def correct_list_test_1():
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

#programa princpal
print("quieres ver las reglas ¿yes or not?")
rules=input()
if(rules=="yes"):
    print("#1: Todo en minuscula")

print('')
print("Test#1")
var_test1=test1()
if(var_test1==1):
    print("test#2")

print("Termino")

