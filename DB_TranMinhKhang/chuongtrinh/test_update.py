
from common.update_danhmuc import update_danhmuc

while True:
    id = input("Id danh mục")
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vào tên mô tả")
    update_danhmuc(id,ten,mota)
    con=input("TIẾP TỤC y, THOÁT THÌ NHẤN KÍ TỰ BẤT KÌ")
    if con!="y":
        break