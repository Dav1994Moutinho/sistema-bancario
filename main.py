from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


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
data_primeira_transacao = None


while True:

### validacao de 1 dia
  if data_primeira_transacao:
    agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
    data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

    if agora.date() > data_primeira_transacao.date():
      numero_transacoes = 0
      numero_saques = 0
      data_primeira_transacao = None
      print("\nNovo dia detectado. Contadores de transações e saques foram reiniciados.\n")

  opcao = input(menu)
    

### CÓDIGO PARA DEPOSITAR
  if opcao == "d":
    if numero_transacoes >= LIMITE_TRANSACOES:
      print ("Limite diário de transações excedido")
      continue

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
      agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
      data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      extrato += f"{data_formatada}\n\n"
      numero_transacoes += 1

      if not data_primeira_transacao:
        data_primeira_transacao = agora
      
    else:
      print("Valor informado é inválido!")


# CÓDIGO PARA SACAR    
  elif opcao == "s":

    if numero_transacoes >= LIMITE_TRANSACOES:
      print("Limite diário de transações excedido.")
      continue

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Seu saldo é insuficiente.")

    elif excedeu_limite:
      print("O valor do saque excede o limite.")

    elif excedeu_saques:
      print("Número máximo de saques excedido.")

    elif valor > 0:
      agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
      data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      extrato += f"{data_formatada}\n\n"
      numero_saques += 1
      numero_transacoes += 1
      
      if not data_primeira_transacao:
        data_primeira_transacao = agora
    
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