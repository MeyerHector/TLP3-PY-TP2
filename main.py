import csv
from src.db import db_connect
import MySQLdb
from src.utils.create_csv  import create_csv 
def main():
    cursor, db = db_connect()
    with open('./src/data/localidades.csv', mode='r', encoding='utf-8', newline='\n') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        try:
            sql = '''INSERT INTO `localidades`(`provincia`, `id`, `localidad`, `cp`, `id_prov_mstr`) 
                        VALUES (%s, %s, %s, %s, %s)'''    
            cursor.executemany(sql, lector_csv)
            db.commit()
            print('Localidades insertadas correctamente')
        except MySQLdb.error as e:
            print('Error en la consulta: ', e)

    create_csv(cursor, db)
main()



    