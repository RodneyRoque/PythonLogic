#01 - Área de um retângulo
"""
baseRetangulo = float(input("Digite a base do retângulo: "))
alturaRetangulo = float(input("Digite a altura do retângulo: "))
areaRetangulo = baseRetangulo * alturaRetangulo

print(round(areaRetangulo, 2))
"""

#02 - Desconto produto
"""
ValProduto = float(input("Digite o valor do seu produto: "))
PorcentagemDesconto = float(input("Digite a porcentagem de desconto: "))
DescontoDecimal = PorcentagemDesconto/100
DescontoFinal = ValProduto * DescontoDecimal
ValFinal = ValProduto - DescontoFinal

print("O seu produto agora vale: R$" + str(ValFinal))
"""

#03 - Área de um círculo
"""
pi = 3.141592
raio = float(input("Digite o raio do círculo: "))
areaCirculo = pi * (raio ** 2)

print("A área do círculo é: ",round(areaCirculo, 2))
"""

#04 - Reais para Dólar
"""
vreal = float(input("Digite o valor em reais(R$): "))
vdolar = vreal / 5.15

print("O resultado da conversão é de: $",round(vdolar, 2))
"""

#05 - Dólares para real
"""
vdolar = float(input("Digite o valor em dólares($): "))
vreal = vdolar * 5.15

print("O resultado da conversão é de R$",round(vreal, 2))
"""