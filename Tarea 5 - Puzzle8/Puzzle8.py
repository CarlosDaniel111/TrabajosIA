import heapq

inicial = [
    [5, 3, 2],
    [1, 4, 0],
    [8, 7, 6]
]
final = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def getPosicion(num):
    for i in range(3):
        for j in range(3):
            if final[i][j] == num:
                return i,j

def getManhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
    

def getHeuristica(tablero):
    heuristica = 0
    for i in range(3):
        for j in range(3):
            if tablero[i][j] != final[i][j]:
                x2,y2 = getPosicion(tablero[i][j])
                heuristica += getManhattan(i,j,x2,y2)
    return heuristica
                

class Nodo:
    def __init__(self, tablero,peso,heuristica,movimiento, anterior):
        self.tablero = tablero 
        self.anterior = anterior
        self.peso = peso
        self.heuristica = heuristica
        self.movimiento = movimiento
    
    def __lt__(self, other):
        return (self.peso + self.heuristica) < (other.peso + other.heuristica)

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

def main():
    print("BIENVENIDO AL PUZZLE 8")
    print("Tablero Inicial")
    for row in inicial:
        print(' '.join(f'{num:2}' for num in row))
    print('')

    visitados = set()
    colaPrioridad = []
    heapq.heappush(colaPrioridad, Nodo(inicial,0,getHeuristica(inicial),"",None))
    while colaPrioridad:
        current = heapq.heappop(colaPrioridad)
        if current.tablero == final:
            break
        visitados.add(str(current.tablero))
        movimientos = ['Arriba', 'Abajo', 'Izquierda', 'Derecha']
        for movimiento in movimientos:
            siguienteTablero = moverPieza(current.tablero,movimiento)
            if siguienteTablero is not None and str(siguienteTablero) not in visitados:
                heapq.heappush(colaPrioridad, Nodo(siguienteTablero,current.peso+1,getHeuristica(siguienteTablero),movimiento,current))
    
    if current.tablero != final:
        print("No se encontro solucion")
        return
    camino = []
    while current is not None:
        camino.append(current)
        current = current.anterior
    camino.reverse()

    print("Movimientos")
    for nodo in camino:
        if nodo.movimiento:
            print(f'Movimiento: {nodo.movimiento}')
            print('')
        for row in nodo.tablero:
            print(' '.join(f'{num:2}' for num in row))
        print('')

    print("Cantidad de Movimientos: ",len(camino)-1)
    print('')
    

if __name__ == "__main__":
    main()