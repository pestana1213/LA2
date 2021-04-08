'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menore que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.
'''




def build(artigos):
    adj = {}
    
    for livro in artigos:
        for autor in artigos[livro]:
            if autor not in adj:
                adj[autor] = set()
            adj[autor].update(set(artigos[livro]))
            adj[autor].remove(autor)
       
    return adj     

def bfs(adj,o):
    pesos = {}
    pesos[o] = 0
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                pesos[d] = pesos[v] + 1
                vis.add(d)
                queue.append(d)
    return pesos


def erdos(artigos,n):
    if (len(artigos)) == 0:
        return ["Paul Erdos"]

    adj = build(artigos)
    pesos = bfs(adj,"Paul Erdos")
    
    l = []
    for autor in pesos:
        if pesos[autor] <= n:
            l.append((autor,pesos[autor]))
    
    
 
    l.sort(key = lambda t: (t[1],t[0]))
    
    l1 = []
    for c in l:
        l1.append(c[0])
    
    return l1