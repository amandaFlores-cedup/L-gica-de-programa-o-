multiplo_7 = []
for i in range (1,501):
    if i % 7 == 0:
        multiplo_7.append(i)
print(f"Os números multiplos de 7 em uma lista de 1 a 500 são: {multiplo_7}")
print(len(multiplo_7))