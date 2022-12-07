valor = 100
reajuste = 1.02
participantes = 10
valorfinal = 0

for meses in range(1,11,1):
    valorfinal = valor * participantes
    valor = valor * 1.02
    print(meses,"°mês =",round(valorfinal,2))
print("Seu valor final será de:",round((valorfinal/10),2))

