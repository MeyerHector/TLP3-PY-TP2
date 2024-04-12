from src.db import db_connect
from src.utils.insert_localities import insert_localities
from src.utils.create_csv  import create_csv 
def main():
    cursor, db = db_connect()
    insert_localities(cursor, db)
    create_csv(cursor, db)
main()



    