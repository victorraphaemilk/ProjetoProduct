import sessao_estudos
import nada
import redes_sociaisa
import bolsa
import processos




while True:
    mensagem_inicio = f'''{10*'-'} Olá Victor! {10*'-'}
{10*'-'} O que você deseja fazer? {10*'-'}
1 - Estudar
2 - Redes Sociais
3 - Bolsa
4 - Nada \n'''

    print(mensagem_inicio)

    resposta = input('* Insira sua resposta aqui:  ')

    match resposta:
        case "1":
            sessao_estudos.estudos()
            break  # Encerra o loop após executar a ação

        case '2':
            redes_sociaisa.redes()
            break  # Encerra o loop após executar a ação

        case '3':
            bolsa.executar()

        case '4':
            nada.sair()
            break  # Encerra o loop após executar a ação



        case _:
            processos.limpar_terminal()
            print("Opção inválida. Por favor, tente novamente.")

    



