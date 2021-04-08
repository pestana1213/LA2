'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que calcula o tamanho de uma cidade, sendo
esse tamanho a distância entre os seus cruzamentos mais afastados.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''


def build (ruas):
    
    adj = {}
    for rua in ruas:
        if rua[0] not in adj:
            adj[rua[0]] = {}
        if rua[-1] not in adj:
            adj[rua[-1]] = {}
    
        adj[rua[0]][rua[-1]] = len(rua) 
        adj[rua[-1]][rua[0]] = len(rua)

    for rua in ruas:
        if (adj[rua[0]][rua[-1]] > len(rua)):
            adj[rua[0]][rua[-1]] = len(rua) 
        if (adj[rua[-1]][rua[0]] > len(rua)):
            adj[rua[-1]][rua[0]] = len(rua)    
    
    return adj




def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                   dist[o][d] = dist[o][k] + dist[k][d]
    return dist
    
    



def tamanho(ruas):
    adj = build (ruas)
    dist = fw(adj)
    max = 0
    for x in ruas:
        for y in ruas:
            if (dist[x[0]][y[0]] > max):
                max = dist[x[0]][y[0]]
    
        
    return max