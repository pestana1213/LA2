from continente import maior
from area import area
from cidade import tamanho
from labirinto import caminho
from cavalo import saltos
from viagem import viagem
from erdos import erdos
from travessia import travessia

def main():
    
    print("<h3>saltos</h3>")
    print("in: (0,0) (1,1)")
    print("out:",saltos((0,0),(1,1)))
    
    print("<h3>maior</h3>")
    vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
    print("in:", vizinhos)
    print("out:", maior(vizinhos))

    print("<h3>area</h3>")
    mapa = ["..*..",
            ".*.*.",
            "*...*",
            ".*.*.",
            "..*.."]
    print("in:",(3,2))
    print('\n'.join(mapa))
    print("out:",area((3,2),mapa))

    print("<h3>tamanho</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:", ruas)
    print("out:", tamanho(ruas))

    print("<h3>caminho</h3>")
    mapa = ["  ########",
            "# # #    #",
            "# # #### #",
            "# #      #",
            "# # # ####",
            "# # #    #",
            "#   # #  #",
            "##### ####",
            "#        #",
            "########  "]
    print("in:")
    print('\n'.join(mapa))
    print("out:",caminho(mapa))
            
    print("<h3>viagem</h3>")
    rotas = [["Porto",20,"Lisboa"],
             ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
             ["Braga",3,"Famalicao",3,"Porto"],
             ["Viana",4,"Povoa",3,"Porto"],
             ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]
            ]
    print("in: Caminha Lisboa")
    print('\n'.join(map(str,rotas)))
    print("out:",viagem(rotas,"Caminha","Lisboa"))
    
    print("<h3>erdos</h3>")
    artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
               "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
               "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
              }
    print("in: 2")
    print('\n'.join(map(str,artigos.items())))
    print("out:",erdos(artigos,2))
    
    print("<h3>travessia</h3>")
    mapa = ["4563",
            "9254",
            "7234",
            "3231",
            "3881"]
    print("in:")
    print('\n'.join(mapa))
    print("out:",travessia(mapa))
    
if __name__ == '__main__':
    main()
