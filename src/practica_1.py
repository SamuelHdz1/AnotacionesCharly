"""
Crear una lista con los 10 primeros números cuadraticos
"""

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = []
for value in range(1,11):
    square = value**2
    print(f"el número que calculé es {square}")
    squares.append(square)
print(squares)