class TGrafoND:
    def __init__(self, n):
        self.n = n  # Número de vértices
        self.adj = [[None for _ in range(n)] for _ in range(n)]  # Matriz de adjacência
        self.num_arestas = 0  # Contador de arestas

    def insereA(self, v, w, peso):
        if self.adj[v][w] is None:  # Só insere se não houver aresta já existente
            self.adj[v][w] = peso
            self.adj[w][v] = peso  # Grafo não direcionado
            self.num_arestas += 1  # Incrementa o contador de arestas

    def removeVertice(self, v):
        for i in range(self.n):
            if self.adj[v][i] is not None:  # Se o vértice tiver arestas
                self.num_arestas -= 1  # Diminui a contagem de arestas
            self.adj[v][i] = None
            self.adj[i][v] = None

    def removeAresta(self, v, w):
        if self.adj[v][w] is not None:  # Remove somente se houver uma aresta
            self.adj[v][w] = None
            self.adj[w][v] = None
            self.num_arestas -= 1  # Diminui a contagem de arestas

    def mostrarGrafo(self):
        print("Matriz de Adjacência:")
        for i in range(self.n):
            linha = [f"{peso if peso is not None else '∞'}" for peso in self.adj[i]]
            print(f"Vértice {i}: {linha}")

    def carregarDoArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            tipo_grafo = int(linhas[0].strip())  # Tipo do grafo (não usado diretamente)
            self.n = int(linhas[1].strip())  # Número de vértices
            self.adj = [[None for _ in range(self.n)] for _ in range(self.n)]  # Reinicializar a matriz de adjacência
            self.num_arestas = int(linhas[2 + self.n].strip())  # Número de arestas esperado
            
            # Lê a lista de vértices (pula essas linhas, pois a implementação não utiliza os nomes dos vértices diretamente)
            for i in range(2, 2 + self.n):
                vertice_info = linhas[i].strip().split(' ', 1)  # Ignora o nome do vértice neste exemplo
            
            # Lê a lista de arestas e seus pesos
            arestas_lidas = 0
            for linha in linhas[2 + self.n + 1:]:
                valores = linha.strip().split()
                if len(valores) == 3:  # Verifica se a linha tem exatamente 3 valores (v, w, peso)
                    v, w, peso = map(float, valores)
                    self.insereA(int(v), int(w), peso)
                    arestas_lidas += 1
                else:
                    print(f"Linha ignorada: {linha.strip()} (não contém 3 valores)")
            
            # Verifica se o número de arestas lidas corresponde ao número esperado
            if arestas_lidas != self.num_arestas:
                print(f"Alerta: Número de arestas lido ({arestas_lidas}) diferente do esperado ({self.num_arestas})")

    def gravarNoArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"2\n{self.n}\n")  # Tipo de grafo: não direcionado com peso nas arestas
            for i in range(self.n):
                arquivo.write(f"{i}\n")
            
            # Grava o número de arestas
            arquivo.write(f"{self.num_arestas}\n")
            
            # Grava as arestas
            for i in range(self.n):
                for j in range(i + 1, self.n):
                    if self.adj[i][j] is not None:
                        arquivo.write(f"{i} {j} {self.adj[i][j]}\n")
            
            # Mostrar a tabela (matriz de adjacência) no arquivo
            arquivo.write("\nMatriz de Adjacência:\n")
            for i in range(self.n):
                linha = [f"{peso if peso is not None else '∞'}" for peso in self.adj[i]]
                arquivo.write(f"Vértice {i}: {linha}\n")

def menu():
    grafo = None
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Ler dados do arquivo grafo.txt")
        print("2. Gravar dados no arquivo de saída (e exibir grafo)")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar conteúdo do grafo")
        print("8. Sair")
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
                print(f"Grafo exibido e gravado no arquivo de saída com {grafo.num_arestas} arestas.")
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
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
