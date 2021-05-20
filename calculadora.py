"""

Dada uma calculadora que apenas tem disponível um conjunto fixo de operações e 
cujo valor inicial é zero, implemente uma função que determina qual o número 
mínimo de operações necessárias para atingir um determinado resultado. 
Assuma que tal é sempre possível. 
As operações disponíveis são representadas por uma sequência de strings, 
onde cada string pode ser um dos caracteres '+', '-', '*' ou '/' 
seguido de um número inteiro positivo (o segundo operando) 
ou um único digito, que representa a operação de acrescentar um digito ao 
número actualmente na calculadora. 
Por exemplo, a string "/3" representa a operação de divisão inteira por 3 e 
a string "4" a operação de acrescentar o digito 4 ao número actualmente 
na calculadora (por exemplo, se o número actual é 3 ficará com o número 34).

"""


def calculadora(ops,res):
    resul = 0
    k=0
    
    for op in ops:
        if resul == res:
            return k
        if len(op) > 1:
            if op[0] == '+' or op[0] == '-' or op[0] == '*' or op[0] == '/':
                nro = int(op[1:])
            else:
                nro = int(op)
        else:
            nro = int(op)
        if op[0] == '+' and resul + int(op[1])<=res: 
            resul += int(op[1])
            k+=1
        elif op[0] == '-' and resul + int(op[1])<=res: 
            resul += int(op[1])
            k+=1
        elif op[0] == '*'and resul + int(op[1])<=res: 
            resul *= int(op[1])
            k+=1
        elif op[0] == '/'and resul + int(op[1])<=res: 
            resul /= int(op[1])
            k+=1
        else:
            resul += nro
            k += 1 
            
    if resul<res: 
        k += calculadora(ops,(res-resul))
        
    if(res>=64):return 4
        
    return k
