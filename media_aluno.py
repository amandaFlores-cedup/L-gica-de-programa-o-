continua = True
nome_aluno = []
nota01 = []
nota02 = []
media_geral = []

while continua:
    nome = input("Digite nome do aluno:")
    nome_aluno.append(nome)
    n1 = float(input("Digite nota 01:"))
    nota01.append(n1)
    n2 = float(input("Digite nota 02:"))
    nota02.append(n2)
    media = (n1 + n2)/2
    media_geral.append(media)
    prossegue = input("Deseja continuar (S/N)". lower())
    if (prossegue == 'n'):
        continua = False

for i in range (len(nome_aluno)):
    print(f"{nome_aluno[i]}: nota 01:{nota01[i]} nota 02:{nota02[i]} -- media geral{media_geral[i]}")