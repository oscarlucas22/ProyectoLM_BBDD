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
#3
def ano(db):
    sql="SELECT AnoEstreno, NombrePelicula FROM PELICULAS"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- Año Estreno:",registro["AnoEstreno"],"-- Nombre Pelicula:",registro["NombrePelicula"])
    except:
        print("Error al hacer la consulta")
def Mostrar_NombrePeliculaHoy(db,ano):
    print("-----------------------------------------------------")
    print("Nombre de la pelicula del año introducido")
    print("-----------------------------------------------------")
    sql = "SELECT NombrePelicula as 'NombrePeliculaAno' FROM PELICULAS WHERE AnoEstreno = %d" % ano
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No ninguna con ese año")
        else:
            registros = cursor.fetchall()
            for registro in registros:
                print("-- Nombre de la pelicula:",registro["NombrePeliculaAno"])
    except:
        print("Error al hacer la consulta")
#4
def Insertar_Socio(db,socio):
    cursor = db.cursor()
    sql = "INSERT INTO SOCIOS VALUES ('%s', '%s', '%s')" % (socio["DNI"],socio["Nombre"],socio["Direccion"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar.")
        db.rollback()
        print("\r")
    print("-----------------------------------------------------")
    print("Tabla SOCIOS")
    print("-----------------------------------------------------")
    sql2 = "SELECT * FROM SOCIOS"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql2)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["DNI"],"-- Nombre:",registro["Nombre"],"-- Direccion:",registro["Direccion"])
    except:
        print("Error al hacer la consulta")
        db.rollback()

def MostrarMenu():
    menu = '''
1. Lista informacion de los socios e indica el total de socios
2. Muestra el nombre de las pelicula que empiece por L
3. Muestra el nombre de las peliculas que estan presentadas en el año introducido por teclado
4. Inserta en la tabla SOCIOS un nuevo registro que introduciras por teclado
5. Elimina el socio con el DNI que introduzcas por teclado
6. Actualiza el importe a partir de un porcentaje introducido por teclado
0. Salir del programa
'''

    print(menu)
    while True:
        try:
            opcion = int(input("Opcion: "))
            return opcion
        except:
            print("Opcion incorrecta, debe ser un numero")      
