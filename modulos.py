def display_menu(lista_opciones, titulo_menu="MENU", caracter_opciones="numerico"):
    print(f"\n{titulo_menu}")
    print("-" * len(titulo_menu))
    
    if not lista_opciones:
        print("No hay opciones disponibles.")
        return
    
    for i, opcion in enumerate(lista_opciones):
        if caracter_opciones == "numerico":
            print(f"{i + 1}. {opcion}")
        elif caracter_opciones == "alfabetico":
            letra = chr(65 + i) 
            print(f"{letra}. {opcion}")
        else:
            print("Tipo de opción no válido. Use 'numerico' o 'alfabetico'.")
            return


def read_int(prompt = "introduzca un numero", qty_attempts = None, only_positives = False):

    attempts = 0 

    if qty_attempts is not None:
        if qty_attempts <= 0 or not isinstance(qty_attempts, int):
            raise ValueError ("el valor dado a la cantidad de intentos debe ser un numero entero POSITIVO")
    
    while qty_attempts is None or attempts < qty_attempts:
        try:
            user_input = input(prompt)
            value = int(user_input)

            if only_positives and value <0:
                print("El numero no puede ser negativo")
            else:
                return value
        except ValueError:
            print("entrada invalida, introducir un numero entero")

        attempts += 1 
    
    print("se alcanzo el maxio de intentos. cerrando programa")
    exit()

def read_floating_point(prompt = "introduzca un numero", qty_attempts = None, only_positives = False):
    attempts = 0 
    if qty_attempts is not None:
        if qty_attempts <= 0 or not isinstance(qty_attempts, int):
            raise ValueError ("el valor dado a la cantidad de intentos debe ser un numero entero POSITIVO")
    
    while qty_attempts is None or attempts < qty_attempts:
        try:
            user_input = input(prompt)
            value = float(user_input)

            if only_positives and value <0:
                print("El numero no puede ser negativo")
            else:
                return value
        except ValueError:
            print("entrada invalida, introducir un numero entero")

        attempts += 1 
    
    print("se alcanzo el maxio de intentos. cerrando programa")
    exit()

def get_file(end_program = True):

    while True:
        try:
            search_file = input("ingrese el nombre del archivo:")
            file = open(search_file, 'r')
            print(f"Archivo '{search_file}' abierto exitosamente.")
            return file
        except FileNotFoundError as e:
            print(f"no existe un archivo llamado {search_file}")

            with open ("error.log", 'a') as error_log:
                error_log.write(f"no se encontro el archivo '{search_file}' \n")
            if end_program:
                print("Cerrando del programa debido a error en la lectura del archivo.")
                exit() 

            print("haz tu segundo intento \n")

            try:
                search_file = input("ingrese el nombre del archivo nuevamente:")
                file = open(search_file, 'r')
            except FileNotFoundError as e:
                print(f"no existe un archivo llamado {search_file}")

            with open ("error.log", 'a') as error_log:
                error_log.write(f"no se encontro el archivo '{search_file} por segunda vez' \n")  

            print("no se pudo abrir el archivo despues de 2 intentos, el programa va a cerrar")
            exit()              


