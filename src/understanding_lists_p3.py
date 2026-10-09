#TRABAJANDO CON LISTAS

print("\n\tel dia de hoy voy a aprender a trabajar con listas\n".upper())


magicians = ["harry", "ron", "hermione","snape","voldemort"]
print(magicians)


print("ímprimir a la mala")

print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4])
print()
#for aux (cualquier nombre) in iter:

#    actions (identación 4 espacios desde el inicio) iter es iterable
#nombre de la lista en singular para acordarnos
#A esto se le conoce como looping
#for cat in cats:

#ciclo for
print("imprimir con un for")
for wizard in magicians: #for me imprime cada elmeento de la lista porque lo va recorriendo
    print(wizard.upper(), end=" ")
print()

#magicians = ["harry", "ron", "hermione","snape","voldemort"]
# Ahora vamos a imprimir un mensaje para cada mago
print()
for wizard in magicians:
    print(f"{wizard.title()} eso fue un gran hechizo.")
    print(f"no puedo esperar a ver el siguiente hechizo, {wizard.upper()}\n")

print("Gracias a todos, Fue un gran espectáculo")



#IDENTACION
"""

Python utiliza la identación para determinar cuando una 
línea de código está conectada a la línea de código anterior.

Básicamente, se utilizan 4 eespacios en blanco para 
obligarnos a escribir código ordenado y estructurado.

"""

#NO OLVIDEMOS INDENTAR - Traceback IdentationError
magicians = ["alice", "david", "samuel"]
#for magician in magicians:
#print(magician) #IdentationError

#ERROR DE LÓGICA
for magician in magicians:
    print(magician)
print(f"No puedo esperar a ver el siguiente truco, {magician.upper()}\n")

#IDENTACION INECESARIA
message = "hello python world"
#   print(message)

#No olvidar los dos puntos - Syntax Error
#for magician in magicians
#    print(magician)