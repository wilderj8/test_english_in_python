#de theory
def recorrer_lista(list_test):    
    for x in list_test:
        print(x)

good_bas_sen_str=0
vec_bas_sen_str=["----"]
#borrador

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

    if(exa_6_art_def==6):
        print("correct")
        example=True
    
    return example
    
def articles():
    articles_var=False
    var_art=0
    vec_art=["----","----","----","----","----","----","----"]
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

    rul_3_ind_art=input("rule #3: where is the indefinite article located?: ")
    if(rul_3_ind_art=="the article is put before singular nouns"):
        print("correct")
        var_art+=1
        vec_art[2]="rule #3 indefinite articles"
    else:
        print("incorrect")
    print()

    art_ind=input("what are the indefinite articles?: ")
    if(art_ind=="a/an"):
        print("correct")
        var_art+=1
        vec_art[3]="indefinite articles"
    else:
        print("incorrect")
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

    return articles_var


#para llamarlo desde basic sentence structure
print()
articles_var_var=articles()
if(articles_var_var):        
    good_bas_sen_str+=1
    vec_bas_sen_str[0]="articles" 