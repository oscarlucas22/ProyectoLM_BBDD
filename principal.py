from funciones import *

db = Conectar_BD("localhost","usuario","asdasd","proyectoLM_BD")
opcion = MostrarMenu()

while opcion != 0:
    if opcion == 1:
        Mostrar_socios(db)
    
    elif opcion == 2:
        print("-----------------------------------------------------")
        print("Los nombres de las peliculas de la tabla PELICULAS")
        print("-----------------------------------------------------")
        nombre(db)
        print()
        Mostrar_NombrePelicula(db)
