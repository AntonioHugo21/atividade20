# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.

quant_numeros = 100

impares = pares = 0

for cont in range (0,quant_numeros):
    if cont % 2 == 0:
        pares += 1
    else: 
        impares += 1
        
print(f'Existem {pares} números pares e {impares} números ímpares de 0 a {quant_numeros}')