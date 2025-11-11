
import logging
from mysql.connector import Error
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ketnoidb.ketnoi_mql import connect_mysql

# === Cấu hình logging ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # In ra màn hình
        logging.FileHandler("update_danhmuc.log", encoding="utf-8")  # Ghi log vào file
    ]
)

# === Đảm bảo Python tìm thấy module ketnoidb ===
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def update_danhmuc(id_danh_muc, ten_moi=None, mo_ta_moi=None, trang_thai_moi=None):
    """Cập nhật thông tin danh mục theo ID."""
    connection = connect_mysql()
    if connection is None:
        logging.warning("Không thể kết nối cơ sở dữ liệu.")
        return False

    try:
        cursor = connection.cursor()

        # Xây dựng câu lệnh UPDATE động
        updates, values = [], []

        if ten_moi is not None:
            updates.append("ten_danhmuc = %s")
            values.append(ten_moi)
        if mo_ta_moi is not None:
            updates.append("mo_ta = %s")
            values.append(mo_ta_moi)
        if trang_thai_moi is not None:
            updates.append("trang_thai = %s")
            values.append(trang_thai_moi)

        if not updates:
            logging.warning("Không có dữ liệu nào để cập nhật.")
            return False

        sql = f"UPDATE danhmuc SET {', '.join(updates)} WHERE id = %s"
        values.append(id_danh_muc)

        cursor.execute(sql, tuple(values))
        connection.commit()

        if cursor.rowcount == 0:
            logging.warning(f"Không tìm thấy danh mục có ID = {id_danh_muc}.")
            return False
        else:
            logging.info(f"Đã cập nhật danh mục ID = {id_danh_muc} thành công.")
            return True

    except Error as e:
        logging.error(f"Lỗi khi cập nhật danh mục: {e}")
        connection.rollback()
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logging.info("Đã đóng kết nối.")


# === Ví dụ chạy thử ===
if __name__ == "__main__":
    ok = update_danhmuc(
    id_danh_muc=5,
    ten_moi="Dược mỹ phẩm cập nhật",
    mo_ta_moi="Cập nhật thông tin năm 2025",
    trang_thai_moi=1
)


    if ok:
        print("✅ Cập nhật thành công.")
    else:
        print("⚠️ Cập nhật thất bại.")
