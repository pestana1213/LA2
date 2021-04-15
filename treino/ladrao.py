"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada,
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro.

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""

def ladrao(capacidade,objectos):
    k = []

    for nome, valor, peso in objectos:
        k.append(aux(nome,valor,peso,capacidade,objectos))


    return max(k)

def aux(nome, valor, peso, capacidade, objetos):
    x = peso
    k = valor
    passa = []
    j=0
    queque = []
    for n,v,p in objetos:
        if n != nome:
            if x + p <= capacidade and n!= nome:
                x += p
                k += v

            else:
               passa.append((n,v,p))
        j = aux(nome, valor, peso, capacidade, passa)

    if (j>k):
        return j
    else:
        return k


