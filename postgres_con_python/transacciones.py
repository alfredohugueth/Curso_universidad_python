import psycopg2 as bd

conexion = bd.connect(user='postgres', password='postgres',
                      host='localhost', port='5432', database='test_db_python')

try:
    # No es comun, normalmente se utilizara el bloque with o el autocommit en false
    # conexion.autocommit = False # Se inicia la transaccion
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES( %s, %s, %s)'
            valores = ('Alex', 'Rojas123455412', 'arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s where id_persona=%s'
            valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()

print('Termina la transacción, se hizo commit')
