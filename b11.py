print("\033[43m\033[1m\033[30m===========================\033[0m")
print("\033[43m\033[1m\033[30mBLOCO 11 — RECURSIVIDADE\033[0m")
print("\033[43m\033[1m\033[30m===========================\033[0m")
print("\033[43m \033[0m")

print("\033[43m\033[30m95. Implemente uma função recursiva para calcular o fatorial de um número inteiro não negativo.\033[0m")
print("\033[43m \033[0m")

def aiai(x):
    if x==1:
        return 1
    else:
        return x*aiai(x-1)

print(aiai(6))

print("\033[43m\033[30m96. Implemente uma função recursiva para calcular a soma dos n primeiros números naturais.\033[0m")
print("\033[43m \033[0m")

def soma(x):
    if x==1:
        return 1
    else:
        return x + soma(x-1)

print(soma(21))

print("\033[43m\033[30m97. Implemente uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci e, ao final, discuta por que essa solução pode ser ineficiente para valores grandes.\033[0m")
print("\033[43m \033[0m")

# F(n)=F(n-1)+F(n-2)

#Breakdown:  F(2)=F(1)+F(0)
#            F(3)=F(2)+F(1)     F(1)+F(0) + F(1) 
#            F(4)=F(3)+F(2)     F(1)+F(0) + F(1) + F(1)+F(0)

def fibo(n):
    if n==0:    
        return 0
    if n==1:
        return 1
    
    return fibo(n-1)+fibo(n-2)

print(fibo(int(input("fibo"))))

# caralhou sou um genio slk

# se coloca um numero muito alto o bagulho crasha ou demora muito pra responde
# acho só que o python deve ser muito mal otimizado pra lidar com contas muito extensas
# e tbm pq funções só podem ser chamadas um numero limitado de vezes "RecursionError: maximum recursion depth exceeded"

print("\033[43m\033[1m\033[30m===========================\033[0m")
