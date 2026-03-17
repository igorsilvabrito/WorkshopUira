class Calculadora:
    def __init__(self, soma, subtracao, divisao, multiplicacao):
        self.soma = soma
        self.subtracao = subtracao
        self.divisao = divisao
        self.multiplicacao = multiplicacao

    def soma(n1, n2):
        return n1 + n2
    
    def subtracao(n1, n2):
        return n1 - n2
    
    def divisao(n1, n2):
        return n1 / n2
    
    def multiplicacao(n1, n2):
        return n1 * n2
historico = []
operacao = ""

while True:
    
    numero= int(input("1 soma, 2 subtracao, 3 divisao, 4 multiplicacao, 5 - historico, 6 - Limpa Historico "))
    if(numero == 1):
        operacao = "Soma"
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))
        conta = f"{n1} + {n2}"
        resultado = Calculadora.soma(n1, n2)
        print("Resultado", resultado, "\n")
        historico.append(conta)
    if(numero == 2):
        operacao = "subtracao"
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))
        resultado = Calculadora.subtracao(n1, n2)
        print("Resultado", resultado, "\n")
        historico.append(conta)
    if(numero == 3):
        operacao = "divisao"
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))
        resultado = Calculadora.divisao(n1, n2)
        print("Resultado", resultado, "\n")
        historico.append(conta)
    if(numero == 4):
        operacao = "multiplicacao"
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))
        resultado = Calculadora.multiplicacao(n1, n2)
        print("Resultado", resultado, "\n")
        historico.append(conta)

    if numero == 5:
        print(historico)

    if numero == 6:
        historico.clear()
    
    




