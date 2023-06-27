import words
import theory

#programa princpal
print("quieres ver las reglas ¿yes or not?")
rules=input()
if(rules=="yes"):
    print("#1: Todo en minuscula")
    print("#2: Si la respuesta lleva una [,] no hacer el espacio [texto,texto]")

print()
print("do you want the test of [theory] or [words]?")
tho_or_wor=input()
if(tho_or_wor=="words"):
    #you choose words
    print('')
    words.main()

elif(tho_or_wor=="theory"):
    #you choose theory        
    theory.main_theory()

print("Termino")

