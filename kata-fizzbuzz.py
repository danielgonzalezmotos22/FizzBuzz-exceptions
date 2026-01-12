def getnum():
    num = int(input("diga un numero: "))
    return num
def FizzBuzz():
    num = getnum
    if num %3 == 0:
        print("Fizz")
    elif num %5 == 0:
        print("Buzz")
    elif num %3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)
      
    # try:
    #     num == int or float
    # except:
    #     print("Argumento no valido")

if __name__ == "__main__":
    print(getnum())
    print(FizzBuzz())
