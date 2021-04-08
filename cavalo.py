'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''
def build (o):
    
    adj = {}
    adj[o] = set()
    
    x,y = o
    
    adj[o].add ((x+1,y+2))
    adj[o].add ((x-1,y+2))
    adj[o].add ((x+1,y-2))
    adj[o].add ((x-1,y-2))
    adj[o].add ((x+2,y+1))
    adj[o].add ((x+2,y-1))
    adj[o].add ((x-2,y+1))
    adj[o].add ((x-2,y-1))
    
    return adj


    
def saltos ( o , d):
    njog = { o:0 }
    vis = {o}
    f = 0
    r = 0
    
    
    if o == d:
        
        f = 1
    
    else:
        
        queue = [ o ]
        
        while queue and f != 1:
            
            v = queue.pop(0)
            adj = build ( v )
            
            for x in adj[v]:
                   
                   if x not in vis:
                       
                     njog[x] = njog[v] + 1
                
                     if x == d:
                    
                         f = 1
                         r = njog[x]
                
                     else:
                    
                         queue.append ( x )
                         vis.add ( x )
    
    return r