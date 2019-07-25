from pymongo import MongoClient
from pprint import pprint
from mongo_connect import  moonlightDB, heroes
# ---------------------------------------------------------------------------------------------------

# >>>>>>> Alterando valores de um documento:

# valorAntigo = { "name": "Trevor" }
# novoValor = { "$set": { "name": "Belmont" } }
# heroes.update_one(valorAntigo, novoValor)


# >>>>>>> Função Update

def update():
    try:
        idAlteracao = int(input('\nId do personagem: \n'))
        novoName = input('\nNovo nome: \n')
        novaClasse = input('\nNova classe: \n')
        novaForca = input('\nNova força: \n')

        moonlightDB.heroes.update_one(
            {"_id": idAlteracao},
            { "$set": 
                {
                    "name":novoName,
                    "classe":novaClasse,
                    "força":novaForca,
                }
            }
        )
        print ("\nAlteração realizada com sucesso\n")   
    
    except Exception:
        print ("Não foi possível alterar")

update()

