import psycopg2

conexion = psycopg2.connect(user='postgres', password='postgres',
                            host='localhost', port='5432', database='test_db_python')

try:
    with conexion:
        cursor: object
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            # valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1) # Actualizar un registro
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2)
            )  # Actualizar varios registros
            # cursor.execute(sentencia, valores) # Actualizar solo un registro
            cursor.executemany(sentencia, valores) # Actualizar varios registros
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
