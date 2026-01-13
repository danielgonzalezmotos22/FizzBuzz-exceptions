def getnum():
    # num = int(input("diga un numero: "))
    
    try:
        num = int(input("diga un numero: "))
    except Exception:
        num = int(input("Argumento no valido, diga otro argumento: "))
    # print (num)
    if num %3 == 0 and num %5 == 0:
        print("FizzBuzz")
    elif num %5 == 0:
        print("Buzz")
    elif num %3 == 0:
        print("Fizz")
    else:
        print(num)
    return num
      
    # try:
    #     num ==
    # except ValueError:
    #     print("Argumento no valido")

if __name__ == "__main__":
    print(getnum())
    # print(FizzBuzz())
