import json
def gestor_deactores(num2):
    
    if num2 == 1:
            with open('peliculas_diccionario.json', 'r') as archivo:
                peliculas_diccionario = json.load(archivo)

            for pelicula, datos in peliculas_diccionario.items():
                print("te pedira dos actores y 2 peliculas para nuestra base de datos")
                nuevo_actor1 = input("Ingresa el nuevo actor por favor: ")
                nuevo_idactor = input("Ingresa el nuevo  ID del nuevo actor: ")
                nuevo_nombreactor = input("Ingresa el nuevo NOMBRE de la nueva pelicula para el actor: ")

                nuevo_actor1 = {
                    "id": nuevo_idactor,
                    "nombre": nuevo_nombreactor,
                }

                datos['actores'] = nuevo_actor1

            with open('peliculas_diccionario.json', 'w') as archivo:
                json.dump(peliculas_diccionario, archivo, indent=2)

    elif num2 == 2:
            with open('peliculas_diccionario.json', 'r') as archivo:
                peliculas_diccionario = json.load(archivo)

            for pelicula, datos in peliculas_diccionario.items():
                print(f"{datos['actores']}, {datos['nombre']}")

    elif num2 == 3:
            print("regresara a menu")

