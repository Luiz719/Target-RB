
def verificar_ocorrencia_a(string):
    count = 0
    for char in string:
        if char.lower() == 'a':
            count += 1
    if count > 0:
        return f"A letra 'a' apareceu {count} vezes."
    else:
        return "A letra 'a' não apareceu na string."


string = input("Digite uma string: ")
print(verificar_ocorrencia_a(string))
