print("\033[44;30m=====================================\033[0m")
print("\033[44;30mBLOCO 12 — OBJETOS E CLASSES\033[0m")
print("\033[44;30m=====================================\033[0m")
print(" ")

print("\033[44;30m     Atividade 98    \033[0m")
print("\033[104;30mCrie uma classe Pessoa com atributos nome e idade, além de um método para exibir os dados.\033[0m")
print(" ")

class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def mostrar(self):
        print(f"nome={self.nome} idade={self.idade}")

p1=Pessoa("roberto",21)

p1.mostrar()

print("\033[44;30m     Atividade 99    \033[0m")
print("\033[104;30mCrie uma classe Retangulo com atributos base e altura e métodos para calcular área e perímetro.\033[0m")
print(" ")

class Retangulo:
    def __init__(self,lado1,lado2):
        self.lado1=lado1
        self.lado2=lado2
    
    def perimetro(self):
        print(f"perimetro é igual a {(2*self.lado1)+(2*self.lado2)}")
    def area(self):
        print(f"area é igual à {self.lado1*self.lado2}")

r1=Retangulo(10,15)
r1.perimetro()
r1.area()

print("\033[44;30m     Atividade 100    \033[0m")
print("\033[104;30mCrie uma classe ContaBancaria com saldo inicial e métodos para depositar, sacar e exibir saldo, impedindo saques acima do valor disponível.\033[0m")
print(" ")

class ContaBancaria:
    def __init__(self,nome,saldo0):
        self.nome=nome
        self.saldo=saldo0
    
    def depositar(self,deposit):
        self.saldo+=deposit
        print(f"Valor de {deposit} realizado com sucesso")
        print(f"saldo disponivel pra saque={self.saldo} na conta de {self.nome}")
        print(" ")

    def saque(self,saque):
        if self.saldo<saque:
            print("ta quebrado chefe")
        else:
            self.saldo-=saque
            print(f"saque no valor de {saque} realizado com exitô")
        
        print(f"saldo disponivel pra saque={self.saldo} na conta de {self.nome}")
        print(" ")

nubamco=ContaBancaria("roberto",2)
nubamco.depositar(230)
nubamco.saque(232)
nubamco.saque(800)