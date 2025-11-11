# ---------------------------
# 🟢 THÊM DANH MỤC
# ---------------------------

import tkinter as tk
from tkinter import ttk, messagebox

from mysql.connector import Error
import sys
import os

# Thêm thư mục cha (DB_TranMinhKhang) vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ketnoidb.ketnoi_mql import connect_mysql


def them_danhmuc(tk=None):
    ten = entry_ten.get()
    mota = entry_mota.get()

    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục")
        return

    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        cursor.execute(sql, (ten, mota))
        conn.commit()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
        hien_thi_danhmuc()
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ---------------------------
# 🟡 CẬP NHẬT DANH MỤC
# ---------------------------
def capnhat_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn 1 danh mục để sửa.")
        return

    item = tree.item(selected)
    id_danhmuc = item["values"][0]
    ten = entry_ten.get()
    mota = entry_mota.get()

    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục mới")
        return

    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET ten_danhmuc = %s, mo_ta = %s WHERE id = %s"
        cursor.execute(sql, (ten, mota, id_danhmuc))
        conn.commit()
        messagebox.showinfo("Cập nhật", "Đã cập nhật danh mục.")
        hien_thi_danhmuc()
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ---------------------------
# 🔴 XÓA DANH MỤC
# ---------------------------
def xoa_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn danh mục để xóa.")
        return

    item = tree.item(selected)
    id_danhmuc = item["values"][0]

    if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa danh mục này?"):
        return

    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (id_danhmuc,))
        conn.commit()
        messagebox.showinfo("Đã xóa", "Danh mục đã bị xóa.")
        hien_thi_danhmuc()
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ---------------------------
# 🔵 HIỂN THỊ DANH MỤC
# ---------------------------
def hien_thi_danhmuc():
    for row in tree.get_children():
        tree.delete(row)

    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM danhmuc ORDER BY id DESC")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi hiển thị: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ---------------------------
# 🖱️ CHỌN DÒNG TRONG BẢNG
# ---------------------------
def chon_dong(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected)
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, item["values"][1])
        entry_mota.insert(0, item["values"][2])

# ---------------------------
# 🪟 GIAO DIỆN CHÍNH
# ---------------------------
root = tk.Tk()
root.title("Quản lý Danh Mục")
root.geometry("700x500")

frame_top = tk.Frame(root, pady=10)
frame_top.pack()

tk.Label(frame_top, text="Tên danh mục:").grid(row=0, column=0, padx=5)
entry_ten = tk.Entry(frame_top, width=30)
entry_ten.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Mô tả:").grid(row=1, column=0, padx=5)
entry_mota = tk.Entry(frame_top, width=30)
entry_mota.grid(row=1, column=1, padx=5)

frame_btn = tk.Frame(root, pady=10)
frame_btn.pack()

tk.Button(frame_btn, text="Thêm", width=10, bg="#4CAF50", fg="white", command=them_danhmuc).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Sửa", width=10, bg="#FFC107", command=capnhat_danhmuc).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Xóa", width=10, bg="#F44336", fg="white", command=xoa_danhmuc).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="Hiển thị", width=10, command=hien_thi_danhmuc).grid(row=0, column=3, padx=5)

columns = ("ID", "Tên danh mục", "Mô tả")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
tree.heading("ID", text="ID")
tree.heading("Tên danh mục", text="Tên danh mục")
tree.heading("Mô tả", text="Mô tả")

tree.pack(fill=tk.BOTH, expand=True, pady=10)
tree.bind("<<TreeviewSelect>>", chon_dong)

hien_thi_danhmuc()
root.mainloop()