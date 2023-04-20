# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
# deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
# esa base imponible.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Impuestos(metaclass=SingletonMeta):
    def getTotal(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contr_mun = base_imponible * 0.012

        return iva + iibb + contr_mun


imp1 = Impuestos()
imp2 = Impuestos()

if (imp1 == imp2):
    print("Son las mismas instancias")

print(imp1.getTotal(1000))

print(imp2.getTotal(1500))
