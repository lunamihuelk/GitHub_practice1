import sqlite3 as sql

def eliminar_desql(idd):
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"DELETE FROM cuentas WHERE id = '{idd}'"
	#name LIKE '%John%'
	cursor.execute(instruccion)
	conn.commit()
	conn.close()

def readRow(nameTabla): #Leer datos de la tabla
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM {nameTabla}"
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	#print(type(datos))
	return datos

def leerID(nameTabla): #Leer datos de la tabla
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM {nameTabla}"
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	lista = []
	for dato in datos:
		lista.append(dato[0])
	#print(type(datos))
	valor_m=0
	for num in lista:
		if int(num) > valor_m:
			valor_m= num
		else:
			pass
	return valor_m

def leePorOrden(field):
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM cuentas ORDER BY {field}"
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	#print(type(datos))

def buscar(a_buscar):
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"SELECT * FROM cuentas WHERE id ='{a_buscar}'"
	#WHERE subs > 6000
	cursor.execute(instruccion)
	datos = cursor.fetchall()
	conn.commit()
	conn.close()
	return datos

def actualizar(tilte_db, dato_save, a_buscar):
    conn = sql.connect("stream.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE cuentas SET '{tilte_db}' = '{dato_save}' WHERE id = '{a_buscar}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertRow(id, nombres, usuario, contraseña, empresa, frasescret, descripcion):
	conn = sql.connect("stream.db")
	cursor = conn.cursor()
	instruccion = f"INSERT INTO cuentas VALUES ('{id}', '{nombres}', '{usuario}', '{contraseña}', '{empresa}', '{frasescret}', '{descripcion}')"
	cursor.execute(instruccion)
	conn.commit()
	conn.close()

class buscador:
	def __init__(self):
		pass

	def buscar_empresa(self, empresa):
		basic= readRow("cuentas")
		para_imprimir =[]
		for fila in basic:
			if empresa == fila[4]:
				para_imprimir.append(f'{fila[0]} >> {fila[1]}\n')
			else:
				pass
		resultante = "".join(para_imprimir)
		return resultante

	def buscar_por_id(self, id):
		dato_obtenido=buscar(id)
		cara =dato_obtenido[0]
		delvol =[cara[2],cara[3]]
		return delvol

	def buscar_por_select(self, id):
		dato_obtenido=buscar(id)
		cara =dato_obtenido[0]
		return cara

def main():
	preguntica = buscador()
	preguntica.buscar_empresa("facebook")
	preguntica.buscar_por_id(4)

if __name__ == "__main__":
	main()