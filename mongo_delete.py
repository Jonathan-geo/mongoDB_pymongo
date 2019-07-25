from pymongo import MongoClient
from pprint import pprint
from mongo_connect import  moonlightDB, heroes

# ---------------------------------------------------------------------------------------------------

# >>>>>>> Deleta o primeiro documento com o nome selecionado 
# delNome = { "name": "Jonathan" }

# heroes.delete_one(delNome)



# >>>>>>> Deletando vários documentos e retornando o número de documentos deletados. 

# delVarios = { "name": {"$regex": "^N"} }
# deletados = heroes.delete_many(delVarios)
# print(deletados.deleted_count)



# >>>>>>> Deletando todos os documentos de uma coleção:

# delTodos = heroes.delete_many({})
# print(delTodos.deleted_count)



# >>>>>>> Deletado uma coleção:
# heores.drop()




# >>>>>>> Função Delete


def delete():
    try:
        iddelete = int(input('\nId do personagem a ser deletado:\n'))
        moonlightDB.heroes.delete_one({"_id":iddelete})
        print ('\nDeletado com successo\n')
    except Exception:
        print ("Não foi possível deletar")

delete()