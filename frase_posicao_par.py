frase = input("Digite uma palavra ou frase:")
frase = frase.lower()
resultado = ""
i = 1 
for letra in frase:
    if letra.isalpha() and i % 2 == 0:
        resultado += letra.upper()
    else:
        resultado += letra
    i += 1

print(f"resultado final: {resultado}")