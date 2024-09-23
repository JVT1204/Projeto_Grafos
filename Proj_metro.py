class TGrafoND:
    def __init__(self, n):
        self.n = n  # Número de vértices
        self.adj = [[None for _ in range(n)] for _ in range(n)]  # Matriz de adjacência

    def insereA(self, v, w, peso):
        self.adj[v][w] = peso
        self.adj[w][v] = peso  # Grafo não direcionado

    def removeVertice(self, v):
        for i in range(self.n):
            self.adj[v][i] = None
            self.adj[i][v] = None

    def removeAresta(self, v, w):
        self.adj[v][w] = None
        self.adj[w][v] = None

    def mostrarGrafo(self):
        print("Matriz de Adjacência:")
        for linha in self.adj:
            print(linha)

    def carregarDoArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            tipo_grafo = int(linhas[0].strip())  # Tipo do grafo (não usado diretamente)
            self.n = int(linhas[1].strip())  # Número de vértices
            self.adj = [[None for _ in range(self.n)] for _ in range(self.n)]  # Reinicializar a matriz de adjacência
            
            # Lê a lista de vértices
            for i in range(2, 2 + self.n):
                vertice_info = linhas[i].strip().split(' ', 1)  # Ignora o nome do vértice neste exemplo
            
            # Lê a lista de arestas e seus pesos
            for linha in linhas[2 + self.n:]:
                v, w, peso = map(float, linha.strip().split())
                self.insereA(int(v), int(w), peso)

    def gravarNoArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"2\n{self.n}\n")  # Tipo de grafo: não direcionado com peso nas arestas
            for i in range(self.n):
                arquivo.write(f"{i}\n")
            for i in range(self.n):
                for j in range(i + 1, self.n):
                    if self.adj[i][j] is not None:
                        arquivo.write(f"{i} {j} {self.adj[i][j]}\n")

def menu():
    grafo = None
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Ler dados do arquivo grafo.txt")
        print("2. Gravar dados no arquivo de saída")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar conteúdo do grafo")
        print("8. Mostrar grafo (matriz de adjacência)")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo de entrada: ")
            grafo = TGrafoND(0)
            grafo.carregarDoArquivo(nome_arquivo)
            print("Grafo carregado com sucesso.")

        elif opcao == "2":
            if grafo:
                nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
                grafo.gravarNoArquivo(nome_arquivo_saida)
                print("Dados gravados com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "3":
            if grafo:
                novo_vertice = grafo.n
                grafo.n += 1
                grafo.adj.append([None] * grafo.n)
                for i in range(grafo.n):
                    grafo.adj[i].append(None)
                print(f"Vértice {novo_vertice} inserido com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "4":
            if grafo:
                v = int(input("Digite o vértice de origem: "))
                w = int(input("Digite o vértice de destino: "))
                peso = float(input("Digite o peso da aresta: "))
                grafo.insereA(v, w, peso)
                print("Aresta inserida com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "5":
            if grafo:
                v = int(input("Digite o vértice a ser removido: "))
                grafo.removeVertice(v)
                print(f"Vértice {v} removido com sucesso.")
            else:
                print("Grafo não carregado.")

        elif opcao == "6":
            if grafo:
                v = int(input("Digite o vértice de origem: "))
                w = int(input("Digite o vértice de destino: "))
                grafo.removeAresta(v, w)
                print("Aresta removida com sucesso.")
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
                grafo.mostrarGrafo()
            else:
                print("Grafo não carregado.")

        elif opcao == "9":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
