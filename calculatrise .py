#calculatrise 

def somme(list):
    a=int(input("entre premier nomber"))
    b=int(input("enter duxiem nomber"))
    list=a+b 
    print(f"la somme de {a}+{b}={list}")
def soustraction( list) :
    a=int(input("entre premier nomber"))
    b=int(input("enter duxiem nomber"))
    list=a-b 
    print(f"la somme de {a}-{b}={list}")
def multiplication (list):
    a=int(input("entre premier nomber"))
    b=int(input("enter duxiem nomber"))
    list=a*b 
    print(f"la somme de {a}*{b}={list}")
def division( list):
    a=int(input("entre premier nomber"))
    b=int(input("enter duxiem nomber"))
    list=a/b 
    print(f"la somme de {a}/{b}={list}")
def prog():
    print ("1-somme")
    print("2-soustraction")  
    print("3-multiplication")  
    print("4-division")
    print("0-quiter")
    choix=input("Quelle est l opération mathématique que vous souhaitez ?")
    if choix =="1":
        somme(list)
    if choix =="2":
        soustraction(list)
    if choix =="3":
        multiplication(list)
    if choix =="4":
        division(list)
    if choix=="0":
        exit()
    prog()
prog()    

        





