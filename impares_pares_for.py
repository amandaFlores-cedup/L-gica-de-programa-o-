numeros = []
pares = []
impares = []
for i in range(10):
    numero = int(input(f" Digite o {i+1} numero :")) 
    numeros.append(numero)
    if numero % 2==0:
        pares.append(numero)
    else:
        impares.append(numero)
    print(f" Os numeros digitados foram: {numeros}")
    print(f" desses numeros os pares são: {pares}")
    print(f" Desses numeros os impares são: {impares}")