"""
Estruturas de repetição - loops

while
for
do while

"""

a = 0

while a <= 5: #LOOP com while, vai aumentar o valor de a de 1 em 1, até o valor se tornar 5
    print(a) 
    """if a == 3:
        break""" #Comando break, usado para terminar o loop
    a = a + 1 
else: #Pode ser usado Else com While
    print(f"a não é menor ou igual a 5. Valor de a:{a}")

#Os próximos comandos só serão executados após o término do loop
print("Resultado final de a: ",a) #Valor se tornou 6, então saiu do loop

