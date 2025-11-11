from common.insertdanhmuc import insert_danhmuc
while True:
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vào tên mô tả")
    insert_danhmuc(ten,mota)
    con=input("TIẾP TỤC y, THOÁT THIF NHẤN KÍ TỰ BẤT KÌ")
    if con!="y":
        break