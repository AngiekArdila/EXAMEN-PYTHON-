import json

def gestor_deactores(num2):
    if num2 == 1:
        with open('peliculas_diccionario.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        nuevo_genero1 = {} 
        for pelicula, datos in peliculas_diccionario.items():
            if 'genero' in datos:
                print("Te pedirá dos géneros y dos películas para nuestra base de datos")
                nuevo_actores1 = input("Ingresa el nuevo GÉNERO por favor: ")
                nuevo_idactores = input("Ingresa el nuevo ID del nuevo género: ")
                nuevo_nombreactores = input("Ingresa el nuevo NOMBRE de la nueva película en el género: ")

                nuevo_actores1 = {
                    "id": nuevo_idactores,
                    "nombre": nuevo_nombreactores,
                }

                datos['genero'] = nuevo_genero1
                print("Sirve")

        with open('peliculas_diccionarioactores.json', 'w') as archivo:
            json.dump(peliculas_diccionario, archivo, indent=2)

    elif num2 == 2:
        with open('peliculas_diccionariogeneros.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        for pelicula, datos in peliculas_diccionario.items():
            print(f"{datos['actores']}, {datos['nombre']}")

    elif num2 == 3:
        print("Regresará al menú")
