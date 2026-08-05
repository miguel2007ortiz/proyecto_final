def calculadora():
    print("=== CALCULADORA INTERACTIVA ===")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Salir")
    
    opcion = input("\nElige una opción (1-5): ")
    
    if opcion == "5":
        print("¡Hasta luego!")
        return

    if opcion in ["1", "2", "3", "4"]:
        # Solicitamos los números al usuario y los convertimos a decimales (float)
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        if opcion == "1":
            resultado = num1 + num2
            print(f" Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f" Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f" Resultado: {num1} * {num2} = {resultado}")
        elif opcion == "4":
            # Validamos que no se divida entre cero para evitar que el programa falle
            if num2 == 0:
                print(" Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f" Resultado: {num1} / {num2} = {resultado}")
    else:
        print(" Opción no válida. Inténtalo de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
