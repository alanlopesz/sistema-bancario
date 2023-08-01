#sistema bancário
#depósito, saque e extrato
#regras de saque: 3x por dia, max de 500 por vez
operacao = "\n[D] para depósito \n[S] para saque \n[E] para extrato\n[SAIR] para fechar o programa\n"
deposito = 0
saque = 0
saldo = 0.0
valor_depósito = []
valor_saque = []
while True:
    opcao = input(operacao).upper().strip()
    if opcao == "D":
        deposito = (float(input("Quantos reais você irá depositar? R$ ")))
        if deposito <= 0:
            print("o valor de deposito precisa ser maior do que 0 (zero) reais")
        else:
            valor_depósito.append(deposito)
            saldo += deposito
            print("Valor depositado com sucesso!")
    elif opcao == "S":
        if len(valor_saque) < 3:
            saque = float(input("Quantos reais você irá sacar? R$ "))
            if saque > 500 and saque < saldo:
                print("Não é possível sacar mais do que R$ 500 por vez")
            else:
                valor_saque.append(saque)
                saldo -= saque
                print("saque efetuado com sucesso!")
        else:
            print("você já excedeu o limite de saques hoje!")
    elif opcao == "E":
        print("="*25, "\nO seu saldo total é de: \nR$ {}\n".format(saldo))
        print("="*25)
        print("~"*25)
        print("\033[0;32m="*25)
        print("\033[0;32m\nos seus depósitos foram de:")
        for c in range(0, len(valor_depósito)):
            print("="*25)
            print("\nR$ {}".format(valor_depósito[c]))
        print("="*25)
        print("\033[0;0m~"*25)
        print("\033[1;31m="*25)
        print("\nos seus saques foram de:")
        for c in range(0, len(valor_saque)):
            print("="*25)
            print("\nR$ {}".format(valor_saque[c]))
        print("="*25, '\033[0;0m')
    elif opcao == "SAIR":
        print("\nSaindo...")
        break
    else:
        print("\ndigite uma opção válida!")