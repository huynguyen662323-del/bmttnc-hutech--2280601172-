# Hàm đếm số lần xuất hiện
def dem_so_lan_xuat_hien(lst):
    count_dict = {}          # tạo dictionary rỗng để lưu kết quả
    for item in lst:         # duyệt từng phần tử trong list
        if item in count_dict:   # nếu đã có trong dict
            count_dict[item] += 1  # tăng số lần lên 1
        else:
            count_dict[item] = 1   # nếu chưa có thì gán = 1
    return count_dict          # trả về dict kết quả

# Nhập danh sách từ người dùng
input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")

# Tách chuỗi thành list (mỗi từ là 1 phần tử)
word_list = input_string.split()

# Sử dụng hàm và in kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử:", so_lan_xuat_hien)
