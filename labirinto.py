'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruç~ões podem ser 'N','S','E','O'.

'''


def build(mapa):
    adj = {}

    x = 0
    y = 0
    
    for row in mapa:
        for column in row:
            if (column != "#"):
                adj[(x,y)] = set()
                if ((x-1 >= 0) and mapa[x-1][y] != "#"):
                    adj[(x,y)].add((x-1,y))
                if (x+1 < len(mapa[0]) and mapa[x+1][y] != "#"):
                    adj[(x,y)].add((x+1,y))
                if ((y-1 >= 0) and mapa[x][y-1] != "#"):
                    adj[(x,y)].add((x,y-1))
                if ((y+1 < len(mapa)) and mapa[x][y+1] != "#"):
                    adj[(x,y)].add((x,y+1))
            y+=1 
        x+=1
        y=0
    
    return adj


                    
def bfs(adj,x,y):
    pai = {}
    vis = {(x,y)}
    queue = [(x,y)]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def caminho(mapa):
    
    adj = build(mapa)
    pai = bfs(adj,len(mapa[0])-1,len(mapa)-1)
    output =""
    v = (0,0)
    while (v != (len(mapa[0])-1,len(mapa)-1)):
        p = pai[v]
        if (p[0] > v[0] and p[1] == v[1]):
            output = output + 'S'
        elif (p[0] < v[0] and p[1] == v[1]):
            output = output + 'N'
        elif (p[1] > v[1] and p[0] == v[0]):
            output = output + 'E'   
        elif (p[1] < v[1] and p[0] == v[0]):
            output = output + 'O'
        v = p

    

    return output