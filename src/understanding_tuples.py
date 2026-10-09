#LAS TUPLES SON LISTAS QUE NO PUEDO MODIFICAR/UNA LISTA CONSTANTE
#TUPLAS ELEMENTOS IMMUTABLES () Y LISTAS MUTABLES []

"""
TUPLAS

Las tuplas son listas de elementos que no cambian de tamaño,
los tuplas son elementos inmutables.

Se utilizan los paréntesis () para definir una tupla.

Ejemplo:

Si tenemos un rectangulo (largo, ancho) que siempre va
a tener cierto tamaño, podemos asegurar que sus dimensiones
no va a cambiar si colocamos sus valores en una tupla

"""

dimensions = (200, 50)
print("tupla original:", dimensions)

#vamos a imprimir elementos de una tupla
#se realiza de la misma forma que con una lista
print(dimensions[0])
print(dimensions[1])
#print(dir(dimensions))

#vamos a modificar el valor de una lista
names = ["carlos", "samuel", "charly","carlitos"]
print(names)
names[0] = "messi"
names[1] = "embape"
print(names)

#dimensions[0] = 500 #ESTA OPERACIÓN NO ESTÁ PERMITIDA

#looping throght a tuple
for dimension in dimensions:
    print(dimensions)

"""lo que si se puede es refinir el contenido de la variable, 
cambiar la asignación de la varible, es el truco para cambiar el valor de una variable."""


dimensions = (500, 1000, 20)
print("tupla re-definida:", dimensions)


 #TIPOS DE DATOS BOOLEANOS

answer = True
print(answer)