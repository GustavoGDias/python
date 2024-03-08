'''from random import *
people=[]
while True:
    person=input("Enter a person participating.(end to exit):\n")
    if person=="end": break
    people.append(person)


shuffle(people)
for i in range(len(people)):
    print(people[i],"buys for",people[(i+1)%(len(people))])'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# Lista de participantes e seus e-mails
participantes = {
    'leo': 'exemple@gmail.com',
    'gustavo': 'exemple@gmail.com',
    'lucas': 'exemple@gmail.com',
    # Adicione mais participantes conforme necessário
}

# Função para realizar o sorteio e enviar e-mails
def enviar_amigo_secreto(participantes):
    lista_participantes = list(participantes.keys())
    random.shuffle(lista_participantes)

    for i, participante in enumerate(lista_participantes):
        amigo_secreto = lista_participantes[(i + 1) % len(lista_participantes)]

        # Enviar e-mail para o participante com seu amigo secreto
        enviar_email(participante, participantes[participante], amigo_secreto)

# Função para enviar e-mail
def enviar_email(nome, email, amigo_secreto):
    remetente = 'exemple@gmail.com'  # Seu e-mail
    senha = 'exemplepassword'  # Sua senha

    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = email
    mensagem['Subject'] = 'Resultado do Amigo Secreto'

    corpo_email = f'Olá, {nome}!\n\nSeu amigo secreto é: {amigo_secreto}'

    mensagem.attach(MIMEText(corpo_email, 'plain'))

    # Configuração do servidor SMTP para envio do e-mail
    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)  # Substitua pelos detalhes do seu servidor SMTP
    servidor_smtp.starttls()
    servidor_smtp.login(remetente, senha)
    servidor_smtp.sendmail(remetente, email, mensagem.as_string())
    servidor_smtp.quit()

# Chamando a função para realizar o sorteio e enviar e-mails
enviar_amigo_secreto(participantes)
