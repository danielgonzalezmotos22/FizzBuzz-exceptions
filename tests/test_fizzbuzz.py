from kata_fizzbuzz import FizzBuzz
import pytest
def test_num_div3():
    #Prueba si el numero es divisible entre 3 retorna "Fizz"
    assert FizzBuzz(3) == "Fizz"

def test_num_div5():
    #Prueba si el numero es divisible entre 5 retorna "Buzz"
    assert FizzBuzz(5) == "Buzz"

def test_num_div15():
    #Prueba si el numero es divisible entre 15 retorna "FizzBuzz"
    assert FizzBuzz(15) == "FizzBuzz"

def test_si_numero_es_negativo():
    with pytest.raises(ValueError):
        FizzBuzz(-3)
        
def test_numero_mayor_a_cien():
    with pytest.raises(ValueError):
        FizzBuzz(200)

def test_pasa_str():
    with pytest.raises(TypeError):
        FizzBuzz(str)

def test_numeros_decimales():
    with pytest.raises(TypeError):
        FizzBuzz(float)

def test_caracteres_especiales():
    with pytest.raises(TypeError):
        FizzBuzz("#")

def test_pasar_mas_de_dos_numeros():
    with pytest.raises(TypeError):
        FizzBuzz(3, 5)