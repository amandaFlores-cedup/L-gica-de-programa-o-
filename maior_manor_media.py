numeros = []
contador = 0
while contador <10:
    num = int(input("Digite um numero:"))
    numeros.append(num)
    contador += 1
maior = max (numeros)
menor = min (numeros)
media = sum (numeros)
qtd_digitado = len(numeros)
print(f"Maior numero digitado:{maior}")
print(f"Menor número digitado:{menor}")
print(f"Média dos numeros digitados:{media}")
print(f"Quantidade de numeros digitados:{qtd_digitado}")