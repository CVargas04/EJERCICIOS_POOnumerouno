if __name__ == "__main__":
    def factorial(r):
        if r==0 or r==1:
            total= 1
        else :
            total=r * factorial(r-1)
        return(total)
fact5=factorial(7)
print(fact5)
