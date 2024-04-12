import csv
import pathlib

def create_csv(cursor, db):
    sql = 'SELECT DISTINCT `provincia` FROM `localidades`'
    cursor.execute(sql)
    provincias = cursor.fetchall()
    provincias = [tupla[0] for tupla in provincias] 
    for i in range(len(provincias)):
        provincias[i] = provincias[i].replace(' ', '_')
    try:
        for provincia in provincias:
            sql = 'SELECT `id`, `localidad`, `cp`, `id_prov_mstr` FROM `localidades` WHERE provincia = %s'
            cursor.execute(sql, (provincia.replace('_', ' '),))
            data = cursor.fetchall()
            archivo =  f'{provincia}.csv'
            arc = pathlib.Path(__file__).parent.parent.joinpath("data", archivo)

            with open(arc, mode='w', encoding='utf-8', newline='\n') as archivo_csv:
                writer_csv = csv.writer(archivo_csv)
                writer_csv.writerow(['provincia', 'id', 'localidad', 'cp', 'id_prov_mstr'])
                writer_csv.writerows(data)
            print(f'Archivo {archivo} creado correctamente')
    except db.Error as e:
        print('Error en la consulta: ', e)