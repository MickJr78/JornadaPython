# PEDE AO USUÁRIO QUE DIGITE UM TEXTO, E EXIBE NA TELA O TEXTO DIGITADO MAIS A QUANTIDADE
# DE LETRAS QUE A STRING POSSUI, ENCERRANDO O LOOP QUANDO FOR DIGITADO 'FIM' EM MAIÚSCULAS.


while True:
    palavra = input("Digite um texto e vamos saber quantas letras ela tem: ")
    if palavra != 'FIM':
        print(f"A palavra {palavra} tem", len(palavra), "letras!")
    else:
        print("Fim da Execução.")
        break