"""
Python - Comandos de controle condicional

if, else e elif 

"""
x = 5
y = 8

if y > x:
    print("y é maior do que x")
elif y < x:
    print("y é menor do que x")
else:
    print("y é igual a x")
    
    
print("Código fora do bloco condicional")

#Simplificando os IFS, "Operador Ternário"
a = 5
b = 8

print("B") if b < a else print("A") #Operador ternário, Expressões Condicionais