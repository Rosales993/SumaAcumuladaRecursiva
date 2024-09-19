def suma_acumulada(n):
    # ... (código con documentación y manejo de errores)
    def suma_acumulada_iterativo(n):
        suma = 0
        for i in range(1, n + 1):
            suma += i
        return suma

# Obtener el valor de n del usuario de forma segura
while True:
    try:
        n = int(input("Ingrese un valor positivo: "))
        if n < 0:
            raise ValueError("n debe ser un número entero positivo")
        break
    except ValueError:
        print("Por favor, ingrese un número entero positivo válido.")

# Calcular y mostrar la suma acumulada
resultado = suma_acumulada(n)
print(f"\nEl total de toda la suma acumulada es: {resultado}")