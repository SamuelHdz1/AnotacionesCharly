#LISTAS DE NUMEROS

"""
Las listas también pueden almacenar números. Python
ofrece varias herramientas que ayudan a trabajar eficientemente 
con listas de números.
"""
#METODO BUILD-IN range ()
"""
El método range nos ayuda a crear fácilmente 
series de números.

Ejemplo
"""
for value in range(1,5): #DONDE COMIENZO Y TERMINO -1
    print(value) 

#IMPORTANTEE Range solo genera numeros, no crea listas
first_ten_numbers = range(0,10)
#first_ten_numbers = range(0,10)
for value in first_ten_numbers:
    print(value)

numbers = list(range(0,10))
print(numbers)

#LISTA DE NUNEROS PARES 
even_numbers = list(range(0,11,2))
#¿que pasa con un paso negativo?
print(even_numbers)

table_multplication = list(range(0,51,5))
print(table_multplication)