from asyncore import write
from ctypes import pointer


def main_theory():
    abecedary()
    basic_sentence_structure()

def recorrer_lista(list_test):
    print("correct words/structure")
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
    print()

def list_correct_basic_sentence_strcture():
    print()
    print("question---answer")
    print("what the basic sentence structure?---subject+verb+object")
    print("what is a subject?---a subject is a part of a sentence that contains the person or thing performing the action in a sentence")
    correct_list_test_noun_subject()
    print("what are pronouns?--pronouns are the words we often use to talk about a person when we are not using their name")




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
        print("¿you want to see the list of answers, but if you see them the test is over?yes/not")
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

def noun_subject():
    point=False
    list_test_noun_subject=["----","----","----","----","----","----","----","----","----","----","----","----","----","----","----",]
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
    
    if(good==15):
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

    you_sing_var=input("write tu: ")
    if(you_sing_var=="you"):
        print("correct")
        good_pro+=1

    he_var=input("write él: ")
    if(he_var=="he"):
        print("correct")
        good_pro+=1

    she_var=input("write ella: ")
    if(she_var=="she"):
        print("correct")
        good_pro+=1

    it_var=input("write eso: ")
    if(it_var=="it"):
        print("correct")
        good_pro+=1

    we_var=input("write nosotros/as: ")
    if(we_var=="we"):
        print("correct")
        good_pro+=1

    you_plu_var=input("write ustedes: ")
    if(you_plu_var=="you"):
        print("correct")
        good_pro+=1

    they_var=input("write ellas/ellos: ")
    if(they_var=="they"):
        print("correct")
        good_pro+=1
    
    print("write object pronouns")
    me_var_obj_pro=input("write conmigo/a mi: ")
    if(me_var_obj_pro=="me"):
        print("correct")
        good_pro+=1

    you_sin_var_obj_pro=input("write conmigo/a ti: ")
    if(you_sin_var_obj_pro=="you"):
        print("correct")
        good_pro+=1

    him_var_obj_pro=input("write el/a el: ")
    if(him_var_obj_pro=="him"):
        print("correct")
        good_pro+=1

    her_var_obj_pro=input("write a ella: ")
    if(her_var_obj_pro=="her"):
        print("correct")
        good_pro+=1

    it_var_obj_pro=input("write a eso/esa: ")
    if(it_var_obj_pro=="it"):
        print("correct")
        good_pro+=1

    us_var_obj_pro=input("write a nosotros/no: ")
    if(us_var_obj_pro=="us"):
        print("correct")
        good_pro+=1

    you_plu_var_obj_pro=input("write a ustedes: ")
    if(you_plu_var_obj_pro=="you"):
        print("correct")
        good_pro+=1

    them_var_obj_pro=input("write ellos/ellas: ")
    if(them_var_obj_pro=="them"):
        print("correct")
        good_pro+=1
    
    print()
    print("examples object pronouns:")
    exa_1_obj_pro=input("how would the sentence with object pronoun? [susan calls sexilio]")
    if(exa_1_obj_pro=="she calls him"):
        print("correct")
        good_pro+=1

    exa_2_obj_pro=input("how would the sentence with object pronoun? [paul works with kelly]")
    if(exa_2_obj_pro=="he works with her"):
        print("correct")
        good_pro+=1
    
    exa_3_obj_pro=input("how would the sentence with object pronoun? [peter and victor play with their friend]")
    if(exa_3_obj_pro=="they play with them"):
        print("correct")
        good_pro+=1
    
    exa_4_obj_pro=input("how would the sentence with object pronoun? [mr.gonzales feeds the dog]")
    if(exa_4_obj_pro=="she feed it"):
        print("correct")
        good_pro+=1
    
    exa_5_obj_pro=input("how would the sentence with object pronouns? [mr.smith feeds the cats]")
    if(exa_5_obj_pro=="he feeds them"):
        print("correct")
        good_pro+=1

    exa_6_obj_pro=input("how would the sentence with object pronouns? [mary and charlie talk to my sister and me]")
    if(exa_6_obj_pro=="they talk to us"):
        print("correct")
        good_pro+=1

    
    if(good_pro==22):
        print("Congratulations, you have a point")
        point=True
    else:
        print("you not have point")
        
    return point


def basic_sentence_structure():
    print()
    print("BASIC SENTENCE STRUCTURE")
    vec_bas_sen_str=["------","------","------","------"]
    good_bas_sen_str=0
    answer_bas_sen_str=input("what the basic sentence structure?: ")
    if(answer_bas_sen_str=="subject+verb+object"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[0]="what the basic sentence structure"
    else:
        print("incorrect")

    print()
    answer_wh_sub=input("what is a subject?: ")
    if(answer_wh_sub=="a subject is a part of a sentence that contains the person or thing performing the action in a sentence"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[1]="what is a subject"
    else: 
        print("incorrect")

    print()
        
    point_noun_subject=noun_subject()
    if(point_noun_subject):
        good_bas_sen_str+=1
        vec_bas_sen_str[2]="subjects/nouns words"

    print()
    answer_wh_ar_pro=input("what are pronouns?: ")
    if(answer_wh_ar_pro=="pronouns are the words we often use to talk about a person when we are not using their name"):
        print("correct")
        good_bas_sen_str+=1
        vec_bas_sen_str[3]="what are pronouns"

    print()    
    print("Answers:")
    recorrer_lista(vec_bas_sen_str)
    print(f"result: {good_bas_sen_str}/27")
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
   
