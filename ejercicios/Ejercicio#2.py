if __name__ == "__main__":
    def circulo(a):
        pi=3.14
        total=pi*a**2
        return(total)
    radio=float(input("Digite radio\n"))
    print("El area es:", circulo(radio))
