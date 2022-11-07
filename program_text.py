import words
import theory

#programa princpal
print("quieres ver las reglas ¿yes or not?")
rules=input()
if(rules=="yes"):
    print("#1: Todo en minuscula")

print()
print("do you want the test of [theory] or [words]?")
tho_or_wor=input()
if(tho_or_wor=="words"):
    #you choose words
    print('')
    print("Test#1")
    var_test1=words.test1()
    if(var_test1==1):
        print("test#2")
        var_test_2=words.test2()
        if(var_test_2==1):
            print("test #3")
            var_test_3=words.test3()
            if(var_test_3==1):
                print("test #4")
elif(tho_or_wor=="theory"):
    #you choose theory        
    theory.main_theory()

print("Termino")

