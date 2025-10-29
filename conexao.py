import mysql.connector

def connectar():
    conexao = mysql.connetor.connect(
    host="localhost",
    user="root",
    password="",
    database+"nome"
    )
    return conexao