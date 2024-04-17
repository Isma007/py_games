from getpass import getpass


def menu():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
print(id(menu()))
def main():
    menu()
    while True:
        suma_puntos_a=0
        suma_puntos_b=0
        while suma_puntos_a<=2 and suma_puntos_b<=2:
            player_a = getpass("Jugador A, selecciona r = rock, p = paper or s = scissors--> ")
            player_b = getpass("Jugador B, selecciona r = rock, p = paper or s = scissors--> ")
            print(f"\n{player_a},{player_b}")
            if player_a =="r" and player_b=="s":
                    print("Jugador A gana, piedra gana a tijeras")
                    suma_puntos_a += 1
                    print("El total de puntos de jugador1 y jugador2 son: ",suma_puntos_a, " & ", suma_puntos_b)

            elif player_a =="s" and player_b=="r":
                    print("Jugador B gana, piedra gana a tijeras")
                    suma_puntos_b+=1
                    print("El total de puntos de jugador1 y jugador2 son: ",suma_puntos_a," & ",suma_puntos_b)

            elif player_a =="p" and player_b=="r":
                    print("Jugador A gana, papel gana a piedra")
                    suma_puntos_a+=1
                    print("El total de puntos de jugador1 y jugador2 son: ", suma_puntos_a, " & ", suma_puntos_b)

            elif player_a=="r" and player_b=="p":
                    print("Jugador B gana, papel gana a piedra")
                    suma_puntos_b+=1
                    print("El total de puntos de jugador1 y jugador2 son: ", suma_puntos_a, " & ", suma_puntos_b)

            elif player_a=="s" and player_b=="p":
                    print("Jugador A gana, Tijeras ganan a papel")
                    suma_puntos_a+=1
                    print("El total de puntos de jugador1 y jugador2 son: ", suma_puntos_a, " & ", suma_puntos_b)

            elif player_a=="p" and player_b=="s":
                    print("Jugador B gana, papel gana a tijeras")
                    suma_puntos_b+=1
                    print("El total de puntos de jugador1 y jugador2 son: ", suma_puntos_a, " & ", suma_puntos_b)
        if suma_puntos_a==3:
            print("El jugador A gana la batalla")
            print("GRACIAS POR JUGAR AL PIEDRA PAPEL O TIJERA")
            break
        elif suma_puntos_b==3:
            print("El jugador B gana la batalla")
            print("GRACIAS POR JUGAR AL PIEDRA PAPEL O TIJERA")
            break
main()
