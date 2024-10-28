# VERIFICA SE NAS ELEIÇÕES MUNICIPAIS HAVERÁ OU NÃO SEGUNDO TURNO


nomeMunicipio = input('Informe o nome do seu Município: ')
qtdeEleitores = int(input(f'Agora informe a quantidade de eleitores que têm no município de {nomeMunicipio}:'))

if qtdeEleitores >= 200000:
    votosMaisVotado = int(input(f'Quantos votos teve o candidato mais votado em {nomeMunicipio}?'))
    if votosMaisVotado < (qtdeEleitores * 0.5):
        print(f'No município de {nomeMunicipio} HAVERÁ segundo turno.')
    else:
        print(f'No município de {nomeMunicipio} NÃO HAVERÁ segundo turno.')
else:
    print(f'No município de {nomeMunicipio} NÃO HAVERÁ segundo turno.')
