"""
Una lista comprehension combina el for loop y
y la creación de nuevos elementos en una sola línea
y automáticamente agrega cada nuevo elemento a la lsita, es decir
sin usar el metodo append
"""

squares = [value**2 for value in range(1,11)] #se utiliza para generar listas de manera autom. en oneline
print(squares)

names = ["Samuel", "Balam", "vitor","SanCharly", "Jaime"]

names_upv = [name+"@upv.edu.mx" for name in names]
print(names_upv)