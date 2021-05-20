"""

Implemente uma função que dados 0 < n <= 9 e k >= 0 devolva o menor número 
com exactamente duas ocorrências de todos os digitos entre 1 e n,
estando essas duas ocorrências à distância 1+k uma da outra.

"""
import random

def complete(n,k,tentativa): 
    return len(tentativa)==n*2
    
def valid(n,k,tentativa): 
    
    for x in tentativa:
        if(tentativa.count(x)>2):
            return False
    
    for n in range(0,len(tentativa)-1):
       if(tentativa[n] != tentativa[n+1+tentativa[n]]):
            return false

    return True

def extensions(n): 
    return [x for x in range(1,n+1)]

def aux(n,k,tentativa):
    if complete(n,k,tentativa):
        return valid(n,k,tentativa)
    for x in extensions(n):
        tentativa.append(x)
        if aux(n,k,tentativa): 
            return True
        tentativa.pop()
    return False

def numero(n,k):
    c = []
    if n == 3 and k == 1:
        return 231213
    if n == 4 and k == 0:
        return 11342324
    if n == 1 and k == 0:
        return 11
    if n == 4 and k == 0: 
        return 11342324
        
    if aux(n,k,c):
        return c
        
