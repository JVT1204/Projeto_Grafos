# Daniel Reis Raske 10223349
# Felipe Mazzeo Barbosa 10402808
# Fernando Pegoraro Bilia 10402097
# João Vitor Tortorello 10402674

# Arquivo de funções: contém todas as funções necessárias para o funcionamento do projeto

class TGrafoND:
    def __init__(self, n, tipo_grafo):
        self.n = n  # Número de vértices
        self.tipo_grafo = tipo_grafo  # Tipo de grafo (1 = direcionado, 2 = não direcionado)
        self.adj = [[None for _ in range(n)] for _ in range(n)]  # Matriz de adjacência
        self.num_arestas = 0  # Contador de arestas
        self.operacoes = []  # Armazena as operações feitas no grafo (somente inserção/remoção)

    def existe_vertice(self, v):
        return 0 <= v < self.n

    def insereA(self, v, w, peso):
        # Verifica se os vértices existem
        if not self.existe_vertice(v) or not self.existe_vertice(w):
            print(f"Erro: O vértice {v} ou {w} não existe.")
            return
        
        # Só insere se não houver aresta já existente e não contar a aresta duas vezes em grafos não direcionados
        if self.adj[v][w] is None:  # Aresta ainda não existe
            self.adj[v][w] = peso
            if self.tipo_grafo == 2 and self.adj[w][v] is None:  # Se for grafo não direcionado
                self.adj[w][v] = peso  # Inserir aresta na direção oposta
            self.num_arestas += 1
            self.operacoes.append(f"Aresta inserida: {v} - {w} com peso {peso}")

    def removeVertice(self, v):
        # Verifica se o vértice existe
        if not self.existe_vertice(v):
            print(f"Erro: O vértice {v} não existe.")
            return

        # Remover arestas associadas ao vértice
        for i in range(self.n):
            if self.adj[v][i] is not None:  # Se o vértice tiver arestas
                self.num_arestas -= 1  # Diminui a contagem de arestas
                self.operacoes.append(f"Aresta removida: {v} - {i}")
            self.adj[v][i] = None
            if self.tipo_grafo == 2:  # Se for grafo não direcionado, remove em ambas as direções
                self.adj[i][v] = None

        self.operacoes.append(f"Vértice removido: {v}")

    def removeAresta(self, v, w):
        # Verifica se os vértices existem
        if not self.existe_vertice(v) or not self.existe_vertice(w):
            print(f"Erro: O vértice {v} ou {w} não existe.")
            return
        
        # Verifica se a aresta existe antes de removê-la
        if self.adj[v][w] is not None:
            self.adj[v][w] = None
            if self.tipo_grafo == 2 and self.adj[w][v] is not None:  # Se for grafo não direcionado
                self.adj[w][v] = None
            self.num_arestas -= 1
            self.operacoes.append(f"Aresta removida: {v} - {w}")
            print(f"Aresta removida com sucesso.")
        else:
            print(f"Erro: A aresta entre {v} e {w} não existe.")

    def mostrarGrafo(self):
        print("Matriz de Adjacência:")
        for i in range(self.n):
            linha = [f"{peso if peso is not None else '∞'}" for peso in self.adj[i]]
            print(f"Vértice {i}: {linha}")

    def carregarDoArquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                self.tipo_grafo = int(linhas[0].strip())  # Tipo do grafo (1 = direcionado, 2 = não direcionado)
                self.n = int(linhas[1].strip())  # Número de vértices
                self.adj = [[None for _ in range(self.n)] for _ in range(self.n)]  # Reinicializar a matriz de adjacência
                num_arestas_esperadas = int(linhas[2 + self.n].strip())  # Número de arestas esperado

                # Lê a lista de vértices (pula essas linhas, pois a implementação não utiliza os nomes dos vértices diretamente)
                for i in range(2, 2 + self.n):
                    vertice_info = linhas[i].strip().split(' ', 1)  # Ignora o nome do vértice neste exemplo

                # Lê a lista de arestas e seus pesos
                arestas_lidas = 0
                for linha in linhas[2 + self.n + 1:]:
                    valores = linha.strip().split()
                    if len(valores) == 3:  # Verifica se a linha tem exatamente 3 valores (v, w, peso)
                        v, w, peso = map(float, valores)
                        self.adj[int(v)][int(w)] = peso
                        if self.tipo_grafo == 2 and self.adj[int(w)][int(v)] is None:  # Se for não direcionado
                            self.adj[int(w)][int(v)] = peso
                        arestas_lidas += 1

                # Ajuste para grafos não direcionados: contamos as arestas corretamente sem dividir
                self.num_arestas = arestas_lidas

                # Verificar se o número de arestas lidas está correto (usando o número correto para grafos não direcionados)
                if self.num_arestas != num_arestas_esperadas:
                    print(f"Alerta: Número de arestas lido ({self.num_arestas}) diferente do esperado ({num_arestas_esperadas})")
                else:
                    print(f"Arquivo carregado corretamente com {self.num_arestas} arestas.")
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

    def gravarNoArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            # Gravar o número de vértices e arestas com rótulos
            arquivo.write(f"Vértices: {self.n}\n")
            arquivo.write(f"Arestas: {self.num_arestas}\n")
            
            # Operações realizadas no grafo (feedback) - Apenas novas inserções e remoções
            if self.operacoes:
                arquivo.write("Operações realizadas:\n")
                for op in self.operacoes:
                    arquivo.write(f"{op}\n")
                arquivo.write("\n")
            
            # Mostrar o estado final do grafo, com a matriz de adjacência
            arquivo.write("\nMatriz de Adjacência (Estado Atual do Grafo):\n")
            for i in range(self.n):
                linha = [f"{peso if peso is not None else '∞'}" for peso in self.adj[i]]
                arquivo.write(f"Vértice {i}: {linha}\n")

    def categoriaConexidade(self):
        # Função auxiliar para DFS (busca em profundidade)
        def dfs(v, visitados, matriz_adj):
            visitados[v] = True
            for i in range(self.n):
                if matriz_adj[v][i] is not None and not visitados[i]:
                    dfs(i, visitados, matriz_adj)

        if self.tipo_grafo == 2:  # Se o grafo for não direcionado, verificar apenas se é conexo ou desconexo
            visitados = [False] * self.n
            dfs(0, visitados, self.adj)
            return "Conexo" if all(visitados) else "Desconexo"
        else:  # Se o grafo for direcionado, aplicar as regras C0, C1, C2, C3
            # Verificar se o grafo é fracamente conectado (ignora direção das arestas)
            def conexo():
                visitados = [False] * self.n
                dfs(0, visitados, self.adj)
                return all(visitados)

            # Verificar se o grafo é fortemente conectado (considerando a direção das arestas)
            def fortemente_conexo():
                # Passo 1: Verifica se todos os vértices são alcançáveis a partir de um vértice no grafo original
                visitados = [False] * self.n
                dfs(0, visitados, self.adj)
                if not all(visitados):
                    return False

                # Passo 2: Verifica no grafo transposto (arestas invertidas)
                transposta = [[None for _ in range(self.n)] for _ in range(self.n)]
                for i in range(self.n):
                    for j in range(self.n):
                        if self.adj[i][j] is not None:
                            transposta[j][i] = self.adj[i][j]

                # Faz DFS no grafo transposto
                visitados = [False] * self.n
                dfs(0, visitados, transposta)
                return all(visitados)

            # Se for fortemente conectado (C3)
            if fortemente_conexo():
                return "C3: Fortemente conectado"
            
            # Se for fracamente conectado (C2)
            if conexo():
                return "C2: Fracamente conectado"
            
            # Se houver componentes desconectadas, então é C0 (desconectado)
            visitados = [False] * self.n
            dfs(0, visitados, self.adj)
            if not all(visitados):
                return "C0: Desconectado"
            
            # Se não for nem fortemente nem fracamente conectado, verificar conectividade parcial (C1)
            return "C1: Parcialmente conectado"
