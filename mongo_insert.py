from pymongo import MongoClient
from pprint import pprint
from mongo_connect import  moonlightDB, heroes

# -----------------------------------------------------------------------------------------------------

# >>>>>>>>>>>>Criando vários documentos e inserindo eles em uma coleção (Tabela):

# variosHerois = [{ "name": "Leda", 
#                 "Classe": "mago de fogo",
#                 "força": 18, 
#                 "defesa": 13, 
#                 "arma": "cajado",
#                 "poder1": "bola de fogo",
#                 "poder2": "chuva de meteoro" },
                
#                 { "name": "Anny", 
#                 "Classe": "animal",
#                 "força": 11, 
#                 "defesa": 15, 
#                 "arma": "guarra",
#                 "poder1": "furtividade",
#                 "poder2": "guarras afiadas" },

#                 { "name": "Nick", 
#                 "Classe": "animal",
#                 "força": 15, 
#                 "defesa": 14, 
#                 "arma": "mordida",
#                 "poder1": "velocidade",
#                 "poder2": "mordida frontal" },
# ]

# inserindoTudo = heroes.insert_many(variosHerois)

# print(inserindoTudo.inserted_ids)

# ----------------------------------------------------------------------------------------------------

# >>>>>>>Criando um documento com ID. Lembre-se, dois documentos NÃO podem ter o mesmo ID.
# Paladino = { "_id": 1,
#             "name": "Jonathan",
#             "Classe": "paladino",
#             "força": 24,
#             "defesa": 19,
#             "arma": "espada longa",
#             "poder1": "ataque divino",
#             "poder2": "cura pelas mãos" }

# inserColeçao = heroes.insert_one(Paladino)
# print(inserColeçao.inserted_id)

# >>>>>>>>Posso criar documentos com mais {chave: valor} em uma mesma colection. 
# Paladino = { "_id": 2,
#             "name": "Trevor",
#             "Classe": "Knight",
#             "força": 24,
#             "defesa": 19,
#             "arma": "espada longa",
#             "poder1": "ataque divino",
#             "poder2": "cura pelas mãos",
#             "poder3": "Espada da noite" }

# inserColeçao = heroes.insert_one(Paladino)
# print(inserColeçao.inserted_id)


# ---------------------------------------------------------------------------------------------------

# >>>>>>> Função Insert 

def insert():
    try:
        employeeId = int(input('id: '))
        employeeName = input('Name: ')
        employeeClasse = input('Classe: ')
        employeeForca = int(input('Força: '))
        employeeDefesa = int(input('Defesa: '))
        employeeArma = input('Arma: ')
        
        moonlightDB.heroes.insert_one(
            {
                "_id": employeeId,
                "name":employeeName,
                "classe":employeeClasse,
                "força":employeeForca,
                "defesa":employeeDefesa,
                "arma":employeeArma,
        })
        pprint ('Dados incerido com sucesso')
    
    except Exception:
        pprint ("Erro")


insert()
