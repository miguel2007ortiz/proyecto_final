def sistema_inventario():
    # Usamos una lista para almacenar los productos del inventario
    inventario = []
    
    while True:
        print("\n=== 📦 SISTEMA DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio por unidad: "))
            
            # Guardamos las propiedades del producto en un diccionario
            producto = {
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio
            }
            inventario.append(producto)
            print(f"✅ ¡{nombre} agregado con éxito!")
            
        elif opcion == "2":
            if len(inventario) == 0:
                print("⚠️ El inventario está completamente vacío.")
            else:
                print("\n--- Lista de Productos ---")
                for prod in inventario:
                    total = prod['cantidad'] * prod['precio']
                    print(f"🔹 {prod['nombre']} | Cantidad: {prod['cantidad']} | Precio: ${prod['precio']} | Valor Total: ${total}")
                    
        elif opcion == "3":
            print("¡Cerrando el sistema de inventario! 👋")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    sistema_inventario()
