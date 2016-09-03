import json
import socket
import MySQLdb
from time import sleep
from threading import Thread


HOST = ''
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def get_data(db, last_id=0):
    c = db.cursor()
    c.execute("""select * from vendas_empresa where id > %s order by id asc limit 50""" % last_id)
    return dictfetchall(c)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


def get_database_connection():
    return MySQLdb.connect(host='localhost', user='root', db='representante')


def listen(conn):
    db = get_database_connection()
    streaming_data = get_data(db)

    while streaming_data:
        for data in streaming_data:
            conn.sendall(json.dumps(data, default=date_handler))
            sleep(1)
        streaming_data = get_data(db, data['id'])

    conn.close()


while True:
    conn, addr = s.accept()
    print 'Connected by', addr

    listen_thread = Thread(target=listen, args=(conn,))
    listen_thread.start()
