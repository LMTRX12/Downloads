# print("ingrese 3 numeros")
# n1=float(input("ingrese un numero"))
# n2=float(input("ingrese otro numero"))
# n3=float(input("ingrese otro numero"))
# prom=(n1+n2+n3)/3
# print("el promedio es", round(prom, 1))
# if prom>=4:
#     print("el alumno aprobo")
# else:
#     print("el alumno reprobo")  
# print("el valor a apagar es")
# print("el valor a apagar es")
# print("el valor a apagar es")
# print("el valor a apagar es")

# op=int(input())
# if op==1:
#     print("el valor a pagar es")
# elif op==2:
#     print("el valor a pagar es")
# elif op==3:
#     print("el valor a pagar es")
# else:print("opcion invalida")

# n= "colonia"
# name= "alonso"
# name="eva"
# print(name(0))
# print(leb(name))
# print(n.strip())
# print(name.upper())
# print(name.lower())
# print(name.replace())
# print(name.split(
# SHAZAM= "SHAZAM"
# print("ingresar contraseña")
# clave=str(input("clave"))

# if clave==SHAZAM:
#     print("es correcto")
# else:print("invalido")

# user=input("ingrese el nombre de usuario")

# if len(user)>4 and len(user)<=10:
# print("error, el maximo de letras son 10")
# elif len(user)>10:
# print("usuario invalido")
# else:
# print("usuario creado correctamente")

# pin=int(input("ingrese su pin: "))

# if len(str(pin))

candidato1 = "Alonso"
candidato2 = "Eva"

votos1 = 0
votos2 = 0

print("votaciones")
cantidad_votantes = int(input("cantidad de personas que votaran: "))

for i in range(cantidad_votantes):
    print("\nAlternativas de voto:")
    print("1.", candidato1)
    print("2.", candidato2)
    
    voto = int(input("Votante número " + str(i+1) + ", ingrese su opción (1 o 2): "))
    
    if voto == 1:
        votos1 = votos1 + 1
    elif voto == 2:
        votos2 = votos2 + 1
    else:
        print("Voto nulo (opción inválida)")

print("\n---resultados---")
print(candidato1, "tuvo:", votos1, "votos")
print(candidato2, "tuvo:", votos2, "votos")

if votos1 > votos2:
    print("el ganador es:", candidato1)
elif votos2 > votos1:
    print("el ganador es:", candidato2)
else:
    print("es un empate")