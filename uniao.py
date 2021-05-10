'''

Implemente uma função que dada uma lista de conjuntos de inteiros determine qual
o menor número desses conjuntos cuja união é idêntica à união de todos os 
conjuntos recebidos.

'''
def setsun(teste):
    res=[]
    for n in teste: 
        for k in n:
            if k not in res: 
                res.append(k)
    return res
    
def complete(sets,tentativa): 
    return len(setsun(sets))==len(setsun(tentativa))
    
def extensions(sets,tentativa): 
    res = []
    ultimo = tentativa[(len(tentativa)-1)]
    for n in sets: 
        if ultimo==n: 
            res.append(sets[-1])
    return res
    
def aux(sets,tentativa): 
    if complete(sets,tentativa): 
        return True
    for x in extensions(sets,tentativa): 
        tentativa.append(x)
        if aux(sets,tentativa): 
            return True
        tentativa.pop()
    return False

def uniao(sets):
    for n in sets: 
        c = [n]
        if aux(sets,c): 
            return len(c)
