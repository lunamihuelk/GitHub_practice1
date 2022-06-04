import sqlite3 as sql


def createDB():
	conn = sql.connect("laBase.db")
	conn.commit()
	conn.close()

def createTable(nameTabla):
	conn = sql.connect("laBase.db")
	cursor = conn.cursor()
	instruccion = f"CREATE TABLE {nameTabla}(id integer, title text, palabras text, Alter1 text, Alter2 text, Alter3 text, Alter4 text, Clave text, Descripcion text)"
	cursor.execute(instruccion)

def insertRow(session, clase, puntaje):
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"INSERT INTO streameras VALUES ('{session}', '{clase}', '{puntaje}')"
	cursor.execute(instruccion)
	conn.commit()
	conn.close()

def readRow(nameTabla): #Leer datos de la tabla
	conn = sql.connect("laBase.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM {nameTabla}"
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	return datos
	#print(datos)

def insertFilas(streamerslist):
	conn = sql.connect("streamers.db")
	cursor = conn.cursor()
	instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
	cursor.executemany(instruccion, streamerslist)
	conn.commit()
	conn.close()

def leePorOrden(field):
	conn = sql.connect("streamers.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM streamers ORDER BY {field}"
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	print(datos)

def buscar(a_buscar):
	conn = sql.connect("laBase.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM indice WHERE clase ='{a_buscar}'"
	#WHERE subs > 6000
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	return datos

def buscar_sql(a_buscar = "Palabras Similares", numbr = 3):
    conn = sql.connect("laBase.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM indice WHERE clase ='{a_buscar}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    datiyo = datos[0][numbr]
    return datiyo

def actualizar(a_buscar, dato_save):
	conn = sql.connect("laBase.db")
	cursor = conn.cursor()
	instruccion = f"UPDATE indice SET aPuntaje = {dato_save} WHERE clase = '{a_buscar}'"
	cursor.execute(instruccion)
	conn.commit()
	conn.close()

def eliminar():
	conn = sql.connect("streamers.db")
	cursor = conn.cursor()
	instruccion = f"DELETE FROM streamers WHERE name = 'elXokas'"
	#name LIKE '%John%'
	cursor.execute(instruccion)
	conn.commit()
	conn.close()

if __name__== "__main__":
	#createDB()
	#createTable("indice")
	#insertRow("PRIMERA SESSION", "CLASE 4", 20)
	#readRow("primerasesion")
	streamersli = [("elXokas", 10000, 9500),("AuronPlay", 15000, 7500),("Ibai", 65000, 6500)]
	#insertFilas(streamersli)
	#leePorOrden("subs")
	#buscar("Terminacion ING")
	actualizar("Terminacion ING", 15)
	#eliminar()