"""
Do While

Código para adivinhr um número

"""

#palpite = 0
#numero = 9

#while palpite != numero:
    #print("Qual o número correto? ")
    #palpite = int(input())
    #print("Puts, você errou!")
    #print("Vamos, tentar de novo")

#print("Parabéns você acertou!")

"""VERSÃO 2.0 com boolean"""

palpite = 5
numero = 9

while bool(palpite) is True:
    print("Qual o número correto? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns, você acertou!")
        break
    else:
        print("Você errou!")
else:
    print("Erro na aplicação")

print(bool(palpite))
