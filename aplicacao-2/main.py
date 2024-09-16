# recebe os dados, busca as informacoes no banco de dados, formata o arquivo bruto, gera o pdf, envia por email
import MySQLdb
from smtplib import SMTP
from loguru import logger

phones = input("Telefone(s): ")
send_mail = input("Envia o relatório por email? (Sim/Não): ")
path_raw_file = input("Caminho do arquivo bruto: ")
date = input("Data da confecção (Exemplo: 2024/01/10 06:00): ")

# trim, split
# phones in ('','')
# nao achou telefone, da erro

phone = ""

db = MySQLdb.connect(host="db", user="root", password="root", database="teste_nimbus")
c = db.cursor()
c.execute("""SELECT name, email FROM customers WHERE phone == '%s'""", (phone))

print("teste")

# input e tratar input
# buscar no banco de dados
# tratar arquivo bruto
# gerar pdf
# enviar por email
