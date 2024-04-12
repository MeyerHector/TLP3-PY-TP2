import sys
import MySQLdb
def db_connect():
    try:
        db = MySQLdb.connect("localhost","root","","csv_python")
        print('Conexion establecida')
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)
    
    drop_table_sql = 'DROP TABLE IF EXISTS `csv_python`.`localidades`'
    try:
        cursor.execute(drop_table_sql)
        print('Tabla eliminada con éxito')
    except MySQLdb.Error as e:
        print("Error al eliminar la tabla: ",e)
    
    create_table_sql = 'CREATE TABLE `csv_python`.`localidades` (`provincia` VARCHAR(32) NOT NULL , `id` INT NOT NULL , `localidad` VARCHAR(64) NOT NULL , `cp` INT NOT NULL , `id_prov_mstr` INT NOT NULL)'
    try:
        cursor.execute(create_table_sql)
        print('Tabla creada con éxito')
    except MySQLdb.Error as e:
        print("Error en la creacion de la tabla: ",e)
    
    return cursor, db

