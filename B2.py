print("\033[37m\033[41m    Atividade 11    \033[0m")


a1 = int(input("numb pls:"))
a2 = int(input("segundo numb pls:"))
a3 = int(input("esse nao importa n"))

if a2 == 0:
    dv="syntax error"
else:
    dv=a1/a2

print(a1+a2,a1-a2,a1*a2,dv)

########
print(" ")
print("\033[37m\033[41m    Atividade 12    \033[0m")

print(a1,a2,a3)
print((a1+a2+a3)/3)

########
print(" ")
print("\033[37m\033[41m    Atividade 13    \033[0m")

m = float(input("metros p/ converte"))
print("centimetros=",m*100,"| milimetros=",m*1000)

########
print(" ")
print("\033[37m\033[41m    Atividade 14    \033[0m")

bas = int(input("me de a base de um retangulo"))
alt = int(input("me de a altura de um retangulo"))

print("area=",bas*alt,"perimetro=",(bas*2)+(alt*2))

########
print(" ")
print("\033[37m\033[41m    Atividade 15    \033[0m")

rai = (int(input("raio do circulo")))
dio = (rai*2) #WWRYYYYYY
print("raio=",rai,"diametro=",dio,"circund=",dio*3.14,"area=",(rai**2)*3.14)


########
print(" ")
print("\033[37m\033[41m    Atividade 16    \033[0m")

pre = float(input("preco"))
des = float(input("desconto"))
print("preco descontado",pre-(pre*(des/100)))

########
print(" ")
print("\033[37m\033[41m    Atividade 17    \033[0m")

#igual a anterior
sal = float(input("salario"))
per = float(input("aumento em %"))
print("new salario",sal+(sal*(per/100)))

########
print(" ")
print("\033[37m\033[41m    Atividade 18    \033[0m")

#mudancas minimas
lil = float(input("litros consum."))
km = float(input("dist."))

print("consum. med.",km/lil,"km por L")

########
print(" ")
print("\033[37m\033[41m    Atividade 19    \033[0m")

day = int(input("days pls:"))
hr = int(input("houers pls:"))
mi = int(input("minits pls:"))

print("minutos nisso tudo ==",(day*1440)+(hr*60)+mi)

########
print(" ")
print("\033[37m\033[41m    Atividade 20    \033[0m")
    
if a2 == 0:
    a2 += 2

print(a1,"and",a2)
print(a1//a2," ", a1%a2)
