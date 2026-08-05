def mi_agenda():
    contactos = {}
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Anadir contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")

        opcion = input("\nSelecciona una opcion (1-5): ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ").strip()
            if nombre in contactos:
                print("Este contacto ya existe.")
            else:
                telefono = input("Telefono: ")
                correo = input("Correo electronico: ")
                contactos[nombre] = {"telefono": telefono, "correo": correo}
                print(f"Contacto {nombre} guardado con exito.")
        elif opcion == "2":
            if not contactos:
                print("La agenda esta vacia.")
            else:
                print("\n--- Lista de Contactos ---")
                for nombre, datos in contactos.items():
                    print(f"Contactos: {nombre} -> Tel: {datos['telefono']} | Email: {datos['correo']}")
        elif opcion == "3":
            nombre = input("Introduce el nombre a buscar: ").strip()
            if nombre in contactos:
                print(f"\nInformacion de {nombre}:")
                print(f"Telefono: {contactos[nombre]['telefono']}")
                print(f"Correo: {contactos[nombre]['correo']}")
            else:
                print("Contacto no encontrado.")
        elif opcion == "4":
            nombre = input("Introduce el nombre a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print("No se encontro ese contacto.")
        elif opcion == "5":
            print("Saliendo de la agenda")
            return
        else:
            print("Opcion incorrecta. Intentalo de nuevo.")

if __name__ == "__main__":
    mi_agenda()
