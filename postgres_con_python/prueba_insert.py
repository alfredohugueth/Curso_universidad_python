import psycopg2

conexion: None = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432', database='test_db_python')


try:
    with conexion:
        cursor: object
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            # valores = ('Carlos', 'Lara', 'clara@mail.com') #Insertar solo un registro
            valores = (
                ('Marcos', 'Cantu', 'mcantu@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
            )
            # cursor.execute(sentencia, valores) # Insertar solo un registro
            cursor.executemany(sentencia, valores) # Insertar varios registros
            # conexion.commit() # Guarda los cambios en la base de datos, no es necesario ya que estamos usando el with
            registros_intertados = cursor.rowcount
            print(f'Registros insertados: {registros_intertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
