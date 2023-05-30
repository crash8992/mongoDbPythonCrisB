from dataBasenoSQl import client

db = client.ejemploBase02
coleccion = db.jugadores

nombre = input("inserte el nombre: ")
equipo_actual =input("inserte el equipo que juega: ")
minutos_jugados =int(input("inserte el # de minutos jugados: "))

datos1 = {"nombres": nombre, "equipo_actual": equipo_actual, "minutos_jugados": minutos_jugados}

coleccion.insert_one(datos1)