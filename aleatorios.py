"""
Cuarta tarea de APA - Generación de números aleatorios

Ferran Gotarra
"""

class Aleat:
    """
    Clase Aleat que implementa un generador de números aleatorios
    en el rango 0 <= x_n < m usando el método LGC.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Constructor de la clase Aleat. Inicializa los parámetros del generador.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        """
        Método mágico que genera el siguiente número aleatorio usando el algoritmo LGC.
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        """
        Método mágico que sobrecarga la llamada a función.
        Permite reiniciar la secuencia con una nueva semilla.
        """
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números aleatorios basada en el algoritmo LGC.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        nueva_semilla = yield x
        if nueva_semilla is not None:
            x = nueva_semilla


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
