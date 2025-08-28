def imprimir_y_multiplicar(dato):
    if not isinstance(dato, (int, float)):
        print("Error: Solo se permiten números (int o float).")
        return
    print("Dato recibido:", dato)
    resultado = dato * 2
    print("Resultado multiplicado por 2:", resultado)

# Ejemplo de uso
imprimir_y_multiplicar(10)
imprimir_y_multiplicar("hola")  # Esto mostrará el error
