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
                novo_vertice = grafo.n
                grafo.n += 1
                grafo.adj.append([None] * grafo.n)
                for i in range(grafo.n):
                    grafo.adj[i].append(None)
                grafo.operacoes.append(f"Vértice inserido: {novo_vertice}")
                print(f"Vértice {novo_vertice} inserido com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "4":
            if grafo:
                v = int(input("Digite o vértice de origem: "))
                w = int(input("Digite o vértice de destino: "))
                if not grafo.existe_vertice(v) or not grafo.existe_vertice(w):
                    print(f"Erro: O vértice {v} ou {w} não existe.")
                else:
                    peso = float(input("Digite o peso da aresta: "))
                    grafo.insereA(v, w, peso)
                    print("Aresta inserida com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "5":
            if grafo:
                v = int(input("Digite o vértice a ser removido: "))
                if not grafo.existe_vertice(v):
                    print(f"Erro: O vértice {v} não existe.")
                else:
                    grafo.removeVertice(v)
                    print(f"Vértice {v} removido com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "6":
            if grafo:
                v = int(input("Digite o vértice de origem: "))
                w = int(input("Digite o vértice de destino: "))
                grafo.removeAresta(v, w)
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
                inicio = int(input("Digite o ID da estação de partida: "))
                fim = int(input("Digite o ID da estação de destino: "))
                caminho, distancia = grafo.dijkstra(inicio, fim)
                if caminho:
                    print(f"Caminho mínimo entre {inicio} e {fim}: {caminho}")
                    print(f"Distância total: {distancia}")
                else:
                    print("Não existe caminho entre as estações selecionadas.")
            else:
                print("Grafo não carregado.")

        elif opcao == "10":
            if grafo:
                # Realiza as análises e exibe os resultados
                analise = grafo.analisar_caracteristicas()
                print("Características do grafo:")
                print(f"Grau dos vértices: {analise['grau_vertices']}")
                print(f"É Euleriano: {'Sim' if analise['euleriano'] else 'Não'}")
                print(f"É Hamiltoniano: {'Sim' if analise['hamiltoniano'] else 'Não'}")
                print(f"Coloração do grafo (vértice: cor): {analise['coloracao']}")
            else:
                print("Grafo não carregado.")

        elif opcao == "11":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
