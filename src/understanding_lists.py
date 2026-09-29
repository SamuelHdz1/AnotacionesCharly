#LISTAS
#Las listas son elementos mutables, eso es que su tamaño cambia en tiempo  real

"""
Las listas nos permiten almacenar información en un lugar,
la canridad que se desee: ya sean pocos elementos o millones de elementos.

Una lista es una colección de ítems (elementos) que tiene
un orden particular. Se pueden crear listas que incluyan 
strings, enteros, floats, los nombres de las personas de tu familia, etc.
Podemos almacenar (los tipos de datos permitidos en Python) lo que queremos es una lista.

Son elementos mutables: Puede modificarse el tamaño de la lista.

Se recomienda nombrar una variable de tipo lista en plural.

En python, los corchetes [] indican una lista,
sus elementos se separan por comas.

Ejemplo:
"""
bicycles = [ "trek","cannondale", "redline", "specialized", "apache"]
print(bicycles)

#¿Cómo podemos acceder a los elementos de una lista? Cuando hablemos de índices se empieza desde 0

"""
Las listas son colecciones ordenadas. Se puede acceder
a un elemento de una lista diciéndole a Python la posición
o índice del elemento deseado.

Para obtener el valor deseado, se debe escribir el nombre de la lista,
seguido del índice del elemento entre corchetes. 

"""

print(bicycles[0], bicycles[1], bicycles[2])

print(bicycles[0].upper())

#Los indices comienzan en 0, no en 1
#bicycles =  [ "trek","cannondale", "redline", "specialized", "apache"]
#Ejemplo

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1]) #-1 es el último
print(bicycles[-2]) #-2 es el penultimo

#utilizando valores individuales de una lista
message = f"Mi first bicycle was a {bicycles[-1].upper()}"
print(message)
