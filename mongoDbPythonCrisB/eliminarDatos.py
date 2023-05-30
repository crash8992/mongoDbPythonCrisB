from dataBasenoSQl import client

db = client.ejemploBase02
coleccion = db.jugadores

print("mostrar todos los documentos de la base")
datos1 = coleccion.find()
for registro in datos1:
    print(registro)
    
print("proceso para eliminar datos")
coleccion.delete_many({'minutos_jugados': 256 })

