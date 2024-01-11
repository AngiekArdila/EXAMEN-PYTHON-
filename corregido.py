import json
num2=input("escribe numero")
def gestor_deactores(num2):
    if num2 == 1:
        with open('peliculas_diccionario.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        for pelicula, datos in peliculas_diccionario.items():
            print("Te pedirá dos actores y dos películas para nuestra base de datos")
            nuevo_actor1 = input("Ingresa el nuevo actor por favor: ")
            nuevo_idactor = input("Ingresa el nuevo ID del nuevo actor: ")
            nuevo_nombreactor = input("Ingresa el nuevo NOMBRE de la nueva película para el actor: ")

            nuevo_actor1 = {
                "id": nuevo_idactor,
                "nombre": nuevo_nombreactor,
            }

            datos['actores'].append(nuevo_actor1)
            print("Paso")

        with open('peliculas_diccionarioactores.json', 'w') as archivo:
            json.dump(peliculas_diccionario, archivo, indent=2)

    elif num2 == 2:
        with open('peliculas_diccionarioactores.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        for pelicula, datos in peliculas_diccionario.items():
            # Assuming 'actores' is a list in your data structure
            for actor in datos['actores']:
                print(f"{actor['nombre']}, {datos['nombre']} del actor")
                print(actor)

    elif num2 == 3:
        print("Regresará al menú")
