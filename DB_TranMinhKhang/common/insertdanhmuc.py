import sys
import os
from mysql.connector import Error

# 👉 Thêm thư mục gốc vào đường dẫn để import được ketnoidb
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ketnoidb.ketnoi_mql import connect_mysql


def insert_danhmuc(ten_danhmuc, mo_ta):
    """Thêm một danh mục mới vào bảng danhmuc"""
    print("🧠 Hàm insert_danhmuc đã được gọi!")  # Debug check

    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối đến cơ sở dữ liệu.")
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        values = (ten_danhmuc, mo_ta)

        print("🧾 SQL:", sql)          # Debug - hiển thị câu SQL
        print("📦 Values:", values)    # Debug - hiển thị dữ liệu

        cursor.execute(sql, values)
        connection.commit()

        print(f"✅ Đã thêm danh mục '{ten_danhmuc}' thành công! ID mới: {cursor.lastrowid}")

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối.")


# 👉 Khi chạy trực tiếp file này, hàm insert_danhmuc sẽ được gọi
if __name__ == "__main__":
    print("🚀 Bắt đầu thêm danh mục...")
    insert_danhmuc("Mỹ phẩm thiên thần", "Sản phẩm chăm sóc da từ thiên thần")
    print("🏁 Kết thúc chương trình.")
