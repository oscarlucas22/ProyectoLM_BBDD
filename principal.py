from funciones import *

db = Conectar_BD("localhost","usuario","asdasd","proyectoLM_BD")
opcion = MostrarMenu()

while opcion != 0:
    if opcion == 1:
        Mostrar_socios(db)
