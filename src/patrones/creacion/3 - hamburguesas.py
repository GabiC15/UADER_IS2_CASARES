# Genere una clase donde se instancie una comida rápida “hamburguesa” que
# pueda ser entregada en mostrador, retirada por el cliente o enviada por
# delivery. A los efectos prácticos bastará que la clase imprima el método de
# entrega.

class Hamburguesa:
    def __init__(self, tipo):
        self.tipo = tipo


class EntregaCreator:
    def entregar(self):
        pass


class Mostrador(EntregaCreator):
    def __init__(self, hamburguesa):
        self.hamb = hamburguesa

    def entregar(self):
        print(
            f"Se ha entregado una hamburguesa {self.hamb.tipo} en el mostador")


class RetiroCliente(EntregaCreator):
    def __init__(self, hamburguesa):
        self.hamb = hamburguesa

    def entregar(self):
        print(
            f"Se ha entregado una hamburguesa {self.hamb.tipo} al cliente")


class Delivery(EntregaCreator):
    def __init__(self, hamburguesa):
        self.hamb = hamburguesa

    def entregar(self):
        print(
            f"Se ha entregado una hamburguesa {self.hamb.tipo} por delivery")


hamburguesa = Hamburguesa("doble")

Mostrador(hamburguesa).entregar()
RetiroCliente(hamburguesa).entregar()
Delivery(hamburguesa).entregar()
