class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(reg):
        self.registro = reg

    def asignarTipo(tip):
        tip = tip.lower()
        if tip == "electrico":
            self.tipo = tip
        
        elif tip == "gasolina":
            self.tipo = tip
