# Implemente una clase “factura” que tenga un importe correspondiente al total
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
# condición.

class Factura:
    def __init__(self, importe, condicion):
        self.importe = importe
        self.condicion = condicion

    def imprimir_factura(self):
        print(
            f"Factura con importe {self.importe} de condición '{self.condicion}'")


class FacturaCreator:
    def crear_factura(self, importe):
        pass


class IVAResponsableFacturaCreator(FacturaCreator):
    def crear_factura(self, importe):
        factura = Factura(importe * 1.21, "IVA Responsable")
        return factura


class IVANoInscriptoFacturaCreator(FacturaCreator):
    def crear_factura(self, importe):
        factura = Factura(importe, "IVA No Inscripto")
        return factura


class IVAExentoFacturaCreator(FacturaCreator):
    def crear_factura(self, importe):
        factura = Factura(importe, "IVA Exento")
        return factura


factura = IVAResponsableFacturaCreator().crear_factura(100)

factura.imprimir_factura()
