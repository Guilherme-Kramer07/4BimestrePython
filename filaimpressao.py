def menu():
    fila_impressao=FilaDeImpressao()
    fila_impressao.configurar_inicial()
    
    while True:
        print("Opções:")
        print("1 Adiciona um trabalho na fila da impressao")
        print("2. imprimir o proximo trabalho da fila")
        print("3. mostrar a fila de impressao")
        print("4. sair")
        escolha = input("escolha uma opcao 1-4")
    if escolha == "1":
        trabalho = input("Digite o nome do trabalho a ser impresso")
        fila_impressao.adicionar_trabalho(trabalho)
    elif escolha == "2":
        fila_impressao.processar_trabalho()
    elif escolha =="3":
        fila_impressao.mostrar_fila()
    elif escolha == "4":
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")
