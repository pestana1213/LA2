'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''

def build(rotas):
    adj = {}
    for l in rotas:
        for x in range (1,len(l)-1,2):
            if l[x-1] not in adj:
                adj[l[x-1]] = {}
            if l[x+1] not in adj:
                adj[l[x+1]] = {}
            adj[l[x-1]][l[x+1]] = l[x]
            adj[l[x+1]][l[x-1]] = l[x]
    return adj


def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist



def viagem(rotas,o,d):
    if (o==d):
        return 0
    adj = build(rotas)
    dist = dijkstra(adj,o)
    p = dist[d]
    return p