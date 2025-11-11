import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ketnoidb.ketnoi_mql import connect_mysql
from mysql.connector import Error

def get_all_danhmuc(trang_thai=None):
    """Lấy danh sách tất cả danh mục (hoặc theo trạng thái nếu có)"""
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối cơ sở dữ liệu.")
        return

    try:
        cursor = connection.cursor(dictionary=True)  # Trả về dạng dict để dễ đọc

        # Câu SQL cơ bản
        sql = "SELECT * FROM danhmuc"
        params = ()

        # Nếu có trạng thái, lọc theo
        if trang_thai is not None:
            sql += " WHERE trang_thai = %s"
            params = (trang_thai,)

        cursor.execute(sql, params)
        result = cursor.fetchall()

        if len(result) == 0:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("📋 Danh sách danh mục:")
            for row in result:
                print(f"  ID: {row['id']} | Tên: {row['ten_danhmuc']} | Mô tả: {row['mo_ta']} | Trạng thái: {row['trang_thai']} | Ngày tạo: {row['ngay_tao']}")

        return result

    except Error as e:
        print("❌ Lỗi khi truy vấn danh mục:", e)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối.")

# 🧠 Gọi thử:
if __name__ == "__main__":
    # Lấy tất cả danh mục
    get_all_danhmuc()

    # Hoặc chỉ lấy danh mục đang hoạt động (trang_thai = 1)
    # get_all_danhmuc(trang_thai=1)
