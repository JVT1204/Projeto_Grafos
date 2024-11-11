# Daniel Reis Raske - 10223349
# Felipe Mazzeo Barbosa - 10402808
# Fernando Pegoraro Bilia - 10402097
# João Vitor Tortorello - 10402674

# Arquivo de funções: contém todas as funções necessárias para o funcionamento do projeto

from mapeamento_linhas import LINHAS_METRO_CPTM
import sys

    # Função para remover acentos sem importar biblioteca
def remover_acentos(texto):
    acentos = {
        'á': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o', 'õ': 'o',
        'ú': 'u',
        'ç': 'c', 'Ç': 'C',
        'Á': 'A', 'Ã': 'A', 'Â': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O', 'Õ': 'O',
        'Ú': 'U'
    }
    return ''.join(acentos.get(char, char) for char in texto)

class TGrafoND:
    def __init__(self, n, tipo_grafo):
        self.n = n  # Número de vértices
        self.tipo_grafo = tipo_grafo  # Tipo de grafo (1 = direcionado, 2 = não direcionado)
        self.adj = [[None for _ in range(n)] for _ in range(n)]  # Matriz de adjacência
        self.num_arestas = 0  # Contador de arestas
        self.operacoes = []  # Armazena as operações feitas no grafo (somente inserção/remoção)
        self.cores = [-1] * n  # Inicializa cores dos vértices como não coloridos (-1)
        self.estacoes = {}  # Dicionário para mapear ID da estação para o nome
        self.linhas = {linha: estacoes[:] for linha, estacoes in LINHAS_METRO_CPTM.items()}

    def existe_vertice(self, v):
        return 0 <= v < self.n

    def obter_id_estacao_por_nome(self, nome_estacao):
        # Primeira tentativa: busca pelo nome exatamente como digitado
        nome_estacao = nome_estacao.strip().lower()
        for id_estacao, nome_original in self.estacoes.items():
            if nome_estacao.lower() == nome_original.lower():
                return id_estacao

        # Segunda tentativa: busca sem considerar acentuação
        nome_normalizado = remover_acentos(nome_estacao).lower()
        for id_estacao, nome_original in self.estacoes.items():
            if remover_acentos(nome_original).lower() == nome_normalizado:
                return id_estacao
                
        print(f"Erro: Estação '{nome_estacao}' não encontrada. Verifique o nome e tente novamente.")
        return None

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

    def inserir_vertice_com_nome(self, nome_estacao):
        novo_vertice = self.n
        self.n += 1
        self.adj.append([None] * self.n)
        for i in range(self.n):
            self.adj[i].append(None)
        self.estacoes[novo_vertice] = nome_estacao
        self.operacoes.append(f"Vértice inserido: {novo_vertice} ({nome_estacao})")
        print(f"Vértice {novo_vertice} com nome '{nome_estacao}' inserido com sucesso.")


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
                self.cores = [-1] * self.n  # Reinicializar a lista de cores para o número correto de vértices
                self.estacoes = {}  # Reinicializar o dicionário de estações
                num_arestas_esperadas = int(linhas[2 + self.n].strip())  # Número de arestas esperado

                # Lê a lista de vértices (pula essas linhas, pois a implementação não utiliza os nomes dos vértices diretamente)
                for i in range(2, 2 + self.n):
                    dados_vertice = linhas[i].strip().split(' ', 1)
                    id_vertice = int(dados_vertice[0])
                    nome_estacao = dados_vertice[1].strip('"')
                    self.estacoes[id_vertice] = nome_estacao

                    # Associa a estação a todas as linhas em que ela aparece
                    for linha, estacoes in LINHAS_METRO_CPTM.items():
                        if nome_estacao in estacoes and nome_estacao not in self.linhas[linha]:
                            self.linhas[linha].append(nome_estacao)
                
                # Lê a lista de arestas e seus pesos
                arestas_lidas = 0
                for linha in linhas[2 + self.n + 1:]:
                    valores = linha.strip().split()
                    if len(valores) == 3:  # Verifica se a linha tem exatamente 3 valores (v, w, peso)
                        v, w, peso = map(float, valores)
                        self.insereA(int(v), int(w), peso)  # Utiliza o método insereA para inserir a aresta
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
        finally:
            # Limpa as operações registradas durante o carregamento
            self.operacoes.clear()

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

            # Exibir os nomes das estações atualizados
            arquivo.write("\nNomes das Estações (Atualizados):\n")
            for id_vertice, nome in self.estacoes.items():
                arquivo.write(f"{id_vertice}: {nome}\n")

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

    # Implementação do Algoritmo de Dijkstra para encontrar o caminho mais curto
    def dijkstra(self, origem, destino):

        dist = [sys.maxsize] * self.n  # Inicializa distâncias como infinito
        dist[origem] = 0
        visitados = [False] * self.n
        antecessor = [None] * self.n

        for _ in range(self.n):
            u = self.min_dist(dist, visitados)
            visitados[u] = True

            for v in range(self.n):
                if self.adj[u][v] is not None and not visitados[v] and dist[u] + self.adj[u][v] < dist[v]:
                    dist[v] = dist[u] + self.adj[u][v]
                    antecessor[v] = u

        caminho = []
        atual = destino
        while atual is not None:
            caminho.insert(0, self.estacoes[atual])  # Converte ID para o nome da estação
            atual = antecessor[atual]

        return caminho if caminho[0] == self.estacoes[origem] else None, dist[destino]

    def min_dist(self, dist, visitados):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.n):
            if dist[v] < min_val and not visitados[v]:
                min_val = dist[v]
                min_index = v

        return min_index

    def grau_vertices(self):
        graus = {v: 0 for v in range(self.n)}
        for v in range(self.n):
            for w in range(self.n):
                if self.adj[v][w] is not None:
                    graus[v] += 1
        return graus

    def is_euleriano(self):
        graus = self.grau_vertices()
        return all(grau % 2 == 0 for grau in graus.values())

    def is_hamiltoniano(self):
        graus = self.grau_vertices()
        return all(grau >= self.n / 2 for grau in graus.values())

    def coloração_sequencial(self):
        # Reinicializa as cores antes de colorir
        self.cores = [-1] * self.n
        self.cores[0] = 0
        cor_disponivel = [False] * self.n

        for u in range(1, self.n):
            # Marca cores dos vizinhos como indisponíveis
            for i in range(self.n):
                if self.adj[u][i] is not None and self.cores[i] != -1:
                    cor_disponivel[self.cores[i]] = True

            # Encontra a primeira cor disponível
            cor = 0
            while cor < self.n and cor_disponivel[cor]:
                cor += 1

            # Atribui a menor cor disponível ao vértice u
            self.cores[u] = cor

            # Reseta as cores para o próximo vértice
            cor_disponivel = [False] * self.n

    def exibir_cores(self):
        # Verifica se a coloração foi realizada
        if -1 in self.cores:
            print("O grafo ainda não foi colorido.")
        else:
            return {vertice: self.cores[vertice] for vertice in range(self.n)}

    def analisar_caracteristicas(self):
        # Garante que o grafo está colorido antes de retornar as características
        if -1 in self.cores:
            self.coloração_sequencial()
        return {
            "grau_vertices": self.grau_vertices(),
            "euleriano": self.is_euleriano(),
            "hamiltoniano": self.is_hamiltoniano(),
            "coloracao": self.exibir_cores()  # A coloração já estará garantida aqui
        }