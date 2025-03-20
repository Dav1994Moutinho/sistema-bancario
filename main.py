menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

numero_transacoes = 0
LIMITE_TRANSACOES = 10

while True:

  opcao = input(menu)



### CÓDIGO PARA DEPOSITAR
  if opcao == "d":
    if numero_transacoes >= LIMITE_TRANSACOES:
      print ("Limite diário de transações excedido")

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      numero_transacoes += 1

    else:
      print("Operação falhou! O valor informado é inválido!")



# CÓDIGO PARA SACAR    
  elif opcao == "s":
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    excedeu_transacoes = numero_transacoes >= LIMITE_TRANSACOES

    if excedeu_saldo:
      print("Seu saldo é insuficiente.")

    elif excedeu_limite:
      print("O valor do saque excede o limite.")

    elif excedeu_saques:
      print("Número máximo de saques excedido.")

    elif excedeu_transacoes:
      print("Limite diário de transações excedido!")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
      
    
    else:
      print("Valor informado é inválido.")



### CÓDIGO PARA EXIBIR EXTRATO   
  elif opcao == "e":
    print("\n================ EXTRATO ================")
    print("não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"Transaões: {numero_transacoes}/10")
    print("=========================================")


### CÓDIGO PARA SAIR DA APLICAÇÃO
  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")