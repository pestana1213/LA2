"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de
uma sequência de inteiros (também não vazia) com a maior soma. A função deve
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que
calcula o prefixo de uma sequência com a maior soma. Tendo essa função
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""


def maxsoma(lista):
    res = 0
    outra = lista
    k= []
    for num in lista:
        res=(aux(num,outra))
        k.append(res)
        outra = apaga(num,outra,1)
        k.append(maxsoma(outra))
    if len(k) > 0:
        return max(k)
    else:
        return 0

def aux(num, lista):
    soma = num
    q = True
    res = []
    teste = []
    for n in range(0,len(lista)):
        if n > 0:
            soma += lista[n]
            teste.append(soma)

    if len(teste)>0:
        return max(teste)
    else:
        return 0

def apaga(num,lista,k):
    lis = lista
    encontra = False
    if len(lista)>0:
        for n in lista:
            if n == num:
                del(lis[0:k])

    return lis