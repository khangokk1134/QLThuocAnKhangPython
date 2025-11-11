import sys
import os
from mysql.connector import Error

# ✅ Thêm đường dẫn để import module ketnoi_mql
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ketnoidb.ketnoi_mql import connect_mysql


def delete_danhmuc(id_danh_muc=None, ten_danh_muc=None):
    """Xóa danh mục theo id hoặc tên"""
    print("🧠 Hàm delete_danhmuc đã được gọi!")  # Debug log

    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối cơ sở dữ liệu.")
        return

    try:
        cursor = connection.cursor()

        # Kiểm tra đầu vào
        if id_danh_muc is not None:
            sql = "DELETE FROM danhmuc WHERE id = %s"
            values = (id_danh_muc,)
        elif ten_danh_muc is not None:
            sql = "DELETE FROM danhmuc WHERE ten_danhmuc = %s"
            values = (ten_danh_muc,)
        else:
            print("⚠️ Bạn cần truyền id_danh_muc hoặc ten_danh_muc để xóa.")
            return

        print("🧾 SQL:", sql)
        print("📦 Values:", values)

        cursor.execute(sql, values)
        connection.commit()

        if cursor.rowcount == 0:
            print("⚠️ Không tìm thấy danh mục phù hợp để xóa.")
        else:
            print("✅ Xóa thành công!")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối.")


# 👉 Thêm phần main để chạy trực tiếp file này
if __name__ == "__main__":
    print("🚀 Bắt đầu xóa danh mục...")
    # ✅ Bạn có thể chọn 1 trong 2 cách dưới đây để test:
    # delete_danhmuc(id_danh_muc=8)
    delete_danhmuc(ten_danh_muc="Mỹ phẩm thiên nhiên")
    print("🏁 Kết thúc chương trình.")
