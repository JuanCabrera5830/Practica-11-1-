def main():
    linea = input("DIGITE NUMERO: ")
    NUM = int(linea)
    I = 1

    while I <= 12:
        RESUL = NUM * I
        print(f"{NUM} * {I} = {RESUL}")
        I += 1

    input("Pulse una tecla para continuar...")

if __name__ == "__main__":
    main()
