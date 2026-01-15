from kata_fizzbuzz import FizzBuzz
import pytest
def num_div3():
    #Prueba si el numero es divisible entre 3 retorna "Fizz"
    assert FizzBuzz(3) == "Fizz"

def num_div5():
    #Prueba si el numero es divisible entre 5 retorna "Buzz"
    assert FizzBuzz(5) == "Buzz"

def num_div15():
    #Prueba si el numero es divisible entre 15 retorna "FizzBuzz"
    assert FizzBuzz(15) == "FizzBuzz"

def si_numero_es_negativo():
    with pytest.raises(ValueError):
        FizzBuzz(-3)