import csv
from src.db import db_connect
import MySQLdb
from src.utils.create_csv  import create_csv 
def main():
    cursor, db = db_connect()
    with open('./src/data/localidades.csv', mode='r', encoding='utf-8', newline='\n') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        try:
            for provincia in lector_csv:
                sql = '''INSERT INTO `localidades`(`provincia`, `id`, `localidad`, `cp`, `id_prov_mstr`) 
                        VALUES (%s, %s, %s, %s, %s)'''
                values = (provincia['provincia'], provincia['id'], provincia['localidad'], provincia['cp'], provincia['id_prov_mstr'])
                cursor.execute(sql, values)
            db.commit()
            print('Localidades insertadas correctamente')
        except MySQLdb.error as e:
            print('Error en la consulta: ', e)

    create_csv(cursor, db)
main()



    