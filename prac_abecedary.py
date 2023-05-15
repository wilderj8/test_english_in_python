#Functions
def validation(letter_test,letter_val):
    result=False
    if(letter_test=='a'):
        if(letter_val=='ei'):
            result=True
    elif(letter_test=='b'):
        if(letter_val=='bi'):
            result=True
    elif(letter_test=='c'):
        if(letter_val=='ci'):
            result=True
    elif(letter_test=='d'):
        if(letter_val=='di'):
            result=True
    elif(letter_test=='e'):
        if(letter_val=='i'):
            result=True
    elif(letter_test=='f'):
        if(letter_val=='ef'):
            result=True
    elif(letter_test=='g'):
        if(letter_val=='yi'):
            result=True
    elif(letter_test=='h'):
        if(letter_val=='eich'):
            result=True
    elif(letter_test=='i'):
        if(letter_val=='ai'):
            result=True
    elif(letter_test=='j'):
        if(letter_val=='jei'):
            result=True
    elif(letter_test=='k'):
        if(letter_val=='kei'):
            result=True
    elif(letter_test=='l'):
        if(letter_val=='el'):
            result=True
    elif(letter_test=='m'):
        if(letter_val=='em'):
            result=True
    elif(letter_test=='n'):
        if(letter_val=='en'):
            result=True
    elif(letter_test=='o'):
        if(letter_val=='ou'):
            result=True
    elif(letter_test=='p'):
        if(letter_val=='pi'):
            result=True
    elif(letter_test=='q'):
        if(letter_val=='kiu'):
            result=True
    elif(letter_test=='r'):
        if(letter_val=='ar'):
            result=True
    elif(letter_test=='s'):
        if(letter_val=='es'):
            result=True
    elif(letter_test=='t'):
        if(letter_val=='ti'):
            result=True
    elif(letter_test=='u'):
        if(letter_val=='iu'):
            result=True
    elif(letter_test=='v'):
        if(letter_val=='vi'):
            result=True
    elif(letter_test=='w'):
        if(letter_val=='dabliu'):
            result=True
    elif(letter_test=='x'):
        if(letter_val=='ex'):
            result=True
    elif(letter_test=='y'):
        if(letter_val=='uai'):
            result=True
    elif(letter_test=='z'):
        if(letter_val=='set'):
            result=True
        
    
    return result

#Main program            
word=input("Write a word: ")
letters=[]
# # a=0 de prueba
for letter in word:
    letters.append(letter)
    # # a+=1

# # a=a-1 de prueba

for letter_test in letters:
    print("Write the letter in english: " + letter_test)
    letter_val=input()
    result=validation(letter_test,letter_val)
    print(result)
    print()





# print("esta es la palabra: "+word)
# print(letters)
# print(letters[0])
# print(letters[a])
# print(letters)