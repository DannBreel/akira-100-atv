print("\033[41m\033[1m\033[97m=====================================\033[0m")
print("\033[41m\033[1m\033[97mBLOCO 10 — FUNÇÕES E PROCEDIMENTOS\033[0m")
print("\033[41m\033[1m\033[97m=====================================\033[0m")
print("\033[41m \033[0m")

print("\033[41m\033[97m87. Crie uma função que receba dois números e retorne o maior deles.\033[0m")
print("\033[41m \033[0m")

def greato(x,y):
    if x>y:
        maior=x
    else:
        maior=y
    return maior

print(f"o maior numero é {greato(122,23)}")

print("\033[41m\033[97m88. Crie uma função que receba um número inteiro e retorne True se ele for par e False caso contrário.\033[0m")
print("\033[41m \033[0m")

def par(x):
    return x%2==0

print(f"o numero 5 é par?  {par(5)}")

print("\033[41m\033[97m89. Crie uma função que receba uma lista de números e retorne a média dos elementos.\033[0m")
print("\033[41m \033[0m")

def medlist(list):
    sim=0
    con=0
    for i in list:
        sim+=i
        con+=1
    return sim/con

aaa=[90,23,45,22]

print(medlist(aaa))

print("\033[41m\033[97m90. Crie um procedimento que receba um nome e exiba uma saudação personalizada.\033[0m")
print("\033[41m \033[0m")

def sadam():
    print("what's your name?")
    name=input()
    print(f"hello {name} nice to meet u")
    print("how are you?")
    print("i'm fine thank you")
    # i wish i were a bird 

print("\033[41m\033[97m91. Crie uma função que receba um número inteiro e retorne seu fatorial.\033[0m")
print("\033[41m \033[0m")

def fat(x):
    if x==1:
        return 1
    else:
        return x*fat(x-1)

print(fat(5))

print("\033[41m\033[97m92. Crie uma função que receba uma matriz e retorne a soma da diagonal principal.\033[0m")
print("\033[41m \033[0m")

def matrix(vets,elms):
    mtx=[]
    for i in range(vets):
        vet=[]
        for i in range(elms):
            vet.append(int(input("number matriz")))
        mtx.append(vet)
    return mtx

def ler(matrx):
    for i in matrx:
        print(i)

def somd(mtx):
    sd=0
    dg=0
    for i in mtx:
        sd+=i[dg]
        dg+=1
    return sd

bladewolf=matrix(3,3)
ler(bladewolf)
print(f"a soma da diagonal é {somd(bladewolf)}")

print("\033[41m\033[97m93. Crie uma função que receba uma string e retorne a quantidade de vogais existentes nela.\033[0m")
print("\033[41m \033[0m")

def vogg(str=str):
    vog=0
    for i in str:
        print(i)
        if i in "aeiou":
            vog+=1
    return vog

print(vogg(str(input())))


print("\033[41m\033[97m94. Crie um procedimento que receba uma lista e exiba seus elementos um por linha, junto do índice correspondente.\033[0m")
print("\033[41m \033[0m")

def lili(lis):
    for i in range(len(lis)):
        print(f"{lis[i]}, indice = {i+1}")

print("\033[41m\033[1m\033[97m=====================================\033[0m")
