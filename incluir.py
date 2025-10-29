from conexao import conectar

nome = input("Digite o nome a incluir: ")

con = conectar()
cursor = con.cursor()

cursor.execute("SELECT * from NOME where NOME = %s ", (nome))
resultado = cursor.fetchone ()

if resultado :
    print("Nome já existe")   
else:
    cursor.execute("INSERT INTO nomes (nome) values (%s)", (nome) )
    con.commit()
    print("nome inserido com sucesso!")
    
cursor.close()
con.close(  )