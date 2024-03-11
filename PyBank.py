menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> '''

saldo = 0
limite = 500
extrato= ""
num_saques= 0 
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float (input("Qual o valor do deósito? "))

        if valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Deu erro na operação! Valor informado é invlido para prosseguir")

    elif opcao == "s":
        valor = float(input("Qual vai ser o valor do saque? "))
        
        ultrapassou_saldo = valor > saldo
        ultrapassou_limite =  valor > limite
        ultrapassou_saques = num_saques >= LIMITE_SAQUES

        if ultrapassou_saldo:
            print("Operação Falhou Você não tem saldo suficiente")
        elif ultrapassou_limite:
            print("Operação Falhou! Você passou o nosso limite para saques")
        elif ultrapassou_saques:
            print("Operação Falhou! Pois você ultrapassou o limite de seus saques diarios")
            
        elif valor > 0:
            saldo = valor
            extrato += f"saque: R$ {valor:.2f}\n"
        else:
            print("Algo deu errado! Pois seu valor inserido é invalido")

    elif opcao == "e":
        print("\n=========EXTRATO==========")
        print("Não foi feitas nenhuma movimentação em sua conta." if not extrato else extrato)
        print(f"\n saldo R$: {saldo:.2f}")
        print("=========================")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")

