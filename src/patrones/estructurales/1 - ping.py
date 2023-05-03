"""
Provea una clase ping que luego de creada al ser invocada con un método
“execute(string)” realice 10 intentos de ping a la dirección IP contenida en
“string” (argumento pasado), la clase solo debe funcionar si la dirección IP
provista comienza con “192.”. Provea un método executefree(string) que haga
lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
www.google.com usando el método executefree de ping y re-envie a execute
de la clase ping en cualquier otro caso. (Modele la solución como un patrón
proxy).
"""

from abc import ABC, abstractmethod
from pythonping import ping


class Subject(ABC):

    @abstractmethod
    def execute(self, direccion) -> None:
        pass

    @abstractmethod
    def executefree(self, direccion) -> None:
        pass


class Ping(Subject):
    def execute(self, direccion) -> None:
        if self.check_ip(direccion):
            ping(direccion, verbose=True, count=10)
    
    def executefree(self, direccion) -> None:
        ping(direccion, verbose=True, count=10)

    def check_ip(self, direccion) -> bool:
        if direccion[:2] != "192":
            print("La direccion debe comenzar con '192'")
            return False
        return True


class PingProxy(Subject):
    def __init__(self, real_subject: Ping) -> None:
        self._proxy = real_subject

    def execute(self, direccion) -> None:
        if(direccion == "192.168.0.254"):
            self._proxy.executefree("www.google.com")
            return
        self._proxy.execute(direccion)

    def executefree(self, direccion) -> None:
        self._proxy.execute(direccion)


def client_code(subject: Subject) -> None:
    direccion = "192.168.0.254"
    subject.execute(direccion)



if __name__ == "__main__":
    print("")

    real_ping = Ping()
    proxy = PingProxy(real_ping)

    client_code(proxy)

    print("")

