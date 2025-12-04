numeros = []
multiplo_de_5 = []
numero = 1
while numero <=15:
    num = int(input("Dígite um número:")) 
    numeros.append(num)
    if num % 5 == 0:
        multiplo_de_5.append(num)
    numero += 1
print(f"Os números digitados foram: {numeros}")
print(f"Desses números os multiplos de 5 são: {multiplo_de_5}")