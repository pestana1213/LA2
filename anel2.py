'''

Um anel de tamanho n (um número par) consiste numa permutação do números de 1 
até n em que a soma de quaisquer dois números adjacentes é um número primo
(considera-se que o primeiro elemento da sequência é adjacente do último).
Implemente uma função que calcule um destes aneis de tamanho n.

'''
def complete(n, tentativa):
    return len(tentativa) == n
    
def extensions(n,tentativa):
    res = []
    elementoanterior = tentativa[-1]
    primeiroelemento = tentativa[0]
    
    if len(tentativa) == n-1: 
        for x in range(1,n+1):
            if isPrime(elementoanterior + x)and isPrime(primeiroelemento + x) and x not in tentativa:
                res.append(x)
    else: 
        for x in range(1,n+1): 
            if isPrime(elementoanterior + x) and x not in tentativa: 
                res.append(x)
    return res

def aux(n,tentativa): 
    if complete(n,tentativa):
        return True
    for x in extensions(n,tentativa): 
        tentativa.append(x)
        if aux(n,tentativa):
            return True 
        tentativa.pop()
    return False

def anel(n):
    for x in range(1,n+1):
        c = [x]
        if aux(n,c):
            return c
            
def isPrime(x):
    for p in range(2,x):
        if x % p == 0:
            return False
    return True
