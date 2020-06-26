import mysql.connector
import struct
import heartpy as hp
import numpy as np
from matplotlib import pyplot as plt

from mysql.connector import Error
from mysql.connector import connection
try:
    conn = connection.MySQLConnection(host='localhost',
                        database='heartbug',
                        user='root',
                        password='TigerBarb51$')

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select episodes.ECG from episodes where Episode_ID = 1747092 limit 1;")
        record = cursor.fetchone()
        count = len(record[0])
        result = struct.unpack("c"*count, record[0])
        data = np.array([int.from_bytes(i, "big", signed=True) for i in result])
        plt.plot(data)
        plt.show()
        wd, m = hp.process(data, 200)        
        plot_object = hp.plotter(wd, m, show=False, title='some awesome title')
        plot_object.show()
except Error as e:
     print("Error", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
