class Fila:
    def __init__(self):
        self.fila = []
        
    def enfileirar(self, valor):
        self.fila.append(valor)
        
    def desenfileirar(self):
        if not self.fila:
            print("A fila está vazia")
        else:
            removido = self.fila.pop(0)
            print(f"{removido} removido da lista")
            return removido
        
    def espiar(self):
        if not self.fila:
            print("A fila está vazia")
        else:
            primeiro = self.fila[0]
            print(f"{primeiro} é o primeriro item da lista")
            return primeiro
    
    def esta_vazia(self):
        if self.fila:
            print("Fila populada")
            return True
        else:
            print("Fila vazia")
            return False
        
fila = Fila()
fila.enfileirar("Erick")
fila.enfileirar("Júlio")
fila.enfileirar("Érica")
fila.desenfileirar()
fila.espiar()
fila.desenfileirar()
fila.esta_vazia()
fila.desenfileirar()
fila.esta_vazia()