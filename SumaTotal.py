print ("SumaTotal")

def main():
    total = 0
    while True:
            numero = float(input("Digite un número del 1 - 9 y digite 0 para salir): "))
            if numero == 0:
                break    
            total += numero
     
    print("Suma de los números:", total)

if __name__ == "__main__":
    main()