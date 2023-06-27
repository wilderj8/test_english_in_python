#main
good_bas_sen_str=0
vec_bas_sen_str=["----","----","----","----","----","----","----","----","----","----","----","----",]

#borrador
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

    exa_4_sim=input("Yo como in affirmative and present simple: ")
    exa_5_sim=input("Él come in affirmative and present simple: ")
    exa_6_sim=input("Tú comes in affirmative and present simple: ")
    if(exa_4_sim=="i eat" and exa_5_sim=="he eats" and exa_6_sim=="you eat"):
        print("correct")
        good_sim_tes+=1
    else:
        print("incorrect")
    print()

    exa_7_sim=input("tú no comes in negative and present simple: ")
    exa_8_sim=input("no comistes in negative and past simple: ")
    if(exa_7_sim=="you don't eat" and exa_8_sim=="you didn't eat"):
        print("correct")
        good_sim_tes+=1
    else:
        print("incorrect")
    print()

    exa_9_sim=input("¿tú comes?/¿comes? in interrogative and present simple: ")
    exa_10_sim=input("¿comiste? in interrogative and past simple: ")
    if(exa_9_sim=="do you eat?" and exa_10_sim=="did you eat?"):
        print("correct")
        good_sim_tes+=1
    else:
        print("incorrect")
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

    exa_4_con=input("yo estoy comiendo in affirmative and present continuos: ")
    exa_5_con=input("tú estás comiendo in affirmative and present continuos: ")
    if((exa_4_con=="i am eating" or exa_4_con=="i'm eating") and (exa_5_con=="you are eating" or exa_5_con=="you're eating") ):
        print("correct")
        good_con_tes+=1
    else:
        print("incorrect")
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

    exa_4_per=input("yo he comido in affirmative and present perfect: ")
    exa_5_per=input("nosotros hemos comido in affirmative and present perfect: ")
    exa_6_per=input("ella ha comido in affirmative and present perfect: ")
    if(exa_4_per=="i have eaten" and exa_5_per=="we have eaten" and exa_6_per=="she has eaten"):
        print("correct")
        good_per_tes+=1
    else:
        print("incorrect")
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
    if(aux_con_str=="to be+gerundio"):
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
    if(aux_con_per_str=="to be+to have"):
        print("correct")
        good_aux_verb+=1
    else:
        print("incorrect")
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

#llamar en main
print("auxiliary verbs")
point_verb=aux_verb()
if(point_verb):
    good_bas_sen_str+=1
    vec_bas_sen_str[11]="auxiliary verb"
else:
    print("incorrect")
print()