# Cores ANSI
VERDE = '\033[92m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# funcao que cria matrix (linhas, colunas) ou como esta escrito (vetores e elementos)
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

print(f"{AMARELO}79. Crie uma matriz 3x3 lendo valores do usuário e depois exiba a matriz linha por linha.{RESET}")

mtr3=matrix(3,3)

ler(mtr3)

print(f"{AMARELO}80. Leia uma matriz 3x3 e calcule a soma de todos os seus elementos.{RESET}")

s=0
for i in mtr3:
    for n in i:
        s+=n
print(s)

print(f"{AMARELO}81. Leia uma matriz 4x4 e calcule a soma dos elementos da diagonal principal.{RESET}")

sd=0
mtr4=matrix(4,4)
ler(mtr4)

dg=0
for i in mtr4:
    sd+=i[dg]
    dg+=1

print(sd)

print(f"{AMARELO}82. Leia uma matriz 3x3 e conte quantos elementos são pares.{RESET}")

par=0

for i in mtr3:
    for n in i:
        if n%2==0:
            par+=1
print(f"{par} pare(s) na primeira matriz 3x3")

print(f"{AMARELO}83. Leia duas matrizes 2x2 e gere a matriz soma.{RESET}")

mtr2=matrix(2,2)
ler(mtr2)

mtr22=matrix(2,2)
ler(mtr22)
    

mtrs=[]

for i in range(len(mtr2)):
    vets=[]
    for n in range(len(mtr2[i])):
        vets.append(mtr2[i][n]+mtr22[i][n])
    mtrs.append(vets)

ler(mtrs)

print(f"{AMARELO}84. Leia uma matriz 3x3 e determine o maior valor armazenado e sua posição, linha e coluna.{RESET}")

maior=mtr3[0][0]
mem=f"maior numero da primeira matriz 3x3 = {mtr3[0][0]} linha {1} e coluna {1}"

for i in range(len(mtr3)):
    for n in range(len(mtr3[i])):
        if mtr3[i][n]>maior:
            maior=mtr3[i][n]
            mem=f"maior numero da primeira matriz 3x3 = {mtr3[i][n]} linha {i+1} e coluna {n+1}"
            
print(mem)

print(f"{AMARELO}85. Leia uma matriz 4x4 e exiba a soma de cada linha separadamente.{RESET}")

mtr4=matrix(4,4)
ler(mtr4)


for i in range(len(mtr4)):
    print(f"soma da linha {i} = {sum(mtr4[i])}")

print(f"{AMARELO}86. Faça a transposição de uma matriz 3x4 lida pelo usuário.{RESET}")

bas=matrix(3,4)

ler(bas)
print(" ")

trans=[]
for v in range(len(bas[0])):
   trans.append([])

for m in range(len(bas[0])):
    for v in range(len(bas)):
        trans[m].insert(v,bas[v][m])

ler(trans) 