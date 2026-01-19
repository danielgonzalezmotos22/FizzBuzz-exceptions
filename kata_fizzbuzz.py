def FizzBuzz(num):
   
    if num %3 == 0 and num %5 == 0:
        return ("FizzBuzz")
    elif num %5 == 0:
        return("Buzz")
    elif num %3 == 0:
        return("Fizz")
    else:
            print(num)
    return num
      

if __name__ == "__main__":
    i = 0
    while i == 0:
        try:
            num = int(input("diga un numero entre 0 y 100: "))
            if not num <=0 and num >= 101:
                print(f"Numero invalido, diga otro numero: {num}")
            else:
                i += 1
        except ValueError:
            print("Diga otra cosa")
    print(FizzBuzz(num))
