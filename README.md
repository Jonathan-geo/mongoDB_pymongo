# MONGO_DB

Esta é uma pequena documentação de utilização do mongoDB.

MongoDB é um banco de dados orientado a documentos, é de código aberto, gratuito e de alta performance. Foi escrito na linguagem de programação C++, o que o torna multiplataforma. Classificado como um programa de banco de dados NoSQL, o MongoDB usa documentos semelhantes a JSON com esquemas. É desenvolvido pela MongoDB Inc. e publicado sob uma combinação da GNU Affero General Public License e Licença Apache. Suas características permitem com que as aplicações modelem informações de modo muito mais natural, pois os dados podem ser aninhados em hierarquias complexas e continuar a ser indexáveis e fáceis de buscar.

OBS: Para esta documentação foi utilizado um cluster no mongodb cloud.

### Install

```bash

#  No terminal 

$ python -m pip install pymongo
$ python -m pip install pymongo[srv]

```
### Import

```python
from pymongo import MongoClient
from pprint import pprint
```
OBS: A biblioteca pprint foi utilizada para que o outputs fossem estilizados semelhantes formato json. 

### Connect

```python
connection = MongoClient("mongodb+srv://login:senha@cluster0-5ueib.mongodb.net/test?retryWrites=true&w=majority")
```
```python

#Estabelecendo a conexão 
connection = MongoClient("mongodb+srv://login:senha@cluster0-5ueib.mongodb.net/test?retryWrites=true&w=majority")

#Criando um DB
moonlightDB = connection["moonlightDB"]

#Criando uma colection
heroes = moonlightDB["heroes"]

#Criando um documento
Paladino = { "name": "Jonathan", 
            "Classe": "paladino",
            "força": 21, 
            "defesa": 19, 
            "arma": "espada longa",
            "poder1": "ataque divino",
            "poder2": "cura pelas mãos" }

inserColeçao = heroes.insert_one(Paladino)
print(inserColeçao.inserted_id)
```