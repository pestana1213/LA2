'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.

O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.

O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.

O robot só consegue movimentar-se na horizontal ou na vertical. 

mapa =     ["..*..",
            ".*.*.",
            "*...*",
            ".*.*.",
            "..*.."]

'''


def build(mapa):
    adj = {}

    for x in range (0,len(mapa[0])):
        for y in range (0,len(mapa)):
            adj[(x,y)] = set()
            
    x = 0
    y = 0
    
    for linha in mapa:
        for pixel in linha:
            if (pixel != "*"):
                if ((((x-1),(y)) in adj) and mapa[y][x-1] != "*"):
                    adj[(x,y)].add((x-1,y))
                if ((((x+1),(y)) in adj) and mapa[y][x+1] != "*"):
                    adj[(x,y)].add((x+1,y))
                if ((((x),(y-1)) in adj) and mapa[y-1][x] != "*"):
                    adj[(x,y)].add((x,y-1))
                if ((((x),(y+1)) in adj) and mapa[y+1][x] != "*"):
                    adj[(x,y)].add((x,y+1))
            x+=1 
        y+=1
        x=0
    
    return adj
    


                    
                    
def bfs(adj,x,y,vis):
    
    pai = {}
    n = 1
    vis.add((x,y))
    queue = [(x,y)]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                n = n + 1
                pai[d] = v
                queue.append(d)
    return n
    
def area(p,mapa):
    x,y = p
    vis = set()
    adj = build(mapa)
    n = bfs(adj,x,y,vis)
    return n
    