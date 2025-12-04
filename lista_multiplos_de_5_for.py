numeros = []
multiplo_de_5 = []
for i in range (15):
    num = int(input("Dígite um número:"))
    numeros.append(num)
    if num % 5 == 0:
        multiplo_de_5.append(num)
print(f"Os números dígitados foram: {numeros}")
print(f"Dentre esses números os multiplos de 5 são: {multiplo_de_5}")