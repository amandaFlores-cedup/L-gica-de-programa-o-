print("**** MENU PRINCIPAL") 
print("1 para incluir")
print("2 para alterar")

opcao = input("Sua opção = ")

if opcao == "1":
   import incluir
elif opcao == "2":
    import alterar
else:
    print("ERROU!")
    