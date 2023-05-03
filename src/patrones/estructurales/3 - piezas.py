"""
Represente la lista de piezas componentes de un ensamblado con sus
relaciones jerárquicas. Empiece con un producto principal formado por tres
sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
que representen esa configuración y la muestren. Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón
composite).
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Pieza(ABC):

    @property
    def parent(self) -> Pieza:
        return self._parent

    @parent.setter
    def parent(self, parent: Pieza):
        self._parent = parent


    def add(self, component: Pieza) -> None:
        pass

    def remove(self, component: Pieza) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class PiezaLeaf(Pieza):
    def operation(self) -> str:
        return "Pieza Leaf"


class Composite(Pieza):
    def __init__(self) -> None:
        self._children: List[Pieza] = []

    def add(self, component: Pieza) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Pieza) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Pieza) -> None:
    print(f"RESULT: {component.operation()}", end="")



if __name__ == "__main__":
    print("")

    producto_final = Composite()

    subconj1 = Composite()
    subconj2 = Composite()
    subconj3 = Composite()

    for i in range(4):
        subconj1.add(PiezaLeaf())
        subconj2.add(PiezaLeaf())
        subconj3.add(PiezaLeaf())
    
    producto_final.add(subconj1)
    producto_final.add(subconj2)
    producto_final.add(subconj3)

    subconj4 = Composite()

    for i in range(4):
        subconj4.add(PiezaLeaf())

    producto_final.add(subconj4)

    client_code(producto_final)

    print("")
