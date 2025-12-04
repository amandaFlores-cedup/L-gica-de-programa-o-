numeros = []
contador = 0
soma_impares = 0

while contador < 10:
    numero = int(input(f"Digite o {contador + 1} numero:"))
    numeros.append(numero)
    if numero % 2 != 0:
        soma_impares += numero
    contador +=1

print(f"Numeros digitados: {numeros}")
print(f"A soma dos impares é: {soma_impares}")