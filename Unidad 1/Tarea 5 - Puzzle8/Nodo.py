class Nodo:
    def __init__(self, tablero,peso,heuristica,movimiento, anterior):
        self.tablero = tablero 
        self.anterior = anterior
        self.peso = peso
        self.heuristica = heuristica
        self.movimiento = movimiento
    
    def __lt__(self, other):
        return (self.peso + self.heuristica) < (other.peso + other.heuristica)