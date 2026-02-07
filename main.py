print("Bem-vindo à Loja de Gelados do Junior Rodrigues")
print("---------------- Cardápio ----------------")
print("| Tamanho | Cupuaçu (CP) | Açaí (AC) |")
print("|    P    |   R$  9.00   | R$ 11.00  |")
print("|    M    |   R$ 14.00   | R$ 16.00  |")
print("|    G    |   R$ 18.00   | R$ 20.00  |")
print("------------------------------------------")

# Inicializa o acumulador do valor total
total = 0

# Início do loop principal
while True:

    # Loop para validar o sabor
    while True:
        sabor = input("Entre com o sabor desejado (CP/AC): ").lower()
        if sabor != "cp" and sabor != "ac":
            print("Sabor inválido. Tente novamente")
            continue
        break

    # Loop para validar o tamanho
    while True:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()
        if tamanho != "p" and tamanho != "m" and tamanho != "g":
            print("Tamanho inválido. Tente novamente")
            continue
        break

    # Estrutura condicional aninhada para calcular o preço
    if sabor == "cp":
        if tamanho == "p":
            preco = 9.00
            produto = "Cupuaçu"
        elif tamanho == "m":
            preco = 14.00
            produto = "Cupuaçu"
        else:
            preco = 18.00
            produto = "Cupuaçu"
    else:
        if tamanho == "p":
            preco = 11.00
            produto = "Açaí"
        elif tamanho == "m":
            preco = 16.00
            produto = "Açaí"
        else:
            preco = 20.00
            produto = "Açaí"

    # Mostra o pedido ao usuário
    print(f"Você pediu um {produto} no tamanho {tamanho.upper()}: R$ {preco:.2f}")

    # Soma ao total acumulado
    total += preco

    # Pergunta se deseja continuar
    continuar = input("Deseja mais alguma coisa? (S/N): ").lower()

    # Se o usuário não quiser continuar, encerra o loop
    if continuar != "s":
        break

# Exibe o valor total ao final
print(f"O valor total a ser pago: R$ {total:.2f}")
