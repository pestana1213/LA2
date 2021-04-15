"""

Implemente uma função que, dada uma frase cujos espaços foram retirados,
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação),
a função recebe uma lista de palavras válidas a considerar na reconstrução
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""

def espaca(frase,palavras):
    res = ""
    teste = []
    usada = []

    for palavra in palavras:
        k =  aux(palavra,frase)
        teste.append(k)

    for possibilidade in teste:
        possibilidade = "".join(possibilidade)
        outra = apaga(possibilidade, frase)
        if len(possibilidade) == len(frase):
            res += possibilidade
        if temcontinuidade(palavras, outra) and possibilidade!="":
            if possibilidade not in usada:
                usada.append(possibilidade)
                escolhida = possibilidade
                escolhida = "".join(escolhida)
                outraa = apaga(escolhida, frase)
                res += escolhida +" "


            if len(outraa) >= 1:
                res += espaca(outra,palavras)

    return res

def aux(palavra,frase):

    tamanho = len(palavra)
    str = ""
    outra = list(frase)
    k = 0
    if len(frase) >= len(palavra):
        for n in range(0,tamanho):
            if frase[n] == palavra[n]:
                k += 1
                if k == tamanho:
                    str+=(palavra)
                    del(outra[0:k])
    outra = "".join(outra)
    return str

def apaga(palavra,frase):

    tamanho = len(palavra)
    str = ""
    res = []
    outra = list(frase)
    k = 0

    if len(frase)>=len(palavra):
        for n in range(0,tamanho):
            if frase[n] == palavra[n]:
                k += 1
                if k == tamanho:
                    str+=(palavra)
                    del(outra[0:k])
    outra = "".join(outra)
    res.append(str)
    return outra

def temcontinuidade(palavras,frase):

    ret = False
    k = ""
    r = ""

    for palavra in palavras:
        k=(aux(palavra,frase))
        if k!= "":
            r = k

    if len(r)>0:
        ret = True
    else:
        ret = False
    return ret