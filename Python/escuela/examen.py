from alumno import Alumno


class Examen:

    def __init__(self, identificador, asignatura, alumno, nota):
        self._identificador = identificador
        self._asignatura = asignatura
        self._alumno = alumno
        self._nota = nota

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, identificador):
        self._identificador = identificador

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, asignatura):
        self._asignatura = asignatura

    @property
    def alumno(self):
        return self._alumno

    @alumno.setter
    def alumno(self, alumno):
        self._alumno = alumno

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def __str__(self):
        return f'[EXAMEN] ID: {self._identificador} ' \
               f'ASIGNATURA: {self._asignatura} ' \
               f'ALUMNO: {self._alumno.nombre, self._alumno.apellido} ' \
               f'NOTA: {self._nota}'
