class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        print('Raaawr!')
        
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def emitir_som(self):
        print('Woof!')
        
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def emitir_som(self):
        print('Miau!')
        
leao = Animal("Simba")
cachorro = Cachorro("Snoopy")
gato = Gato("Garfield")

for x in (leao, cachorro, gato):
    x.emitir_som()    