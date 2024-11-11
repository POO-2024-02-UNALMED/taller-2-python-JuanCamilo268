from Asiento import Asiento
from Motor import Motor
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio,  marca, motor, registro, asientos = []):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos():
        cantidad = 0
        for i in self.asientos:
            if i != null:
                cantidad += 1
        return cantidad
    
    def verificarIntegridad():
        verificar = "Auto original"
        if self.registro != self.motor.registro:
            verificar = "Las piezas no son originales"
            return verificar
        else:
            for i in self.asientos:
                if self.registro != i.registro:
                    verificar = "Las piezas no son originales"
                    return verificar
        return verificar
