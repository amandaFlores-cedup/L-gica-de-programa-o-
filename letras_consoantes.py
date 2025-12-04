palavra = "programação em linguagem python"
novapalavra = ""
for letra in palavra:
    if letra != "a" or letra != "e" or letra != "i" or letra != "o" or letra != "u":
        novapalavra = novapalavra + letra

print(novapalavra)