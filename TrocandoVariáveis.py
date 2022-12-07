"""
Exercício - trocar variáveis

"""
#Trocando variáveis em python

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

#Criaremos uma variável temporária

temp = x
x = y
y = temp

print(f"O valor de x depois da troca: {x}")
print(f"O valor de y depois da troca: {y}")

#Na programação estruturada temos uma estrutura, ou seja, inicio-meio-fim
#Então na ordem de nosso programa, tudo será lido do começo ao final do código
#A variável temporária receberá o valor de x, logo após o valor de x será substituido 
#pelo valor de y. E por último o valor de y será substituído pela variável temporária