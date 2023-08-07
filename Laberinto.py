#juego del laberinto
import os
import readchar

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_matriz_laberinto(laberinto_cadena):
    laberinto_matriz = [list(fila) for fila in laberinto_cadena.strip().split("\n")]
    return laberinto_matriz

def mostrar_laberinto(laberinto):
    limpiar_pantalla()
    for fila in laberinto:
        print("".join(fila))

def main_loop(laberinto, inicio, fin):
    px, py = inicio

    while (px, py) != fin:
        mostrar_laberinto(laberinto)
        tecla = readchar.readkey()

        if tecla == 'n':
            numero += 1
            if numero > 50:
                numero = 50
            limpiar_pantalla()
            print(f"Tecla presionada: {tecla}")
            print(f"Número: {numero}")
        elif tecla == readchar.key.UP:
            nueva_px, nueva_py = px - 1, py
        elif tecla == readchar.key.DOWN:
            nueva_px, nueva_py = px + 1, py
        elif tecla == readchar.key.LEFT:
            nueva_px, nueva_py = px, py - 1
        elif tecla == readchar.key.RIGHT:
            nueva_px, nueva_py = px, py + 1
        else:
            continue

        if 0 <= nueva_px < len(laberinto) and 0 <= nueva_py < len(laberinto[0]) and laberinto[nueva_px][nueva_py] != "#":
            laberinto[px][py] = "."
            px, py = nueva_px, nueva_py
            laberinto[px][py] = "P"

    # El jugador ha llegado al final del laberinto
    mostrar_laberinto(laberinto)
    print("¡Felicidades, lo lograste, has salido del laberinto!")

def main():
    print("¡Bienvenido al juego de laberinto!")
    nombre_jugador = input("Por favor, ingresa tu nombre: ")
    print(f"¡Hola, {nombre_jugador}! Comencemos a jugar.")

    laberinto_cadena ="""......#...#
###.###.#.#
#.....#.#.#
#.#.#####.#
#.#.......#
#.###.#.###
#.#.#.#.#.#
###.#.#.#.#
#.....#...#
#########.#"""

    inicio = (0, 0)
    fin = (9, 9)

    laberinto = crear_matriz_laberinto(laberinto_cadena)
    main_loop(laberinto, inicio, fin)

if __name__ == "__main__":
    main()
