nome = input('Digite o nome do lutador: ')

peso = float(input('Agora digite o peso do lutador: '))

if peso < 52:
    print(f"O lutador {nome} está abaixo da faixa de peso"
          f" aceitável nas categorias({peso}kg).")
elif peso >= 52 and peso < 65:
    print(f"Peso pena('{peso}kg.')")
elif peso >= 65 and peso < 72:
    print(f"Peso Leve('{peso}kg.')")
elif peso >= 72 and peso < 79:
    print(f"Peso Ligeiro('{peso}kg.')")
elif peso >= 79 and peso < 86:
    print(f"Peso Meio-médio('{peso}kg.')")
elif peso >= 86 and peso < 90:
    print(f"Peso Médio('{peso}kg.')")
elif peso >= 90 and peso < 100:
    print(f"Peso Meio-Pesado('{peso}kg.')")
else:
    print(f"Peso Pesado('{peso}kg.')")
