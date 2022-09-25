##executar no terminal
##pip install mysql-connector-python==8.0.28


import mysql.connector
from mysql.connector import errorcode

print('Conectando...')
try:
    conn= mysql.connector.connect(
          host='127.0.0.1',
          user='root',
          password='1234'
        )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `login`;")

cursor.execute("CREATE DATABASE `login`;")

cursor.execute("USE `login`;")

# criando tabelas
TABLES = {}
TABLES['Login'] = ('''
      CREATE TABLE 'login' (
      `email` varchar(50) NOT NULL,
      `nome` varchar(20) NOT NULL,
      `CPF` varchar(11) NOT NULL,
      PRIMARY KEY ('email')
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Problemas'] = ('''
      CREATE TABLE 'problemas' (
      'problema' varchar(150) NOT NULL,
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO login (email, nome, CPF) VALUES (%s, %s, %s)'
usuarios = [
      ("victor.portela@fatec.sp.gov.br", "Victor", "12345678910"),
      ("pedro.pucci@fatec.sp.gov.br", "Pedro", "10987654321"),
      ("gustavo.abreu6@fatec.sp.gov.br", "Gustavo", "23456789010")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from login.login')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo problemas
problemas_sql = 'INSERT INTO problemas (problemas) VALUES (%s)'
problemas = [
      ('Computador liga a tela'),
      ('Computador não liga'),
      ('Teclado não funciona'),
      ('Computador não tem conexão a internet')
]
cursor.executemany(problemas_sql, problemas)

cursor.execute('select * from login.problemas')
print(' -------------  Problemas:  -------------')
for problema in cursor.fetchall():
    print(problema[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
