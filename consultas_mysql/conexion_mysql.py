import mysql.connector


def obtener_conexion_db():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "juanolijaz",
        database = "laura"
    )
# conn = obtener_conexion_db()
# cursor = conn.cursor()

# if cursor:
#     print("conexion exitosa")

# conn.close()







