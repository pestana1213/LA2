'''

Implemente uma função que determina quantas permutações dos n primeiros digitos 
são múltiplas de um dado número d. Por exemplo se n for 3 temos as seguintes 
permutações: 123, 132, 213, 231, 312, 321. Se neste caso d for 3 então todas 
as 6 permutações são múltiplas.

'''
def complete(n,tentativa): 
    return n == len(tentativa)

def valid(n,d,tentativa): 
    stri = ""
    for k in tentativa: 
        stri.join(str(k))
    print(stri)
    return -1
 
    
def extensions(n,d,tentativa): 
    res = []
    if len(tentativa)==0: 
        for k in range(1,n+1): 
            res.append(k)
    else: 
        for k in range(1,n+1): 
            if k not in tentativa and k not in res: 
                res.append(k)
    return res
    
def valid(n, d, tentativa):
    return int("".join(map(str, tentativa))) % d == 0
        
def aux(n,d,tentativa): 
    if complete(n,tentativa): 
        return valid(n,d,tentativa)
    res = 0
    for x in extensions(n,d,tentativa): 
        tentativa.append(x)
        res += aux(n,d,tentativa)
        tentativa.pop()
    return res 
    
def multiplos(n,d):
    return aux(n,d,[])
