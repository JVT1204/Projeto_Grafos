# Daniel Reis Raske - 10223349
# Felipe Mazzeo Barbosa - 10402808
# Fernando Pegoraro Bilia - 10402097
# João Vitor Tortorello - 10402674

# Arquivo texto para ser lido: grafo_metro.txt
# Arquivo texto de saída do grafo: "nome_desejado".txt

# Arquivo main: contém menu de opções que faz a interação com o usuário

from func_grafos import TGrafoND

def menu():
    grafo = None
    while True:
        print("\n--- MetroPath - Menu de Opções ---")
        print("1. Ler dados do arquivo texto desejado")
        print("2. Gravar dados no arquivo de saída")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar conteúdo do grafo")
        print("8. Verificar grau de conexidade")
        print("9. Encontrar caminho mínimo entre estações")
        print("10. Analisar características do grafo")
        print("11. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo de entrada: ")
            grafo = TGrafoND(0, 1)
            grafo.carregarDoArquivo(nome_arquivo)

        elif opcao == "2":
            if grafo:
                nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
                grafo.gravarNoArquivo(nome_arquivo_saida)
                print(f"Grafo exibido e gravado no arquivo de saída.")
            else:
                print("Grafo não carregado.")

        elif opcao == "3":
            if grafo:
                nome_estacao = input("Digite o nome da estação para o novo vértice: ").strip()
                if nome_estacao:
                    grafo.inserir_vertice_com_nome(nome_estacao)
                else:
                    print("Nome da estação não fornecido. Vértice não inserido.")
            else:
                print("Grafo não carregado.")

        elif opcao == "4":
            if grafo:
                estacao_origem = input("Digite o nome da estação de origem: ")
                estacao_destino = input("Digite o nome da estação de destino: ")
                origem = grafo.obter_id_estacao_por_nome(estacao_origem)
                destino = grafo.obter_id_estacao_por_nome(estacao_destino)

                if origem is None or destino is None:
                    print("Erro: Uma das estações não foi encontrada.")
                else:
                    peso = float(input("Digite o peso da aresta: "))
                    grafo.insereA(origem, destino, peso)
                    grafo.operacoes.append(f"Aresta inserida: {estacao_origem} - {estacao_destino} com peso {peso}")
                    print(f"Aresta entre '{estacao_origem}' e '{estacao_destino}' inserida com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "5":
            if grafo:
                estacao = input("Digite o nome da estação a ser removida: ")
                vertice = grafo.obter_id_estacao_por_nome(estacao)

                if vertice is None:
                    print("Erro: A estação não foi encontrada.")
                else:
                    grafo.removeVertice(vertice)
                    grafo.operacoes.append(f"Vértice removido: {estacao}")
                    print(f"Estação '{estacao}' removida com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "6":
            if grafo:
                estacao_origem = input("Digite o nome da estação de origem: ")
                estacao_destino = input("Digite o nome da estação de destino: ")
                origem = grafo.obter_id_estacao_por_nome(estacao_origem)
                destino = grafo.obter_id_estacao_por_nome(estacao_destino)

                if origem is None or destino is None:
                    print("Erro: Uma das estações não foi encontrada.")
                else:
                    grafo.removeAresta(origem, destino)
                    grafo.operacoes.append(f"Aresta removida: {estacao_origem} - {estacao_destino}")
                    print(f"Aresta entre '{estacao_origem}' e '{estacao_destino}' removida com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "7":
            if grafo:
                print("Conteúdo do grafo:")
                grafo.mostrarGrafo()
            else:
                print("Grafo não carregado.")

        elif opcao == "8":
            if grafo:
                print(f"Grau de conexidade do grafo: {grafo.categoriaConexidade()}")
            else:
                print("Grafo não carregado.")

        elif opcao == "9":
            if grafo:
                print("\nLinhas e estações disponíveis:")
                for linha, estacoes in grafo.linhas.items():
                    print(f"{linha}: {', '.join(estacoes)}\n")
    
                estacao_origem = input("Digite o nome da estação de partida: ").strip().lower()
                estacao_destino = input("Digite o nome da estação de destino: ").strip().lower()

                origem = grafo.obter_id_estacao_por_nome(estacao_origem)
                destino = grafo.obter_id_estacao_por_nome(estacao_destino)

                if origem is not None and destino is not None:
                    caminho, distancia = grafo.dijkstra(origem, destino)
                    if caminho:
                        print(f"Caminho mínimo entre {grafo.estacoes[origem]} e {grafo.estacoes[destino]}: {caminho}")
                        print(f"Distância total: {distancia:.1f}")
                    else:
                        print("Não existe caminho entre as estações selecionadas.")
                else:
                    print("Estação de origem ou destino não encontrada. Tente novamente.")
            else:
                print("Grafo não carregado.")

        elif opcao == "10":
            if grafo:
                while True:
                    print("\n--- Análise de Características do Grafo ---")
                    print("1. Verificar grau dos vértices")
                    print("2. Verificar se o grafo é Euleriano")
                    print("3. Verificar se o grafo é Hamiltoniano")
                    print("4. Verificar coloração do grafo")
                    print("5. Voltar ao menu principal")
                    sub_opcao = input("Escolha uma opção: ")

                    if sub_opcao == "1":
                        graus = grafo.grau_vertices()
                        print("Grau dos vértices:")
                        for vertice, grau in graus.items():
                            nome_estacao = grafo.estacoes.get(vertice, "Desconhecido")
                            print(f"Vértice {vertice} ({nome_estacao}): grau {grau}")

                    elif sub_opcao == "2":
                        euleriano = grafo.is_euleriano()
                        print(f"O grafo é Euleriano: {'Sim' if euleriano else 'Não'}")

                    elif sub_opcao == "3":
                        hamiltoniano = grafo.is_hamiltoniano()
                        print(f"O grafo é Hamiltoniano: {'Sim' if hamiltoniano else 'Não'}")

                    elif sub_opcao == "4":
                        # Verifica se o grafo já foi colorido; se não, realiza a coloração automaticamente
                        if -1 in grafo.cores:
                            grafo.coloração_sequencial()  # Colore o grafo automaticamente sem exibir mensagens

                        # Exibe a coloração do grafo
                        coloração = grafo.exibir_cores()
                        print("Coloração do grafo (vértice: cor):")
                        for vertice, cor in coloração.items():
                            nome_estacao = grafo.estacoes.get(vertice, "Desconhecido")
                            print(f"Vértice {vertice} ({nome_estacao}): cor {cor}")

                    elif sub_opcao == "5":
                        print("Retornando ao menu principal.")
                        break

                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Grafo não carregado.")

        elif opcao == "11":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
