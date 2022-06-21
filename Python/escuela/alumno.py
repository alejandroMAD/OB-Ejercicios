class Alumno:

    def __init__(self, identificador, nombre, apellido):
        self._identificador = identificador
        self._nombre = nombre
        self._apellido = apellido

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, identificador):
        self._identificador = identificador

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._nombre = apellido

    def __str__(self):
        return f'[ALUMNO] ID: {self._identificador} ' \
               f'NOMBRE: {self._nombre} ' \
               f'APELLIDO: {self._apellido}'
