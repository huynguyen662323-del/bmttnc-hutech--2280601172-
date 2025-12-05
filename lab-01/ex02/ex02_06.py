# Nhập chuỗi X, Y từ người dùng (ví dụ: 3,5)
input_str = input("Nhập X, Y: ")

# Tách chuỗi theo dấu phẩy, đổi từng phần thành số nguyên
dimensions = [int(x) for x in input_str.split(',')]

# Số hàng và số cột
rowNum = dimensions[0]
colNum = dimensions[1]

# Tạo mảng 2 chiều ban đầu, toàn 0
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# Gán giá trị i*j cho từng phần tử
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

# In kết quả
print(multilist)
