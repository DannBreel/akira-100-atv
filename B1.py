print('\033[44m     Atividade 01     \033[0m')
nome=input("Seu nome é?")
print("bem vindo",nome,"!")

######################
print(" ")
print('\033[44m     Atividade 02     \033[0m')

at2 = int(input("numero pls:"))
print(at2,at2+1,at2-1)

######################
print(" ")
print('\033[44m     Atividade 03     \033[0m')

print(float(at2+0.12))

######################
print(" ")
print('\033[44m     Atividade 04     \033[0m')

atv4=int(input("idade?"))
print("você tem",atv4,"anos!")

######################
print(" ")
print('\033[44m     Atividade 05     \033[0m')

atv5 = input("altura pls:")
Aa5 = [nome,atv4,atv5]

print(" ")

for i in Aa5:
    print(i)

######################
print(" ")
print('\033[44m     Atividade 06     \033[0m')

print("seu nome tem",len(nome),"letras!")

######################
print(" ")
print('\033[44m     Atividade 07     \033[0m')

print(nome.lower())
print(nome.upper())

######################
print(" ")
print('\033[44m     Atividade 08     \033[0m')

print(atv4>18)

######################
print(" ")
print('\033[44m     Atividade 09     \033[0m')

lo1="aiai meu bumbumn"
lo2="nada ve zé"
print(lo1)
print(lo2)
print(" ")
print(lo1,lo2)

######################
print(" ")
print('\033[44m     Atividade 10     \033[0m')

city = str(input("city é?"))
plp = int(input("habitants?"))

print("cidade",city,",número de habitantes =",plp)
