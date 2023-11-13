import words
import theory
import prac_abecedary
import month_game

#programa princpal
print("quieres ver las reglas ¿yes or not?")
rules=input()
if(rules=="yes"):
    print("#1: Todo en minuscula")
    print("#2: Si la respuesta lleva una [,] no hacer el espacio [texto,texto]")

print()
print("-----------------------------")
print("MENU SECTIONS: ")
print("1: Theory")
print("2: Words")
print("3: Month_game")
print("4: prac_abecedary")
print("-----------------------------")
select_menu=int(input("select: "))
if(select_menu==1):
    theory.main_theory()
    print('')
elif(select_menu==2):
    words.main()
    print('')
elif(select_menu==3):
    month_game.main()
    print('')
elif(select_menu==4):
    prac_abecedary.main()


print("Termino")

