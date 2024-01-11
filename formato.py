import json

def gestor_degeneros(num3):
    if num3 == 1:
        with open('peliculas_diccionario.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        nuevo_genero1 = {} 
        for pelicula, datos in peliculas_diccionario.items():
            if 'genero' in datos:
                print("Te pedirá dos géneros y dos películas para nuestra base de datos")
                nuevo_formato = input("Ingresa el nuevo GÉNERO por favor: ")
                nuevo_idformato = input("Ingresa el nuevo ID del nuevo género: ")
                nuevo_nombreformato = input("Ingresa el nuevo NOMBRE de la nueva película en el género: ")

                nuevo_formato = {
                    "id": nuevo_idformato,
                    "nombre": nuevo_nombreformato,
                }

                datos['formato'] = nuevo_genero1
                print("Sirve")

        with open('peliculas_diccionariogeneros.json', 'w') as archivo:
            json.dump(peliculas_diccionario, archivo, indent=2)

    elif num3 == 2:
        with open('peliculas_diccionariogeneros.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        for pelicula, datos in peliculas_diccionario.items():
            print(f"{datos['formato']}, {datos['nombre']}")

    elif num3 == 3:
        ("regresara a menu")