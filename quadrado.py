mport string

def complete(n,tentativa): 
    return n**2 == len(tentativa)
    
def extensions(n,tentativa): 
    res = []
    a = list(string.ascii_lowercase)
    letraspossiveis = []

    for letra in range(0,n):
        letraspossiveis.append(a[letra])
      
    if len(tentativa)==0:
        for k in range(0,n):
            for letra in letraspossiveis: 
                if letra not in res: 
                    res.append(letra)
    
    else: 
        for letra in letraspossiveis: 
            if letra!=tentativa[-1] and letra not in res: 
                res.append(letra)

    return res
    
def valida(n,tentativa): 
    
    i=0
    j=0
    for k in range(i,n-1): 
        queque = []
        primeironro = []
        for car in tentativa:
            if car in queque: 
                return False
            queque.append(car)
            if j == 0: 
                primeironro=(car)
            j+=1
            i+=1
            if j == 4:
                if car == primeironro: 
                    return False
                primeironro = car
                j=0
               
            if i == 3:
                primeirocarnro=[]
                queque=[]
                i=0
    
    return True 
        
def aux(n,tentativa): 
    if complete(n,tentativa):
        return valida(n,tentativa)
    for x in extensions(n,tentativa): 
        tentativa.append(x)
        if aux(n,tentativa):
            return True
        tentativa.pop()
    return False
    
def quadrado(n):
    c = []
    ret = ""
    teste = []
    print(extensions(n,['a']))
    if aux(n,c):
        teste = c
    k=0
    for letra in teste: 
        if k==n: 
            ret += "\n"
            k=0
        ret+=letra
        k+=1
        
    return ret 
