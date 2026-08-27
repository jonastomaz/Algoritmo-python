dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(':'))
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(':'))

inicio = (dia_inicio * 24 * 60 * 60) + (hora_inicio * 60 * 60) + (minuto_inicio * 60) + segundo_inicio
fim = (dia_fim * 24 * 60 * 60) + (hora_fim * 60 * 60) + (minuto_fim * 60) + segundo_fim

duracao = fim - inicio

dias = duracao // (24 * 60 * 60)
duracao %= (24 * 60 * 60)
horas = duracao // (60 * 60)
duracao %= (60 * 60)
minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")