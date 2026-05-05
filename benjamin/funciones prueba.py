# [import random
# num=random,randint(1,10)
# print(num)

# for i in range(num):
#     print("hola benja")

# for i in range(10):
#     print(f"(num)")

# import random

# nombre = input("ingre nombre")
# print("bienvenido" + nombre)

# j1 = random.randint(60, 190)
# j2 = random.randint(60, 190)
# j3 = random.randint(60, 190)

# print("j1 lanzó: " + str(j1) + "m")
# print("j2 lanzó: " + str(j2) + "m")
# print("j3 lanzó: " + str(j3) + "m")

# mas_fuerte = j1
# ganador = "j1"

# if j2 > mas_fuerte:
#     mas_fuerte = j2
#     ganador = "j2"

# if j3 > mas_fuerte:
#     mas_fuerte = j3
#     ganador = "j3"

# print("\nel golpe más fuerte fue de " + ganador + " con " + str(mas_fuerte) + " metros")
# print("nos vemos " + nombre)


# import random

# dado1 = random.randint(1, 6)
# dado2 = random.randint(1, 6)

# print("dado 1 dio " + str(dado1))
# print("dado 2 dio " + str(dado2))

# import random

# posicion = 0
# turnos = 0

# while posicion < 50:
#     turnos = turnos + 1
    
#     dado1 = random.randint(1, 6)
#     dado2 = random.randint(1, 6)
    
#     avance = dado1 + dado2
#     posicion = posicion + avance
    
#     print("turno " + str(turnos))
#     print("dado 1 dio " + str(dado1))
#     print("dado 2 dio " + str(dado2))
#     print("avanza a la posicion " + str(posicion))
#     print("-" * 20)

# print("¡llegaste a la meta!")
# print("te tomo " + str(turnos) + " turnos llegar")

# import random

# n1 = random.randint(1, 9)
# n2 = random.randint(1, 9)
# n3 = random.randint(1, 9)

# print("objetivo: " + str(n1) + " " + str(n2) + " " + str(n3))

# i1 = 0
# i2 = 0
# i3 = 0
# tiros = 0

# while i1 != n1 or i2 != n2 or i3 != n3:
#     tiros = tiros + 1
#     i1 = random.randint(1, 9)
#     i2 = random.randint(1, 9)
#     i3 = random.randint(1, 9)

# print("ganaste")
# print("numeros: " + str(i1) + " " + str(i2) + " " + str(i3))
# print("te tomo " + str(tiros) + " intentos")

# peso = float(input("Peso (grs): "))
# while peso <= 0:
#     peso = float(input("Error. Peso: "))

# sodio = float(input("Sodio (%): "))
# while sodio < 1 or sodio > 100:
#     sodio = float(input("Error. Sodio: "))

# destino = input("Nacional (N) o Internacional (I): ").upper()

# tipo = ""

# if peso < 500:
#     tipo = "lata normal"
# elif peso >= 501 and peso <= 1500:
#     tipo = "lata mediana"
# else:
#     tipo = "lata grande"

# if sodio >= 5 and sodio <= 8:
#     tipo = "lata especial"
# elif sodio >= 9:
#     tipo = "lata acorazada"

# print("-" * 20)
# print("Producto: " + tipo)

# if destino == "I":
#     print("Pegar sticker sanitario")

# print("-" * 20)