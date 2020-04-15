segundos = eval(input("Insira quantos segundos você deseja converter: "))
a = segundos//60//60//24
b = (segundos//60//60)%24
c = (segundos//60)%60
d = segundos % 60

print(a, "dias,", b, "horas,", c, "minutos e ", d, "segundos.")