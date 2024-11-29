import modulos  # Importa el módulo con las funciones

def main():
    print("\n--- Prueba de funciones del módulo ---\n")

    # Test de read_int()
    try:
        numero_entero = modulos.read_int(prompt="Ingrese un número positivo: ", qty_attempts=3, only_positives=True)
        print(f"Número entero ingresado: {numero_entero}")
    except Exception as e:
        print(e)

    # Test de read_floating_point()
    try:
        numero_decimal = modulos.read_floating_point(prompt="Ingrese un número positivo: ", qty_attempts=2, only_positives=True)
        print(f"Número decimal ingresado: {numero_decimal}")
    except Exception as e:
        print(e)

    # Test de get_file()
    archivo = modulos.get_file(end_program=False)
    if archivo:
        print(f"Archivo abierto exitosamente: {archivo.name}")
        archivo.close()
    else:
        print("No se pudo abrir el archivo.")

    # Test de display_menu()
    # Prueba de display_menu() con opciones numéricas
    opciones_numericas = ["Iniciar sesión", "Registrar usuario", "Salir"]
    modulos.display_menu(opciones_numericas, titulo_menu="MENÚ PRINCIPAL", caracter_opciones="numerico")

    # Prueba de display_menu() con opciones alfabéticas
    opciones_alfabeticas = ["Configurar", "Actualizar", "Cerrar"]
    modulos.display_menu(opciones_alfabeticas, titulo_menu="CONFIGURACIÓN", caracter_opciones="alfabetico")


if __name__ == "__main__":
    main()
