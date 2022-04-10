from math import sqrt


#Verifica daca un numar este obtinut dintr-un numar prim la puterea a treia si daca este mai mare ca 3
def cubPrim(arg):
    if(arg < 3):
        return False
    else:
        #Luam toate numerele prime de la 2 la arg si le verificam pe fiecare in parte
        for number in range(2, arg+1):
            is_prime = True
            for i in range(2, int(sqrt(number)) + 1):
                if (number % i == 0):
                    is_prime = False
                    break
            if is_prime and pow(number,3) == arg:
                return True
        return False

if __name__ == "__main__":
    print(cubPrim(27))

