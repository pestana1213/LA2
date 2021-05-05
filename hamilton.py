def completo(arestas, c): 
    a=[]
    for (valor,b) in arestas: 
        if valor not in a: 
            a.append(valor)
        if b not in a: 
            a.append(b)
            
    return len(c)==len(a)

def extensions(arestas,c): 
    ret = []
    if len(c)==0: 
        for (a,b) in arestas: 
            if a not in ret: 
                ret.append(a)
            if b not in ret: 
                ret.append(b)
    else:
        for (a,b) in arestas: 
            if a == c[(len(c)-1)] and b not in ret and b not in c: 
                ret.append(b)
            if b == c[(len(c)-1)] and a not in ret and a not in c: 
                ret.append(a)
    return ret

def valida(arestas,c): 
    if len(c)==0:    
        return False 
        
    ultimo = c[(len(c)-1)]
    
    for (a,b) in arestas: 
        if a not in c: 
            return False
        if b not in c: 
            return False
    
    for (a,b) in arestas:             
        if ultimo == a and c[0]==b:
            return True
        elif ultimo == b and c[0]==a:
            return True


    return False 
    
def aux(arestas,c):
    if completo(arestas,c):
        return valida(arestas,c)
    for x in extensions(arestas,c): 
        c.append(x)
        print(c)
        if aux(arestas,c):
            return True
        c.pop()
    return False

def hamilton(arestas):
    c=[]
    print(extensions(arestas,[1]))
    if aux(arestas,c):
        return c
