import psycopg2

conexion = psycopg2.connect(user='postgres', password='postgres',
                            host='localhost', port='5432', database='test_db_python')

try:
    with conexion:
        cursor: object
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            valores = (7,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
