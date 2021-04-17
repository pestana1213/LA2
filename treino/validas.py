"""

Um exemplo de um problema que pode ser resolvido de forma eficiente com
programação dinâmica consiste em determinar, dada uma sequência arbitrária de
números não negativos, se existe uma sub-sequência (não necessariamente contígua)
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""

def validas(soma,listas):
    res = []
    for lista in listas:
        if(aux(soma,lista)):
            res.append(lista)

    return res
def aux(soma,lista):
    m={}
    m[0] = lista[0]
    encontra = False
    queque = []

    for n in range(len(lista)):
        if n > 0:
            m[n] = m[n-1] + lista[n]
            queque.append(n)
            if lista[n] == soma:
                encontra = True
            if m[n] == soma:
                encontra = True
            if m[n]>soma:
                m[n]=lista[n]
                for k in range(len(lista)):
                    for valor in m.values():
                        if k not in queque:
                            if valor+lista[k] == soma:
                                encontra = True
    return encontra