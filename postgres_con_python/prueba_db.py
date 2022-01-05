import psycopg2

conexion = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db_python')


try:
    with conexion:
        cursor: object
        with conexion.cursor() as cursor:
            sentencia: str = 'SELECT * FROM persona WHERE id_persona IN %s' # %s es una variable posicional
            # llaves_primarias = ((1,2,3),)
            # id_persona = input('Proporciona el valor de id_persona: ')
            entrada = input('Proporciona los ids a buscar separado por comas: ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall() # Fetch all, trae todos los registros, fetchone trae solo uno
            for registro in registros:
                print(registro)  # Los registros obtenidos son tuples
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
