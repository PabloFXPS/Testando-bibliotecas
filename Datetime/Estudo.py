from datetime import datetime
#
# agora = datetime.now()
# print(agora)
# print(agora.day) #dia
# print(agora.month) #mes
# print(agora.year) #ano
# print(agora.hour) #horas
# print(agora.minute) #minutos
# print(agora.second) #secundos
#
# print(agora.strftime("Hoje é dia %d do mes %m do ano %Y")) #formatação de texto com datas
# print(agora.strftime("Agora são %H horas e %M minutos")) #formatação com horas
#
# aniversario = datetime(2000,5,20)
# print(aniversario)
#
# data_str = "20/04/2025"
# data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
# print(data_convertida)

from datetime import timedelta #calculos com datas

hoje = datetime.now()
um_dia = timedelta(days = 1)

prazo = datetime(2026,3,30)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
amanha = hoje + um_dia
if amanha > prazo:
    print("Prazo vencido!")
else:
    print("Ainda esta no prazo")
print("Amanha é :",amanha)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
ontem  = hoje - um_dia
if ontem > prazo:
    print("Prazo vencido!")
else:
    print("Ainda esta no prazo")
print("Ontem foi:",ontem)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
futuro = datetime(2026,8,5)
dias_restantes = futuro - hoje
print(dias_restantes.days,"Para o dia 05/08/2026")