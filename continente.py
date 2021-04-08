'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''

def build(arestas):
    adj = {}
    for lista in arestas:
        for pais in lista:
            if pais not in adj:
                adj[pais] = set()
            adj[pais].update(set(lista))
            #adj[pais] = adj[pais].union(set(lista))
            
    
    return adj
    
def bfs(adj,o,vis):
    pai = {}
    n = 1
    vis.add(o)
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                n = n + 1
                pai[d] = v
                queue.append(d)
    return n
    
def maior(vizinhos):

    vis=set()
    adj = {}
    adj = build(vizinhos)
    max = 0
    
    for pais in adj:
        if pais not in vis:
            atual = bfs (adj,pais,vis)
            if atual > max:
                max = atual
 
    return max