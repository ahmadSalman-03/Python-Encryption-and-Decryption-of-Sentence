import random
def Encode():
    def radStr(length):
        abc="Abcjdskfuhfihfnsh83jdjd9ayyr2mvvqwertyuiopasdfghjk-34=505=345094-58258lz';./;xcvbnm';lkJSFHJK"
        return "".join(random.sample(abc,length))

    sentence=input("Enter the sentence you would like to Encode. ")
    list_=sentence.split()
    i=0
    while i<len(list_):
        char_list=list(list_[i])
        j=0
        while j<len(char_list)-1:
            char_list[j],char_list[j+1]=char_list[j+1],char_list[j]
            j=j+1
        new_string="".join(char_list)
        if(len(new_string)==2):
             print(new_string," ",end='')
        else:    
            print(radStr(3)+new_string+radStr(3)," ",end='')
        i=i+1

def Decode():
    sentence=input("Enter the sentence you would like to Decode: ")
    list_=sentence.split()
    i=0
    while i<len(list_):
        if(len(list_[i])>=3):
            reassemble=list_[i][3:-3]
            char_list=list(reassemble)
            j=-1
            while j>-(len(char_list)):
                char_list[j],char_list[j-1]=char_list[j-1],char_list[j]
                new_string="".join(char_list)
                j=j-1
            print(new_string," ",end='')
        elif(len(list_[i])==2):
            char_list=list(list_[i])
            char_list[0],char_list[1]=char_list[1],char_list[0]
            new_string="".join(char_list)
            print(new_string," ",end='')
        else:
           print(list_[i]," ",end='')
        i=i+1


choice=input("Enter E if you want to Encode or D if you want to Decode! ")
if(choice=='e' or choice=='E'):
    Encode()
elif(choice=='d' or choice=='D'):
    Decode()
