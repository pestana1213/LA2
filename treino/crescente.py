"""

Implemente uma função que dada uma sequência de inteiros, determinar o
comprimento da maior sub-sequência (não necessariamente contígua) que se
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""

def crescente(lista):
    res = 0
    m = {}
    pos = 0

    for numero in lista:
        m[numero] = conta(numero,pos,lista)
        pos += 1

    return max(m.values())

def conta(numero,pos, lista):
    res = 0

    for n in range (0,len(lista)-1):
        if n>pos:
            if lista[n] > numero:
                res += 1

    return res


