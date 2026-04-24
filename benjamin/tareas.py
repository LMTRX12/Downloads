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