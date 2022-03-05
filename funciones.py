import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()
#1
def Mostrar_socios(db):
    print("-----------------------------------------------------")
    print("Informacion de los socios")
    print("-----------------------------------------------------")
    sql = "SELECT * FROM SOCIOS"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["DNI"],"-- Nombre:",registro["Nombre"],"-- Direccion:",registro["Direccion"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
    print("\r")
    print("-----------------------------------------------------")
    print("Total de socios")
    print("-----------------------------------------------------")
    sql2 = "SELECT count(Nombre) as 'Total de socios' FROM SOCIOS"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql2)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- El total de socios es:",registro["Total de socios"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
#2
def nombre(db):
    sql="SELECT NombrePelicula FROM PELICULAS"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- Nombre Pelicula:",registro["NombrePelicula"])
    except:
        print("Error al hacer la consulta")
def Mostrar_NombrePelicula(db):
    print("-----------------------------------------------------")
    print("Mostrar NombrePelicula que empiece por 'L'")
    print("-----------------------------------------------------")
    sql = "SELECT NombrePelicula as 'NombrePeliculaL' FROM PELICULAS WHERE substr(NombrePelicula,1,1) = 'L'"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- Nombre de la pelicula:",registro["NombrePeliculaL"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
