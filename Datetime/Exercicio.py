from datetime import datetime
data = datetime.now()

# Exercício 1 – Relógio de verificação
# Mostre a hora atual no terminal, mas com a seguinte regra:

# Se a hora for antes das 12h, imprima: "Bom dia!"
# Se estiver entre 12h e 18h: "Boa tarde!"
# Depois disso: "Boa noite!"
horario_atual = datetime.now()
horas = horario_atual.hour
minutos = horario_atual.minute

if 6 < horas < 13:
    print(f"Bom dia! horário atual:{horas}:{minutos}")
elif 13 <= horas < 18:
    print(f"Boa tarde! horário atual:{horas}:{minutos}")
else:
    print(f"Boa noite! horario atual:{horas}:{minutos}")

# Exercício 2 – Quantos meses faltam?
# Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

# Hoje é o 4º mês do ano. Ainda faltam 8 meses para terminar o ano!
meses_total = 12
mes_atual = data.month
faltam = meses_total - mes_atual

print(f"Você esta no mês {mes_atual}. Faltam {faltam} para acabar o ano.")

# Exercício 3 – Assinatura digital do terminal
# Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:

# Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02
# A data e horário devem ser do momento atual da assinatura

def assinatura(nome):
    atual = datetime.now()
    return atual.strftime(f"Assinatura gerada por {nome} em %d de %h de %Y às %H:%M")

assinado = assinatura(str(input("Escreva seu nome para gerar a assinatura: ")))
print(assinado)

# Exercício 4 – Contagem regressiva para o fim do ano
# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.
hoje_ex1 = data.now()
final_ano = datetime(month=12,day=31,year=data.now().year)
faltam= final_ano - hoje_ex1
print(f"Para o final de ano faltam: {faltam.days} dias")

# Exercício 5 – Verificador de evento
# Peça ao usuário que digite uma data de um evento
# Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.
def evento(dia,mes,ano):
  evento = datetime(year=ano,month=mes,day=dia)
  hoje = datetime.now()
  faltam = evento - hoje
  if evento.date() == hoje.date():
      print("Hoje é o dia do evento.")
  elif hoje.date() > evento.date():
      print("Essa data já passou.")
  elif hoje.date() < evento.date():
      horas = faltam.seconds // 3600 #calcular horas que faltam ex: 7200//3600 = 2
      print(f"Faltam:{faltam.days} dias e {horas} horas para o evento.")

evento(dia=int(input("Dia do evento:")),mes=int(input("Numero do mes:")),ano=int(input("Ano:")))

# Exercício 6 – Validade de produto 🥫
# Peça ao usuário para informar a data de fabricação de um produto.
# Considere que ele vence em 180 dias.

# Mostre:
# A data de validade
# Se o produto ainda está válido ou já venceu
# Quantos dias faltam ou há quanto tempo passou do prazo

def validade(dia,mes,ano):
    from datetime import timedelta
    validade = timedelta(days=180)
    fabricacao = datetime(year=ano,month=mes,day=dia)
    hj = datetime.now()
    diferenca = hj - fabricacao

    print(f"Data de validade: {fabricacao.strftime('%d/%m/%Y')}. dias: {diferenca.days}")
    if diferenca.days == 0:
        return f"O produto vence hoje."
    elif diferenca < validade:
        return f"O produto não esta vencido."
    elif diferenca > validade:
        return f"O produto esta vencido."
    return None

p1 = validade(dia = int(input("Dia da fabricação:")),mes= int(input("Numero do mes:")),ano=int(input("Ano:")))
print(p1)