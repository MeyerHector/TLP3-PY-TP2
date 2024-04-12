
import MySQLdb
import csv
def insert_localities(cursor, db):
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