from pymongo import MongoClient
from pprint import pprint

# >>>>>>>>>Estabelecendo uma conexão com o banco de dados. 
#>>>Conexão
connection = MongoClient("mongodb+srv://semana:semana@cluster0-5ueib.mongodb.net/test?retryWrites=true&w=majority")


# >>>>>>>>>Criando o banco de dados "moonlightDB" e instanciando uma variavel de mesmo nome a ele.
#>>>Banco de Dados 
moonlightDB = connection["moonlightDB"]


# >>>>>>>>>Criando uma coleção (Tabela) "heroes" e instanciando uma variavel de mesmo nome a esta coleção. 
#>>>Coleção
heroes = moonlightDB["heroes"]

# --------------------------------------------------------------------------------------------------------

# OBS: No MongoDB, um banco de dados e uma coleção não é criada até obter conteúdo! 
# O MongoDB aguarda até que você tenha inserido um documento antes que ele realmente crie a coleção.

# --------------------------------------------------------------------------------------------------------

# >>>>>>>>>>>>Criando um documento (Paladino) e inserindo ele em uma coleção (heroes):

Paladino = { "name": "Jonathan", 
            "Classe": "paladino",
            "força": 21, 
            "defesa": 19, 
            "arma": "espada longa",
            "poder1": "ataque divino",
            "poder2": "cura pelas mãos" }

inserColeçao = heroes.insert_one(Paladino)
print(inserColeçao.inserted_id)