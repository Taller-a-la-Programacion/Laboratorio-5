import Laboratorio5;
import pytest;
    
    
def test_sumaImparesPares_1():
    assert Laboratorio5.sumaImparesPares([0,2,3,4], [4, 8, 6, 0]) == [13, 14]
    
def test_sumaImparesPares_2():
    assert Laboratorio5.sumaImparesPares([10, 0], [100, 2]) == [110, 2]
    
def test_sumaImparesPares_3():
    assert isinstance(Laboratorio5.sumaImparesPares([1,2], "dos"), str) == isinstance("Error: segundo argumento debe ser entero", str)
    

def test_eliminarElemento_1():
    assert Laboratorio5.eliminarElemento( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12], 12 ) == [78, 0, 5.2, "abc", 0, 5.2]
    
def test_eliminarElemento_2():
    assert Laboratorio5.eliminarElemento( [12, 5.2, 12], 5 ) == [12, 5.2, 12]
    
    
def test_eliminarRepetidos_1():
    assert Laboratorio5.eliminarRepetidos( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] , [12, 5.2, 0]) == [78, "abc"]
    
def test_eliminarRepetidos_2():
    assert Laboratorio5.eliminarRepetidos( [12, 5.2, 12], [12] ) == [5.2]
