i = 1
soma = 0
while i <= 100:
    if i % 3==0 and i % 5==0:
        print(f"{i} é multiplo de 3 e 5")
        soma += i
    i+=1 

print(f"Soma total dos numeros: {soma}")