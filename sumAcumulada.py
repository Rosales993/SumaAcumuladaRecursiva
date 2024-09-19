def suma_acumulada(n):

    #  si n es 1, la suma acumulada es 1
    if n == 1:
        print(f"Suma acumulada de 1 es: 1")
        return 1
    # recursividad: la suma acumulada de n es n más la suma acumulada de n-1
    else:
        resultado = n + suma_acumulada(n - 1)
        print(f"Suma acumulada de {n} es: {resultado}")
        return resultado

n = int(input("ingrese un valor positivo: "))
resultado = suma_acumulada(n)
print(f"\nEl total de toda la suma acumulada es  {resultado} ")