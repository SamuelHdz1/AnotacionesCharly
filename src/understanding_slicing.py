players = ["samuel", "messi" , "balam" , "jaime", "victorkun"]
print("lista original:", players)

#Slicings
print(players[3:5]) #jaime victorkun
print()

#El slicing me permite trabajar con un grupo 
#especifico de una lista: se le conoce como un 
#"slice".

#players = ["samuel", "messi" , "balam" , "jaime", "victorkun"]

print("1:4", players[1:4])
print(":3", players[:3])
print("2:", players[2:])
print("-3:", players[-3:])

print()

#players = ["samuel", "messi" , "balam" , "jaime", "victorkun"]
#Casos especiales de Slicing
print("casos especiales".upper())
print(players)
print(players[1:10]) #cuando el inidice de la derecha es mayor me va a mandar hasta el ultimo
print(players[-10:10]) 
print(players[6:1]) #LISTA VACIA
print(players[1:0])#desde el inicio hasta la 0 -1

#Looping through a slice
print("looping through a slice")
students = ["samuel","peter","charly","jaime","gfgfg"]

#Slicing [::] Tarea
for student in students:
    print(f"el estudiante (student)") 






#¿Como podemos copiar una lista?
my_food = ["pizza","tacos", "flautas"]
my_friend_food_ = my_food #Manera errónea de copiar una lista

#Maneras de copiar lista
#metodo 1 - utilizando slicing
my_friend_food_2 = [:]

#metodo 2 - utilizando el metodo de las listas .copy()
my_friend_food_3 = my_food.copy()

#metodo 3 - utilizando el metodo build-in list

