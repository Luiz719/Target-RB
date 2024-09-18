
def calcular_soma():
    indice = 12
    soma = 0
    k = 1
    while k < indice:
        k = k + 1
        soma = soma + k
    return soma

print(f"O valor final de SOMA é {calcular_soma()}.")
