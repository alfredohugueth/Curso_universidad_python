# DAO - Data Access Object
from Persona import Persona
from conexion import Conexion
from looger_base import log


class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s, WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        try:
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cursor:
                    cursor.execute(cls._SELECCIONAR)
                    registros = cursor.fetchall()
                    personas = []
                    for registro in registros:
                        persona = Persona(registro[0], registro[2], registro[3])
                        personas.append(persona)
                    return personas
        except Exception as e:
            print(f'Ocurrio un error al seleccionar: {e}')


    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertar: {persona}')
                return cursor.rowcount


# ---------------------- Testing -----------------------

if __name__ == '__main__':
    # Insertar un registro:

    persona_1 = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona_1)
    log.debug(f'Personas Insertadas: {personas_insertadas}')

    # Seleccionar un registro

    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
