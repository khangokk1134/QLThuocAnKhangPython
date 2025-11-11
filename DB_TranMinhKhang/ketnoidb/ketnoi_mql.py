import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',     # Mật khẩu mới bạn vừa đặt
            database='quanlithuocankhang',
            port=3307
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None


connect_mysql()
