'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver o a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''




def build(mapa):
    adj = {}
            
    x = 0
    y = 0
    
    for linha in mapa:
        for numero in linha:
            adj[(x,y)] = ((int(mapa[y][x]),set()))
            if (x-1 >= 0 and abs(int(mapa[y][x-1]) - int(mapa[y][x])) <= 2):
                adj[(x,y)][1].add((x-1,y))
            if (x+1 < len(mapa[0]) and abs(int(mapa[y][x+1]) - int(mapa[y][x])) <=2):
                adj[(x,y)][1].add((x+1,y))
            if (y-1 >= 0 and abs(int(mapa[y-1][x]) - int(mapa[y][x])) <= 2):
                adj[(x,y)][1].add((x,y-1))
            if (y+1 < len(mapa) and abs(int(mapa[y+1][x]) - int(mapa[y][x])) <= 2):
                adj[(x,y)][1].add((x,y+1))
            x+=1
        y+=1
        x=0
    
    return adj


def dijkstra(adj,x,y):
    pai = {}
    dist = {}
    dist[(x,y)] = 0
    orla = {(x,y)}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v][1]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if (dist[v] + 1 + abs(adj[v][0] - adj[d][0])) < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + 1 + abs(adj[v][0] - adj[d][0])
    
    return dist





def travessia(mapa):
    adj = build(mapa)
    
    n = 0
    ret = 0
    min = float("inf")
    while (n < len(mapa[0])):
        dist = dijkstra(adj,n,0)
        for x in range(0,len(mapa[0])):
            if (x,len(mapa)-1) not in dist:
                continue
            else:
                new = dist[x,len(mapa)-1]
                if min > new:
                    min = new
                    ret = n
        n+=1
    
    return (ret,min)