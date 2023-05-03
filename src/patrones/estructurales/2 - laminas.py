"""
Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
de 10 mts. Genere una clase que represente a las láminas en forma genérica al
cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
patrón bridge en la solución).
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class LaminaAbstraction:

    def __init__(self, implementation: TrenImplementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.fabricar_lamina()}")


class TrenImplementation(ABC):
    @abstractmethod
    def fabricar_lamina(self) -> str:
        pass


class TrenLamina5mtImplementation(TrenImplementation):
    def fabricar_lamina(self) -> str:
        return "Lamina de 5mt completada"


class TrenLamina10mtImplementation(TrenImplementation):
    def fabricar_lamina(self) -> str:
        return "Lamina de 10mt completada"


def client_code(abstraction: LaminaAbstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    print("")

    implementation = TrenLamina5mtImplementation()
    abstraction = LaminaAbstraction(implementation)
    client_code(abstraction)

    print("")
