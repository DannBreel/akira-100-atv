print("\033[42;30m     Atividade 41    \033[0m")
print("\033[102;30mExiba os números de 1 a 10 usando uma estrutura de repetição.\033[0m")
print(" ")

l = range(1,11)
for i in l:
    print(i)

print("\033[42;30m     Atividade 42    \033[0m")
print("\033[102;30mExiba os números pares de 0 a 100.\033[0m")
print(" ")

l1=range(101)
for i in l1:
    if i%2==0:
        print(i)

print("\033[42;30m     Atividade 43    \033[0m")
print("\033[102;30mLeia um número inteiro n e calcule a soma de 1 até n.\033[0m")
print(" ")

lo = 5
n = int(input("numb maior q 5="))
print(lo)
while lo < n:
    lo += 1
    print(lo)
    
print("\033[42;30m     Atividade 44    \033[0m")
print("\033[102;30mLeia um número inteiro e exiba sua tabuada de 1 a 10.\033[0m")
print(" ")

num=int(input("num pra tabua="))
end=num*10
re = num
print(num)
while re < end:
    re += num
    print(re)

print("\033[42;30m     Atividade 45    \033[0m")
print("\033[102;30mLeia 5 números inteiros e mostre a soma total deles.\033[0m")
print(" ")

s=0
r = list(range(0,65,16))
print(r)
for i in r:
    i+=s
    s=i
    print(i)
print(sum(r))

print("\033[42;30m     Atividade 46    \033[0m")
print("\033[102;30mLeia 10 números e informe quantos são positivos, quantos são negativos e quantos são zero.\033[0m")
print(" ")

import random
x = random.sample(range(-85,85), 10)
print(x)
for i in x:
    if i > 0:
        print(i,"= positivo")
    elif i < 0:
        print(i,"= negativo")
    else:
        print(i,"= zero")

print("\033[42;30m     Atividade 47    \033[0m")
print("\033[102;30mLeia um número inteiro n e calcule n fatorial.\033[0m")
print(" ")

nun=5
fat=list(range(1,nun+1))
f=1
print(nun)
for i in fat:
    i*=f
    f=i
    print(i)

print("\033[42;30m     Atividade 48    \033[0m")
print("\033[102;30mGere a sequência de Fibonacci com os 15 primeiros termos.\033[0m")
print(" ")

yu = 1
ai = 0
for i in range(16):   
    tmp= yu + ai
    ai= yu
    yu=tmp
    print(yu)

