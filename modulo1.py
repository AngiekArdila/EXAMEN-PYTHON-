import json

def gestor_degeneros(num1):
    if num1 == 1:
        with open('peliculas_diccionario.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        nuevo_genero1 = {} 
        for pelicula, datos in peliculas_diccionario.items():
            if 'genero' in datos:
                print("Te pedirá dos géneros y dos películas para nuestra base de datos")
                nuevo_genero= input(str("Ingresa el nuevo GÉNERO por favor: "))
                nuevo_idgenero = input("Ingresa el nuevo ID del nuevo género: ")
                nuevo_nombregenero = input("Ingresa el nuevo NOMBRE de la nueva película en el género: ")
                
                nuevo_genero1 = {
                    "id": nuevo_idgenero,
                    "nombre": nuevo_nombregenero,
                }

                datos['genero'][nuevo_genero]=nuevo_genero1
                print("Sirve")

        with open('peliculas_diccionariogeneros.json', 'w') as archivo:
            json.dump(peliculas_diccionario, archivo, indent=2)

    elif num1 == 2:
        with open('peliculas_diccionariogeneros.json', 'r') as archivo:
            peliculas_diccionario = json.load(archivo)

        for pelicula, datos in peliculas_diccionario.items():
            print(f"{datos['genero']}, {datos['nombre']}")

    elif num1 == 3:
        print("Regresará al menú")



    