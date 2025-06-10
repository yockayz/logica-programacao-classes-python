class Retangulo:
    def __init__(self):
        self._height = None
        self._width = None

    def calcular_area(self):
        area = self._height * self._width
        return area

    def calcular_perimetro(self):
        perimeter = (self._height * 2) + (self._width * 2)
        return perimeter
    
    def get_height(self):
        return self._height
    
    def set_height(self, height):
        self._height = height
        if self._height < 0:
            self._height *= -1
    
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        self._width = width
        if self._width < 0:
            self._width *= -1

rect = Retangulo()
rect.set_height(-15)
rect.set_width(-7)
altura = rect.get_height()
largura = rect.get_width()
area = rect.calcular_area()
perimetro = rect.calcular_perimetro()
print(f"""Altura: {altura} | Largura: {largura} | Área: {area} | Perímetro: {perimetro}""")