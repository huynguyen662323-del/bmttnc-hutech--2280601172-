from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("***************MENU***************")
    print("**  1. Them sinh vien.           **")
    print("**  2. Cap nhat thong tin sinh vien boi ID. **")
    print("**  3. Xoa sinh vien boi ID.     **")
    print("**  4. Tim kiem sinh vien theo ten.        **")
    print("**  5. Sap xep sinh vien theo diem trung binh. **")
    print("**  6. Sap xep sinh vien theo ten chuyen nganh. **")
    print("**  7. Hien thi danh sach sinh vien.      **")
    print("**  0. Thoat.                  **")
    print("**********************************")

    key = int(input("Nhap tuy chon: "))

    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()

    elif (key == 2):
        print("\n2. Cap nhat thong tin sinh vien.")
        ID = int(input("Nhap ID sinh vien: "))
        qlsv.updateSinhVien(ID)

    elif (key == 3):
        print("\n3. Xoa sinh vien.")
        ID = int(input("Nhap ID sinh vien: "))
        if (qlsv.deleteByID(ID)):
            print("Da xoa sinh vien co ID = ", ID)
        else:
            print("Khong tim thay sinh vien co ID = ", ID)

    elif (key == 4):
        print("\n4. Tim kiem sinh vien theo ten.")
        name = input("Nhap ten sinh vien: ")
        listSV = qlsv.findByName(name)
        qlsv.showSinhVien(listSV)

    elif (key == 5):
        print("\n5. Sap xep sinh vien theo diem trung binh.")
        qlsv.sortByDiemTB()
        listSV = qlsv.getListSinhVien()
        qlsv.showSinhVien(listSV)

    elif (key == 6):
        print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
        qlsv.sortByName()
        listSV = qlsv.getListSinhVien()
        qlsv.showSinhVien(listSV)

    elif (key == 7):
        print("\n7. Hien thi danh sach sinh vien.")
        listSV = qlsv.getListSinhVien()
        qlsv.showSinhVien(listSV)

    elif (key == 0):
        print("\nThoat chuong trinh!")
        break

    else:
        print("Khong co chuc nang nay!")
        print("Hay chon chuc nang trong hop menu.")
