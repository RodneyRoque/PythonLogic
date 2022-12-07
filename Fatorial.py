"""
Como achar o fatorial de um número

"""

"""Isso é um fatorial:"""
#4! = 4*3*2*1
#9! = 9*8*7*6*5*4*3*2*1
#0! = 1
#1! = 1

print(30 * "-")
numero = int(input("Insira um numero para realizar uma fatoração: "))
fatorial = 1

if numero < 0:
    print("Não existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} é 1")
else:
    for x in range(1,numero+1): #Como no range o número máximo alcançado será -1 do numero desejado, para usarmos a variavel é necessário somar +1
        fatorial *= x #O mesmo que: fatorial = fatorial * x
        #print(f"Fatorando {numero}: {fatorial}")
    print(f"O fatorial de {numero} é: {fatorial}")
print(30 * "-")