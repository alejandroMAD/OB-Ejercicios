import sqlite3
from escuela.alumno import Alumno


def crear_tabla_alumno():
    """Creación de la tabla alumnos en la database escuela (SQLite3)"""
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE alumnos (
        id INTEGER PRIMARY KEY, 
        nombre TEXT, 
        apellido TEXT
        )
    """)

    cursor.close()
    conn.close()


def crear_tabla_examen():
    """Creación de la tabla examenes en la database escuela (SQLite3)"""
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE examenes (
        id INTEGER PRIMARY KEY, 
        asignatura TEXT,
        alumno INTEGER NOT NULL,
        nota INTEGER,
        FOREIGN KEY (alumno) REFERENCES alumnos(id)
        )
    """)

    cursor.close()
    conn.close()


def insertar_alumno(alumno):
    """Añade un nuevo registro a la tabla alumnos de escuela.db"""
    conn = sqlite3.connect('escuela.db')
    try:
        cursor = conn.cursor()
        rows = cursor.execute(
            f'INSERT INTO alumnos (id, nombre, apellido) '
            f'VALUES(?, ?, ?)',
            (alumno.identificador, alumno.nombre, alumno.apellido)
        )
        conn.commit()
        cursor.close()
        print(f'Alumno con ID: {alumno.identificador} registrado con éxito')
    except sqlite3.Error as err:
        print(f'ERROR en la inserción de {alumno}:\n\t {err.args[0]}')
    finally:
        conn.close()


def insertar_examen(examen):
    """Añade un nuevo registro a la tabla examenes de escuela.db"""
    conn = sqlite3.connect('escuela.db')
    try:
        cursor = conn.cursor()
        rows = cursor.execute(
            f'INSERT INTO examenes (id, asignatura, alumno, nota) '
            f'VALUES(?, ?, ?, ?)',
            (examen.identificador,
             examen.asignatura,
             examen.alumno.identificador,
             examen.nota)
        )
        conn.commit()
        cursor.close()
        print(f'Examen con ID: {examen.identificador} registrado con éxito')
    except sqlite3.Error as err:
        print(f'ERROR en la inserción de {examen}:\n\t {err.args[0]}')
    conn.close()


def buscar_alumno(criterio, patron):
    """Busca un alumno en la base de datos escuela.db
    por el campo pasado como criterio y patrón del segundo argumento"""
    conn = sqlite3.connect('escuela.db')
    try:
        cursor = conn.cursor()
        rows = cursor.execute(
            f'SELECT id, nombre, apellido FROM alumnos '
            f'WHERE {criterio} LIKE "{patron}"'
        )
        data = rows.fetchall()
        cursor.close()
        if len(data) > 0:
            for alumno in range(len(data)):
                print('encontrado ->', Alumno(data[alumno][0], data[alumno][1], data[alumno][2]))
        else:
            print(f'No se ha encontrado a "{patron}" por [{criterio}] en la base de datos')
    except sqlite3.Error as err:
        print(f'ERROR en la búsqueda de {patron} por {criterio}:\n\t {err.args[0]}')
    finally:
        conn.close()


def buscar_examen(criterio, patron):
    """Busca un examen en la base de datos escuela.db
    por el campo pasado como criterio y patrón del segundo argumento"""
    conn = sqlite3.connect('escuela.db')
    try:
        cursor = conn.cursor()
        rows = cursor.execute(
            f'SELECT id, asignatura, alumno, nota FROM examenes '
            f'WHERE {criterio} LIKE "{patron}"'
        )
        data = rows.fetchall()
        cursor.close()
        if len(data) > 0:
            for examen in range(len(data)):
                print('encontrado ->', data[examen])
        else:
            print(f'No se ha encontrado "{patron}" por [{criterio}] en la base de datos')
    except sqlite3.Error as err:
        print(f'ERROR en la búsqueda de {patron} por {criterio}:\n\t {err.args[0]}')
    finally:
        conn.close()


def eliminar_alumno(identificador):
    """Elimina un registro de la tabla alumnos por su id"""
    conn = sqlite3.connect('escuela.db')
    try:
        cursor = conn.cursor()
        rows = cursor.execute(
            'DELETE FROM alumnos WHERE id = ?', (identificador,)
        )
        conn.commit()
        cursor.close()
        print(f'Alumno con ID: {identificador} eliminado con éxito')
    except sqlite3.Error as err:
        print(f'ERROR en la eliminación del alumno con ID {identificador}:\n\t {err.args[0]}')
    conn.close()


def eliminar_examen(identificador):
    """Elimina un registro de la tabla examenes por su id"""
    conn = sqlite3.connect('escuela.db')
    try:
        cursor = conn.cursor()
        rows = cursor.execute(
            'DELETE FROM examenes WHERE id = ?', (identificador,)
        )
        conn.commit()
        cursor.close()
        print(f'Examen con ID: {identificador} eliminado con éxito')
    except sqlite3.Error as err:
        print(f'ERROR en la eliminación del examen con ID {identificador}:\n\t {err.args[0]}')
    conn.close()
