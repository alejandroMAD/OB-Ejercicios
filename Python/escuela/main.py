from escuela.database import *
from escuela.alumno import Alumno
from escuela.examen import Examen


def main():

    crear_tabla_alumno()
    crear_tabla_examen()

    alumno1 = Alumno(1, 'Bart', 'Simpson')
    alumno2 = Alumno(2, 'Lisa', 'Simpson')
    alumno3 = Alumno(3, 'Jimbo', 'Jones')
    alumno4 = Alumno(4, 'Martin', 'Prince')
    alumno5 = Alumno(5, 'Milhouse', 'Van Houten')
    alumno6 = Alumno(6, 'Ralph', 'Wiggum')
    alumno7 = Alumno(7, 'Rod', 'Flanders')
    alumno8 = Alumno(8, 'Todd', 'Flanders')
    alumno9 = Alumno(9, 'Nelson', 'Muntz')
    alumno10 = Alumno(10, 'Jessica', 'Lovejoy')
    alumno11 = Alumno(11, 'Sherri', 'Mackleberry')
    alumno12 = Alumno(12, 'Terri', 'Mackleberry')
    alumno13 = Alumno(13, 'Wendell', 'Borton')
    alumno14 = Alumno(14, 'Üter', 'Zorker')
    alumno15 = Alumno(15, 'Janey', 'Powell')

    # Inserciones de objetos Alumno:
    insertar_alumno(alumno1)
    insertar_alumno(alumno2)
    insertar_alumno(alumno3)
    insertar_alumno(alumno4)
    insertar_alumno(alumno5)
    insertar_alumno(alumno6)
    insertar_alumno(alumno7)
    insertar_alumno(alumno8)
    insertar_alumno(alumno9)
    insertar_alumno(alumno10)
    insertar_alumno(alumno11)
    insertar_alumno(alumno12)
    insertar_alumno(alumno13)
    insertar_alumno(alumno14)
    insertar_alumno(alumno15)

    # Inserciones de objetos Examen instanciados "al vuelo":
    insertar_examen(Examen(1, 'Literatura', alumno1, 4))
    insertar_examen(Examen(2, 'Literatura', alumno2, 10))
    insertar_examen(Examen(3, 'Literatura', alumno3, 2))
    insertar_examen(Examen(4, 'Literatura', alumno4, 10))
    insertar_examen(Examen(5, 'Literatura', alumno5, 4))
    insertar_examen(Examen(6, 'Literatura', alumno6, 3))
    insertar_examen(Examen(7, 'Literatura', alumno7, 7))
    insertar_examen(Examen(8, 'Literatura', alumno8, 7))
    insertar_examen(Examen(9, 'Literatura', alumno10, 9))
    insertar_examen(Examen(10, 'Matemáticas', alumno1, 2))
    insertar_examen(Examen(11, 'Matemáticas', alumno2, 10))
    insertar_examen(Examen(12, 'Matemáticas', alumno4, 9))
    insertar_examen(Examen(13, 'Matemáticas', alumno5, 6))
    insertar_examen(Examen(14, 'Matemáticas', alumno7, 7))
    insertar_examen(Examen(15, 'Matemáticas', alumno8, 7))
    insertar_examen(Examen(16, 'Matemáticas', alumno11, 8))
    insertar_examen(Examen(17, 'Matemáticas', alumno12, 8))
    insertar_examen(Examen(18, 'Matemáticas', alumno15, 5))
    insertar_examen(Examen(19, 'Arte', alumno1, 4))
    insertar_examen(Examen(20, 'Arte', alumno2, 10))
    insertar_examen(Examen(21, 'Arte', alumno4, 7))
    insertar_examen(Examen(22, 'Arte', alumno5, 5))
    insertar_examen(Examen(23, 'Arte', alumno6, 5))
    insertar_examen(Examen(24, 'Arte', alumno10, 7))
    insertar_examen(Examen(25, 'Arte', alumno11, 6))
    insertar_examen(Examen(26, 'Arte', alumno12, 6))
    insertar_examen(Examen(27, 'Arte', alumno15, 9))

    # Búsqueda de alumnos con el apellido Simpson
    buscar_alumno('apellido', 'Simpson')
    # Búsqueda de alumnos cuyo nombre termine en -D
    buscar_alumno('nombre', '%d')
    # Búsqueda de un alumno que no existe en la base de datos
    buscar_alumno('nombre', 'Montgomery')

    # Muestra todos los exámenes de la asignatura de Arte
    buscar_examen('asignatura', 'Arte')

    # Prueba de adición y eliminación de un alumno
    insertar_alumno(Alumno(16, 'Maggie', 'Simpson'))
    eliminar_alumno(16)


if __name__ == '__main__':
    main()