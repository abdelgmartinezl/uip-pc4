from pymongo import MongoClient
from random import randint
# import time
# from pprint import pprint

cliente = MongoClient("localhost", 27017)
db = cliente.restaurantes
# estadoServidor = db.command("serverStatus")
# pprint(estadoServidor)

# nombres = ['Cocina', 'Gran', 'Asado', 'KFC', 'Sabroso', 'Jenny', 'La Reina']
# tipos = ['Pizza', 'Chino', 'Koreano', 'Hamburguesa', 'Arepa', 'Fritura']
# ini = time.time()
# for x in range(1, 1000001):
#     negocio = {
#         'nombre' : nombres[randint(0, (len(nombres)-1))] + " " + nombres[randint(0, (len(nombres)-1))] + " " + tipos[randint(0, (len(tipos)-1))],
#         'valor' : randint(1,5),
#         'cocina' : tipos[randint(0, (len(tipos)-1))]
#     }
#     resultado = db.restaurante.insert_one(negocio)
# fin = time.time()
# print('Terminado ' + str(ini) + " - " + str(fin))

rankiao = db.restaurante.find({'valor': 5})
# for r in rankiao:
#     print(r)

print("\nLa sumatoria de cada ocurrencia de cada valor")
grupovalor = db.restaurante.aggregate(
    [
        {'$group':
            { '_id': "$valor",
                "count":
                    {'$sum': 1}
            }
        },
        {
            "$sort": { "_id": 1}        
        }
    ]
)
for grupo in grupovalor:
    print(grupo)