num = []
maior = 0 

for i in range (5):
    n = int(input("Digite um numero:"))
    num.append(n)
    if i == 0:
        maior = n 
    elif n > maior:
        maior = n
        indice = i

print (f"O maior numero é {num[indice]}")