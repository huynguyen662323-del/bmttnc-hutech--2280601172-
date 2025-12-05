# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    # Các số <= 1 không phải số nguyên tố
    if n <= 1:
        return False

    # Chỉ cần kiểm tra ước từ 2 đến căn bậc hai của n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:      # nếu chia hết cho i -> không phải số nguyên tố
            return False

    # Nếu không tìm được ước nào -> là số nguyên tố
    return True


# Nhập số và kiểm tra
number = int(input("Nhập vào số cần kiểm tra: "))

if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")
