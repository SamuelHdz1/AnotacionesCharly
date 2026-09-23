#Combinación o concatenación de Strings
first_name = "samuel"
last_name = "nava"

full_name = first_name + " " + last_name
print (full_name.title())

# esto no es suma de strings, es concatenación o combinación

print (full_name)

#Siempre los métodos llevan paréntesis, signifícan ejecutate 

print("hola".upper(), first_name + " " + last_name)

# esto + " " + es la concatenación, si pones first_name, last name es el mismo resultado pero no es concatenacoón

#Whitespace

"""
Se refiere a cualquier carácter que no se imprime, es decir,
un espacio (), tabuladores (\t)  y finales de línea (\n).

Loa whitespaces se utilizan comúnmente para
organizar las salidas de texto a usuario
de tal manera que sea más amigable de lerr o ber para los usarios
"""

print ("python")
print ("\tpython")
print ("\t\tpython")
print ("lenguajes: \n\tpython\nC\nJavaScript")

#Concatenación de Strings utilizando F-strings

print ("f-strings")
famous_person = "cabeza de vaca"
message = f"{famous_person} dijo que era buen gobernador"
print = (message)