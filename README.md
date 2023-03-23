# 2023 S1 Laboratorio 5

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio5.py**
- Debe realizar la siguiente función con recursión de cola
- No olvidar los comentarios


## Ejercicio 1. Valor 10 puntos.
Escriba una función sumaImparesPares (lista1 , lista2) que reciba dos lista de números, y retorne una lista que contenga la suma de las posiciones pares de las dos listas de la misma manera con las posiciones impares. No puede usar len (), solo puede recorrer la lista una vez. La función debe comportarse de la siguiente manera:

```python
>>> sumaImparesPares([0,2,3,4], [4, 8, 6, 0])
[13, 14]
>>> sumaImparesPares([10, 0], [100, 2])
[110, 2]
 >>> sumaImparesPares([1,2], "dos")
 "Error: segundo argumento debe ser entero"
 ```

## Ejercicio 2. Valor 10 puntos.
Escriba una función llamada **eliminarElemento** que reciba como parámetro de entrada una lista con diferentes elementos es decir enteros, flotantes y cadenas de texto, y otra variable llamdo **elemento**, y eliminar si este elemento de esta lista. Hacer uso de la iteración y evitar funciones built-in.

```python
>>> eliminarElemento( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] , 12 )
[78, 0, 5.2, "abc", 0, 5.2]
>>> eliminarElemento( [12, 5.2, 12], 5 )
[12, 5.2, 12]
```
## Ejercicio 3. Valor 10 puntos.
Escriba una función llamada **eliminarRepetidos** que reciba como parámetro de entrada una lista con diferentes elementos es decir enteros, flotantes y cadenas de texto, y eliminar si un elemento de esta lista aparece más de una vez. Hacer uso de la iteración y evitar funciones built-in.

```python
>>> eliminarRepetidos( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] )
[78, "abc"]
>>> eliminarRepetidos( [12, 5.2, 12] )
[5.2]
```
