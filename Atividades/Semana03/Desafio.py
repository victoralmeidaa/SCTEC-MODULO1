print("========= Mini-LLM ======================")

nome = input("Qual é o seu nome? ")

while True:

    print(f"\nOlá, {nome}!")

    print("\nEscolha um assunto:")
    print("1 - Tecnologia")
    print("2 - Filmes")
    print("0 - Sair")

    opcao = input("\nDigite uma opção: ")

    if opcao == "0":
        print("\nAté logo!")
        break

    elif opcao == "1":

        interacoes = 0

        resposta = input("\nVocê gosta de programação? ")

        interacoes += 1

        while interacoes < 5:

            if resposta.lower() == "sim":

                print("\nProgramação é uma habilidade muito importante.")

                resposta = input("Qual linguagem você prefere? ")

            else:

                print("\nTalvez você ainda não tenha encontrado a área certa.")

                resposta = input("Você gostaria de aprender programação? ")

            interacoes += 1

        print("\nFim da conversa sobre tecnologia.")

    elif opcao == "2":

        interacoes = 0

        resposta = input("\nVocê gosta de filmes de ação? ")

        interacoes += 1

        while interacoes < 5:

            if resposta.lower() == "sim":

                print("\nFilmes de ação costumam ter cenas emocionantes.")

                resposta = input("Quem é o seu ator favorito? ")

            else:

                print("\nExistem muitos outros gêneros interessantes.")

                resposta = input("Você prefere comédia ou drama? ")

            interacoes += 1

        print("\nFim da conversa sobre filmes.")

    else:
        print("\nOpção inválida.")