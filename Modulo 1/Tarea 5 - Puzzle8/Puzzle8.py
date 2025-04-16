import heapq
import time
from Nodo import Nodo

tableroInicial = [
    [5, 3, 2],
    [1, 4, 0],
    [8, 7, 6]
]
tableroFinal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def getManhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def getHeuristica(tablero):
    heuristica = 0
    for x1 in range(3):
        for y1 in range(3):
            if tablero[x1][y1] != tableroFinal[x1][y1]:
                x2, y2 = next((i, j) for i in range(3) for j in range(3) if tablero[x1][y1] == tableroFinal[i][j])
                heuristica += getManhattan(x1,y2,x2,y2)
    return heuristica      

def moverPieza(tablero, movimiento):
    sigTablero = [row.copy() for row in tablero]
    x, y = next((i, j) for i in range(3) for j in range(3) if tablero[i][j] == 0)
    if movimiento == 'Arriba':
        if x > 0:
            sigTablero[x][y], sigTablero[x - 1][y] = sigTablero[x - 1][y], sigTablero[x][y]
            return sigTablero
    elif movimiento == 'Abajo':
        if x < 2:
            sigTablero[x][y], sigTablero[x + 1][y] = sigTablero[x + 1][y], sigTablero[x][y]
            return sigTablero
    elif movimiento == 'Izquierda':
        if y > 0:
            sigTablero[x][y], sigTablero[x][y - 1] = sigTablero[x][y - 1], sigTablero[x][y]
            return sigTablero
    elif movimiento == 'Derecha':
        if y < 2:
            sigTablero[x][y], sigTablero[x][y + 1] = sigTablero[x][y + 1], sigTablero[x][y]
            return sigTablero
    return None

def imprimirTablero(tablero):
    n = len(tablero)
    ancho = 3 
    def linea_horizontal(izq, medio, der):
        return izq + ("─" * ancho + medio) * (n - 1) + "─" * ancho + der

    borde_sup = linea_horizontal("┌", "┬", "┐")
    borde_mid = linea_horizontal("├", "┼", "┤")
    borde_inf = linea_horizontal("└", "┴", "┘")

    print(borde_sup)
    for i, row in enumerate(tablero):
        print("│ " + " │ ".join(f"{num if num else ' ':>{ancho-2}}" for num in row) + " │")
        if i < n - 1:
            print(borde_mid)
    print(borde_inf)
    print('')

def algoritmo_a_estrella():
    movimientos = ['Arriba', 'Abajo', 'Izquierda', 'Derecha']
    visitados = set()
    colaPrioridad = []
    heapq.heappush(colaPrioridad, Nodo(tableroInicial,0,getHeuristica(tableroInicial),"",None))
    while colaPrioridad:
        actual = heapq.heappop(colaPrioridad)
        if actual.tablero == tableroFinal:
            break
        visitados.add(str(actual.tablero))
        for movimiento in movimientos:
            siguienteTablero = moverPieza(actual.tablero,movimiento)
            if siguienteTablero is not None and str(siguienteTablero) not in visitados:
                heapq.heappush(colaPrioridad, Nodo(siguienteTablero,actual.peso+1,getHeuristica(siguienteTablero),movimiento,actual))
    return actual

def imprimirCamino(actual):
    camino = []
    while actual is not None:
        camino.append(actual)
        actual = actual.anterior
    camino.reverse()

    simboloMovimiento = {
        'Arriba': '↑',
        'Abajo': '↓',
        'Izquierda': '←',
        'Derecha': '→'
    }

    print("Movimientos realizados")
    for nodo in camino:
        if nodo.movimiento:
            print(f'Movimiento: {nodo.movimiento} ' + simboloMovimiento[nodo.movimiento])
            print('')
        imprimirTablero(nodo.tablero)

    print("Cantidad de Movimientos: ",len(camino)-1)

def main():
    # Tiempo inicial
    tiempoInicial = time.time()
    print("┌──────────┐")
    print("│ Puzzle 8 │")
    print("└──────────┘")
    print('')
    print("Tablero Inicial")
    imprimirTablero(tableroInicial)

    actual = algoritmo_a_estrella()
    
    
    if actual.tablero != tableroFinal:
        print("No se encontro solucion")
        print("Tiempo de ejecucion: ",time.time()-tiempoInicial, "segundos")
        return
    
    imprimirCamino(actual)
    print("Tiempo de ejecucion: ",time.time()-tiempoInicial, "segundos")
    

if __name__ == "__main__":
    main()