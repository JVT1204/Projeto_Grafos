# Projeto_Grafos

## Integrantes

- Fernando Pegoraro Bilia - 10402097
- Daniel Reis Raske - 10223349
- Felipe Mazzeo Barbosa - 10402808
- João Vitor Tortorello - 10402674

## Descrição projeto

Projeto para a matéria Teoria dos Grafos na Universidade Presbiteriana Mackenzie que tem como objetivo modelar a rede metroviária e de trens metropolitanos de São Paulo como um grafo para analisar e propor otimizações que possam melhorar a eficiência do sistema de transporte público da cidade.

Serão considerados tanto as linhas de metrô quanto as da CPTM, tendo uma versão simulada demonstrando
as estações e suas respectivas ligações

## Objetivo:

Para esse projeto consideramos o problema real da eficiência do caminho pelos trilhos de São Paulo, como sobrecarga em determinados trechos da rede e facilitar a logística de trajeto.

Nosso objetivo é criar um sistema eficiente de caminho mínimo para a rede de transporte de São Paulo, o que pode facilitar a vida de muitos paulistanos.

Como requisito do projeto, foi pedido pelo professor da disciplina de Teoria de Grafos que destaque um dos Objetivos do Desenvolvimento Sustentável (ODS - https://odsbrasil.gov.br/), e o escolhido foi o de número 9 (Indústria, inovação e infraestrutura), já que escolhemos resolver um problema de infraestrutra da cidade que é o transporte público, visando melhorar o cotidiano e impulsionar maior bem-estar de seus residentes.

## Definições:

#### Arquivo texto (`grafo_metro`) criado com a finalidade de simular em forma de grafo o sistema metroviário de São Paulo
#### Estrutura do arquivo:
### 1. Tipo do Grafo - Primeira linha

0 – grafo não orientado sem peso;

1 – grafo não orientado com peso no vértice;

2 – grafo não orientado com peso na aresta;

3 – grafo não orientado com peso nos vértices e arestas;

4 – grafo orientado sem peso;

5 – grafo orientado com peso no vértice;

6 – grafo orientado com peso na aresta;

7 – grafo orientado com peso nos vértices e arestas.

### 2. Número de vértices
### 3. Lista de vértices (próximas n linhas) - `[número_do_vértice] [nome_da_estação]`
- Vértices (Nodos): Cada estação de metrô ou trem será representada como um vértice no grafo.
### 4. Número de arestas
### 5. Lista de arestas (próximas n linhas) - `[vértice_origem] [vértice_destino] [peso]`
- Arestas: As arestas representarão as conexões diretas entre as estações, com pesos correspondentes à distância física (em quilomêtros) entre as estações.

## Link graph online:

http://graphonline.ru/pt/?graph=vMuiCbBCWBToRENZ

## Imagem grafo (Rede Metroviária de São Paulo)

![alt](/assets/Imagem_grafo.png)