#!/usr/bin/env python3

# Inicializamos las variables
suma_total = 0
cantidad_numeros = 3

print(f"--- Calculadora de Promedio ({cantidad_numeros} números) ---")

# Bucle for para pedir los números
for i in range(cantidad_numeros):
    try:
        numero = float(input(f"Ingresa el número {i + 1}: "))
        suma_total += numero
    except ValueError:
        print("¡Error! Por favor, ingresa un número válido.")
        exit(1)

# Calculamos y mostramos el promedio
promedio = suma_total / cantidad_numeros
print(f"\nEl promedio es: {promedio:.2f}")
