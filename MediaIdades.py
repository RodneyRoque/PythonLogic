#Calcule a média das idades e retorne a quantidade de alunos
qtdAlunos = 0
idade = 0
somaIdade = 0
somaAnterior = 0

while idade != 9999:
    somaAnterior = somaIdade
    idade = int(input("Digite a idade do aluno(9999 para encerrar):"))
    if idade == 9999:
        break
    qtdAlunos += 1
    somaIdade = somaAnterior + idade
    print("A soma das idades é:",somaIdade)

mediaIdade = somaIdade / qtdAlunos

print("\nA quantidade de alunos é de:",qtdAlunos)
print("A soma das idades foi de:",somaIdade)
print("E a idade média é de:",round(mediaIdade,2))

print("\nPROGRAMA ENCERRADO!")

#Minha solução foi criar uma variável somaIdade e SomaAnterior
#A somaAnterior recebe o valor anterior da somaIdade, para fazer a soma com o novo valor que será atribuído