"""

Neste problema pretende-se calcular a distância mais curta entre cidades
num mapa. O mapa consiste numa matriz (definida como uma lista de listas) onde
uma letra representa uma cidade e um número uma estrada de largura igual a esse
número. A função a implementar, para além do mapa, da cidade origem, e da
cidade destino, recebe também a largura do veículo em que se pretende
fazer a viagem. Assuma que as cidades dadas existem no mapa, que o mapa está
bem formado, que os carros apenas se deslocam na horizontal e na vertical, e
que numa cidade consegue circular um carro de qualquer largura.

A função deve devolver -1 se não existir caminho entre as duas cidades.
Deve devolver -2 se existir caminho, mas não usando um carro da largura dada.
Noutro caso deve devolver o tamanho do caminho mais curto entre as duas cidades.

"""

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def caminho_mais_curto(adj,o,d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return caminho


def build_aux(g_l):
    adj = {}
    for o,d in g_l:
        if o not in adj:
            adj[o] = set()
        if d not in adj:
            adj[d] = set()
        adj[o].add(d)
        adj[d].add(o)
    return adj

def build_base(mapa):
    grafo_list = []
    for y in range(len(mapa)-1):
        for x in range(len(mapa[y])-1):
            if mapa[y][x] != ' ' and mapa[y][x+1] != ' ':
                grafo_list.append(((x,y),(x+1,y)))
            if mapa[y][x] != ' ' and mapa[y+1][x] != ' ':
                grafo_list.append(((x,y),(x,y+1)))
    for x in range(len(mapa[-1])-1):
        if mapa[-1][x] != ' ' and mapa[-1][x+1] != ' ':
            grafo_list.append(((x,len(mapa)-1),(x+1,len(mapa)-1)))
    for y in range(len(mapa)-1):
        if mapa[y][-1] != ' ' and mapa[y+1][-1] != ' ':
            grafo_list.append(((len(mapa[0])-1,y),(len(mapa[0])-1,y+1)))
    return build_aux(grafo_list)
    
def comparar_largura(c1,c2,t):
    if c1.isnumeric() and int(c1) < t:
        return False
    if c2.isnumeric() and int(c2) < t:
        return False
    return True
    
def build(mapa,t):
    grafo_list = []
    for y in range(len(mapa)-1):
        for x in range(len(mapa[y])-1):
            if mapa[y][x] != ' ' and mapa[y][x+1] != ' ' and comparar_largura(mapa[y][x],mapa[y][x+1],t):
                grafo_list.append(((x,y),(x+1,y)))
            if mapa[y][x] != ' ' and mapa[y+1][x] != ' ' and comparar_largura(mapa[y][x],mapa[y+1][x],t):
                grafo_list.append(((x,y),(x,y+1)))
    for x in range(len(mapa[-1])-1):
        if mapa[-1][x] != ' ' and mapa[-1][x+1] != ' ' and comparar_largura(mapa[-1][x],mapa[-1][x+1],t):
            grafo_list.append(((x,len(mapa)-1),(x+1,len(mapa)-1)))
    for y in range(len(mapa)-1):
        if mapa[y][-1] != ' ' and mapa[y+1][-1] != ' ' and comparar_largura(mapa[y][-1],mapa[y+1][-1],t):
            grafo_list.append(((len(mapa[0])-1,y),(len(mapa[0])-1,y+1)))
    return build_aux(grafo_list)


def coords(m, o, d):
    coord_origem, coord_destino = False, False
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == o:
                coord_origem = (x,y)
            if m[y][x] == d:
                coord_destino = (x,y)
                
    return coord_origem, coord_destino

def distancia(mapa,tamanho,origem,destino):
    coord_origem, coord_destino = coords(mapa, origem, destino)
    grafo_base = build_base(mapa)
    
    c_base = caminho_mais_curto(grafo_base, coord_origem, coord_destino)
    if not(c_base) or (len(c_base) == 1 and c_base[0] != coord_origem):
       return -1
    
    grafo = build(mapa,tamanho)
    if not(grafo):
        return -2
        
    c = caminho_mais_curto(grafo, coord_origem, coord_destino)
    
    if not(c) or (len(c) == 1 and c[0] != coord_origem):
        return 0
        
    
    return len(c) - 1
