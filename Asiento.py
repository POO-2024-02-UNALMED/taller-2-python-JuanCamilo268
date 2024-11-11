class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, nColor):
        nColor = nColor.lower()

        if nColor == "rojo":
            self.color = nColor

        elif nColor == "verde":
            self.color = nColor
        
        elif nColor == "amarillo":
            self.color = nColor

        elif nColor == "blanco":
            self.color = nColor

        elif nColor == "negro":
            self.color = nColor
       
        
        