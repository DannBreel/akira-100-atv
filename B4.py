print("\033[41;30m     Atividade 31    \033[0m")
print("\033[44;30mLeia um número inteiro e informe se ele é positivo, negativo ou zero.\033[0m")
print(" ")

x=int(input("number pls:"))
if x>0:
    print("positivo")
elif x==0:
    print("zero")
else:
    print("negativo")

print("\033[41;30m     Atividade 32    \033[0m")
print("\033[44;30mLeia um número inteiro e informe se ele é par ou ímpar.\033[0m")
print(" ")

print(x)
if x%2 >0:
    print("impar")
else:
    print("par")

print("\033[41;30m     Atividade 33    \033[0m")
print("\033[44;30mLeia dois números e mostre qual deles é o maior, ou informe se são iguais.\033[0m")
print(" ")

y=int(input("insert second number:"))
if x>y:
    print(x,">",y)
elif x==y:
    print(x,"=",y)
else:
    print(x,"<",y)

print("\033[41;30m     Atividade 34    \033[0m")
print("\033[44;30mLeia a média final de um aluno e informe se ele foi aprovado, em recuperação ou reprovado.\033[0m")
print(" ")

n1=int(input("nota 1:"))
n2=int(input("nota 2:"))
med = (n1+n2)/2
if med >= 70:
    print("aprovved")
elif med >= 40:
    print("recup")
else:
    print("reproved")

print("\033[41;30m     Atividade 35    \033[0m")
print("\033[44;30mLeia um ano e informe se ele é bissexto.\033[0m")
print(" ")

an = int(input("give me ano"))

print("é bissexto?",an%4==0)

print("\033[41;30m     Atividade 36    \033[0m")
print("\033[44;30mLeia três lados e verifique se podem formar um triângulo. Caso possam, informe se é equilátero, isósceles ou escaleno.\033[0m")
print(" ")

a1 = int(input("lado 1 triangulo"))
a2 = int(input("lado 2"))
a3 = int(input("lado 3"))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a2 + a1:
    if a1==a2==a3:
        print("equilatero")
    elif a1==a2 or a2==a3 or a3==a1:
        print("isosceles")
    else:
        print("escaleno")
else:
    print("não forma triangulo")

print("\033[41;30m     Atividade 37    \033[0m")
print("\033[44;30mLeia o preço de um produto e calcule o valor final conforme a forma de pagamento: à vista com desconto, em 2 vezes sem juros ou em 3 vezes com acréscimo.\033[0m")
print(" ")

pr = int(input("preço ="))
print("á vista:",pr-(pr*0.10))
print("2x sem juro:",pr/2,"2x")
print("3x com juro:",(pr+(pr*0.15))/3,"3x")

print("\033[41;30m     Atividade 38    \033[0m")
print("\033[44;30mLeia peso e altura de uma pessoa, calcule o IMC e classifique o resultado em faixas.\033[0m")
print(" ")

pe = float(input("peso="))
al = float(input("altura="))
if al ==0:
    al+=1
    print("formiga no pc")

imc = pe/(al**2) 

if imc <= 16:
    print("desnutrição severa")
elif 16<imc<18.5:
    print("desnutrição braba")
elif 18.5<=imc<=22:
    print("peso baxo")
elif 22<imc<25:
    print("normal")
elif 25<=imc<30:
    print("gordo")
elif 30<=imc<35:
    print("obesidade 1")
elif 35<=imc<40:
    print("obesidade 2")
elif 40<imc:
    print("obesidade 3")    


print("\033[41;30m     Atividade 39    \033[0m")
print("\033[44;30mLeia a idade de uma pessoa e classifique em categorias, por exemplo criança, adolescente, adulto ou idoso.\033[0m")
print(" ")

ida=int(input("gime idade"))
if ida>50:
    print("idoso")
elif ida>25:
    print("adulto")
elif ida>18:
    print("jovem")
else:
    print("criança")
    

print("\033[41;30m     Atividade 40    \033[0m")
print("\033[44;30mLeia duas notas e a frequência de um aluno. Informe se ele foi aprovado, reprovado por nota, reprovado por frequência ou reprovado por ambos.\033[0m")
print(" ")

pre=int(input("percentual de presença:"))

if med >= 70 and pre > 75:
    print("aprovved")
elif med >= 40 and pre > 75:
    print("recup")
else:
    print("reproved")