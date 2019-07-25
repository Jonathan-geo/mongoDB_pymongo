from pymongo import MongoClient
from pprint import pprint
from mongo_connect import  moonlightDB, heroes
# ---------------------------------------------------------------------------------------------------------


# >>>>>>Listando e buscando banco de dados em minha conta mongoDB. 
# >>>>>>Lembrando que minha conexão está com o nome de "coonection"

# pprint (connection.list_database_names())

# dblist = connection.list_database_names()
# if "moonlightDB" in dblist:
#   print("O banco de dados existe.")
# else:
#     print ("O banco de dados não existe.")


# ---------------------------------------------------------------------------------------------------

# >>>>>>>Listando e buscando coleções (Tabelas) no meu banco de dados "moonlight"

# pprint (moonlightDB.list_collection_names())

# collist = moonlightDB.list_collection_names()
# if "heroes" in collist:
#   print("A coleção existe.")


# ----------------------------------------------------------------------------------------------------



# >>>>>> Contando o número de documentos dentro da minha colection
# pprint(heroes.count_documents({}))



# >>>>>> Selecionando o primeiro documento da coleção (heroes):
# pprint(heroes.find_one())



# >>>>>> Selecionando um documento por {chave: Valor}:
# pprint(heroes.find_one({"arma": "mordida"}))



# >>>>>> Selecionando todos os documentos da minha coleção:
# for personagens in heroes.find():
#     pprint(personagens)



# >>>>>> Selecionando todos os documentos da minha coleção (Número limitado)
# selLimite = heroes.find().limit(5)

# for x in selLimite:
#   pprint(x)


# >>>>>> Selecionando todos os documentos que possuem uma mesma {chave:valor} selecionada:
# for animais in heroes.find({"classe": "animal"}):
#     pprint(animais)





# >>>>>> Selecionando o nome e a arma de todos os documentos. 
# >>>>>> Só posso atribuir falso (0) para o id, pois ele é o unico que aparece mesmo quando não mensionado. 
 
# for nomes in heroes.find({},{ "_id": 0, "name": 1, "arma": 1 }):
#   pprint(nomes)


# >>>>>> Neste caso o ID, aparecerá também. 
# for armas in heroes.find({},{ "name": 1, "arma": 1 }):
#   pprint(armas)

# >>>>> Neste caso o id não aparecerá.
# for classes in heroes.find({},{ "_id": 0, "classe": 1, "name": 1, "arma": 1 }):
#   pprint(classes)



# >>>>> Instanciando uma busca. 
# cajado = { "arma": "cajado" }
# busca = heroes.find(cajado)

# for x in busca:
#   pprint(x)





# >>>>>> Buscar os documento em que o valor da chave nome comessem com a 
# >>>>>> letra T ou posterior no alfabeto. (T, U, V, ...). Lembrando que os nomes estão em maiúscula.
# >>>>>> A mesma busca pode ser feita por regex: letraJ = { "name": { "$regex": "^S" } }

# letraJ = { "name": { "$gt": "T" } }
# busca = heroes.find(letraJ)

# for x in busca:
#   pprint(x)



# >>>>>> Selecionando os documentos por ordem alfabética (nome):
# nomePorOredem = heroes.find().sort("name")

# for x in nomePorOredem:
#   pprint(x)


# >>>>>> Selecionando por ordem decrescente. Para o caso de ordem crescente substituir o -1 por 1.
# ordemDecrescente = heroes.find().sort("name", -1)

# for x in ordemDecrescente:
#   pprint(x)



# >>>>>>> Função Read

def read():
    try:
        todosPerson = moonlightDB.heroes.find()
        print ('\n Todos os personagens da minha coleção \n')
        for per in todosPerson:
            pprint (per)

    except Exception:
        pprint ("Não foi possível carregar")


read()