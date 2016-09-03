import json
from socket import *
import MySQLdb
from time import sleep
from threading import Thread


HOST = ''
PORT = 8080
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)


available_models = ['products', 'customers']


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def get_data(db, model_to_sync, last_id=0):
    c = db.cursor()
    c.execute("""select * from {0} where id > {1} order by id asc limit 5""".format(model_to_sync, last_id))
    return dictfetchall(c)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else str(obj)


def get_database_connection():
    return MySQLdb.connect(host='localhost', user='root', db='streaming_test')


def listen(conn, model_to_sync):
    db = get_database_connection()
    streaming_data = get_data(db, model_to_sync)

    while streaming_data:
        for data in streaming_data:
            conn.sendall(json.dumps(data, default=date_handler))
            sleep(1)
        streaming_data = get_data(db, model_to_sync, data['id'])

    conn.close()


while True:
    conn, addr = s.accept()
    print 'Connected by', addr

    model_to_sync = conn.recv(1024)

    if model_to_sync in available_models:
        listen_thread = Thread(target=listen, args=(conn, model_to_sync))
        listen_thread.start()
    else:
        conn.send('Available models: products, customers')
        conn.close()
