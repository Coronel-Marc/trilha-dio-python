import textwrap
'''
imports
'''



'''
====================================
FUNÇÕES
'''
def exibir_menu():
    menu = """

    [e]\tExtrato
    [d]\tDepositar
    [s]\tSacar
    [nc]\tNova Conta
    [lc]\tLista Contas
    [nu]\tNovo Usuario
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    #usuarios
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                n_saques=numero_saques,
                l_saques=LIMITE_SAQUES
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1

            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        
def sacar (*, saldo, valor, extrato, limite, n_saques, l_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedido = n_saques >= l_saques
##=======================================

    if saldo_excedido:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif limite_excedido:
        print("Operação falhou! O valor do saque excede o limite.")

    elif saques_excedido:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        n_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

##=======================================
    
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    try:
        if valor > 0:


            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n Deposito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    except Exception as e:
        print(f"Houve um erro inesperado na função Deposito: {e}. \nNenhum dado fora alterado/adicionado")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuario com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf
    ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print("\n Conta criada com sucesso!")
        return {"agencia":agencia,"numero_conta": numero_conta, "usuario":usuario}
    
    print("Usuario não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

funcoes = {
    'e': exibir_extrato,
    'd':depositar,
    's':sacar,
    'nc':criar_conta,
    'lc':listar_contas,
    'nu':criar_usuario,
}
'''
FUNÇÕES
====================================
'''
main()