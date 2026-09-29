#STRINGS

"""
Un string es de manera sencilla una serie de caracteres.
En python, todo lo que se encuentre entre comillas simples '' 
o dentro de comillas dobles "" se considera un string.

Ejemplo: "Esto es un string" 
'Esto también es un string'
'Le dije a un amigo, "python es mi lenguaje favorito"'
" El lenguaje 'python' lleva el nombre por Monty Python, no por la serpiente "

Ejemplo incorrecto: 

" Samuel '
' "
"""

name = 'sAMUEL hernández nAVA'
print (name)

print (name.title())

#title () Vuelve las iniciales mayus todo lo demás minus

print (name)

name = name.title()
print (name)

"""
Los métodos es una acción que python puede realizar sobre una variable

El punto después de la variable seguido por el nombre del método
en este caso title() dice que se tiene que ejecutar el método title()
de la variable name.

Todos los métodos van seguidos de paréntesis, porque en ocasiones necesitan información adicional para funcionar.
En esta ocasión, el método .title() no requiere información adicional para ejecutarse.
"""

# Otros métodos

print("----------")
print(name)
print(name.upper())
print(name.lower())
