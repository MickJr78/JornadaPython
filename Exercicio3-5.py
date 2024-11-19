time = int(input("Digite um valor de tempo em segundos: "))

hora = time // 3600
minuto = (time % 3600) // 60
segundo = (time % 60)

resultado = f'{hora} hora(s), {minuto} minuto(s) e {segundo} segundo(s).'

print(resultado)
