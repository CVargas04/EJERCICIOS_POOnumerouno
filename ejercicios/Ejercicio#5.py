if __name__ == "__main__":
    def temperatura(a):
        total = (a - 32) / 1.8
        return(total)

    print("BIENVENIDO AL CONVERTIDOR DE TEMPERATURA")
    print(" ")

    farenheit = float(input("Digita temperatura en grados farenheit \n"))

    print("La tempertura en Celsius es: ", temperatura(farenheit))