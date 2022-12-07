"""
Como descobrir se um número é impar ou par

"""
numero = 0

print(50 * "-") #Criando linhas no terminal de maneira simples
while numero != 9999:
    numero = int(input("Insira um número para saber se é par(9999 para finalizar): "))
    if (numero % 2) == 0:
        print(f"O {numero} é par")
    elif (numero % 2) != 0:
        print(f"O {numero} é impar")
print(50 * "-")

#Como saber se um número é impar ou par?
#Se o módulo/resto da divisão por 2 do número for igual a 0, ele é par
#Caso contrário, se for diferente de 0, é um número impar
#Módulo em python é definido por %