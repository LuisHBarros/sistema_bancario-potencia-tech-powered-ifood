"""
Sistema bancario basico Python, implementando deposito, saque e extrato
"""
print("Bem vindo ao Pybank!")
saldo = 0.0
e = "Sim"
while e == "Sim":
    operacao = int(
        input("Qual operacao deseja executar?\n1-)Deposito 2-)Saque 3-)Extrato")
    )
    if operacao == 1:
        valor = float(input("Qual o valor do deposito?"))
        saldo += valor
    if operacao == 2:
        valor = float(input("Qual o valor do saque?"))
        if valor > saldo:
            print(f"Saldo insuficiente para realizar esse saque\n VALOR: R${saldo:.2f}")
            continue
        saldo -= valor
    if operacao == 3:
        print(
            f"""EXTRATO
              ____________________
              VALOR: R${saldo:.2f}"""
        )
    e = input("Deseja realizar outra operacao?\n(Sim) (NAO)")
print("Obrigado pela preferencia, Pybank")
