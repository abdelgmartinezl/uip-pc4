import sqlite3

conn = sqlite3.connect('basedato.db')
print("Conexion abierta exitosamente")
conn.execute('CREATE TABLE estudiantes(nombre TEXT, direccion TEXT, ciudad TEXT, pin TEXT)')
print("Tabla creada exitosamente")
conn.close()