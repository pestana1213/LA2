'''

Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.

'''

def sacos(peso,compras):
    soma = 0 

    for compra in compras: 
        soma += compra 
    nrosacos = soma/peso
    sacos = round(nrosacos)
    if soma==0:
        return 0 
    if peso>soma:
        return 1
        
    if(nrosacos>sacos):
        sacos+=1
        
    return sacos
