total_geral = 0

while True:
    print("\n--- LOJA SIMPLES ---")
    print("1 - Comprar produto")
    print("2 - Ver total")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        total = preco * quantidade
        total_geral += total

        compra_grande = total > 100

        print(f"Você comprou {quantidade}x {nome}")
        print(f"Total da compra: R$ {total:.2f}")
        print("Compra grande:", compra_grande)

    elif opcao == "2":
        print(f"Total acumulado: R$ {total_geral:.2f}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
