print("Menu")
while True:
    print("1- Convertir grados a Celsius a Fahrenheit")
    print("2- Convertir dólar a pesos")
    print("3- Convertir metros a pies")
    print("4- Salir")

    menu = input("Digite el número de la opción: ")

    if menu == '1':
        celsius = float(input("Digite en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

    elif menu == '2':
        dolares = float(input("Digite la cantidad en dólares: "))
        tasa = 58.52
        pesos = dolares * tasa
        print(f"{dolares} dólares son {pesos} pesos dominicanos.")

    elif menu == '3':
        metros = float(input("Digite cantidad de metros: "))
        pies = metros * 3.281
        print(f"{metros} metros son {pies} pies.")

    elif menu == '4':
        print("Detuvo el programa")
        break

    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")