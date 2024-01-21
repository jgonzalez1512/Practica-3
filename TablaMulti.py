print("Tabla de multiplicar")

for numero in range(1, 1001):
    if numero % 5 == 0:
        print(f"Tabla de multiplicar del {numero}:")
        for multiplicador in range(1, 11):
            resultado = numero * multiplicador
            print(f"{numero} x {multiplicador} = {resultado}")
