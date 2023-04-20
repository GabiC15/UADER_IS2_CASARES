# Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar
# para construir aviones en lugar de vehículos. Para simplificar suponga que un
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPlane(self):
        plane = Plane()

        undercarriage = self.__builder.getUndercarriage()
        plane.setBody(undercarriage)

        body = self.__builder.getBody()
        plane.setBody(body)

        turbine = self.__builder.getTurbines()
        plane.attachTurbine(turbine)
        plane.attachTurbine(turbine)

        wing = self.__builder.getWings()
        plane.attachWing(wing)
        plane.attachWing(wing)

        return plane


class Plane:
    def __init__(self):
        self.__turbines = list()
        self.__wings = list()
        self.__body = None
        self.__undercarriage = None

    def setBody(self, body):
        self.__body = body

    def setUndercarriage(self, undercarriage):
        self.__undercarriage = undercarriage

    def attachTurbine(self, turbines):
        self.__turbines.append(turbines)

    def attachWing(self, wings):
        self.__wings.append(wings)

    def specification(self):
        print("chasis: %s" % (self.__body.shape))
        print("turbinas: %d" % (self.__turbines[0].power))
        print("alas: %d\'" % (self.__wings[0].size))


class Builder:

    def getBody(self): pass
    def getUndercarriage(self): pass
    def getTurbines(self): pass
    def getWings(self): pass


class BoeingBuilder(Builder):

    def getWings(self):
        wings = Wings()
        wings.size = 22
        return wings

    def getTurbines(self):
        turbine = Turbine()
        turbine.power = 400
        return turbine

    def getBody(self):
        body = Body()
        body.shape = "Fuselaje Ancho"
        return body

    def getUndercarriage(self):
        undercarriage = Undercarriage()
        return undercarriage


class Turbine:
    power = None


class Wings:
    size = None


class Undercarriage:
    pass


class Body:
    shape = None


def main():
    boeingBuilder = BoeingBuilder()  # initializing the class
    director = Director()

    director.setBuilder(boeingBuilder)

    boeing = director.getPlane()

    boeing.specification()


if __name__ == "__main__":
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

    main()
