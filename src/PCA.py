# setup thư viện
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# tạo hàm đọc dữ liệu từ tệp văn bản
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Chuyển đổi dòng thành danh sách các số thực
            row = list(map(float, line.strip().split(',')))
            data.append(row)
    return np.array(data)

# Đọc dữ liệu từ tệp pca.txt
data_file = 'pca.txt'
X = read_data(data_file)

# Chuẩn hóa dữ liệu (đưa dữ liệu vào biến dạng mảng X_scaled)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Quyết định số chiều của dữ liệu đầu ra
n_components = int(input('Nhập số chiều đầu ra (bé hơn số chiều đầu vào): '))

# Khởi tạo PCA và giảm chiều dữ liệu
pca = PCA(n_components)
X_pca = pca.fit_transform(X_scaled)

# In ra tỷ lệ phương sai
print(f"Tỷ lệ phương sai: {pca.explained_variance_ratio_}")

# Vẽ đồ thị nếu số chiều đầu ra là 2 và in ra các giá trị của dữ liệu sau khi giảm chiều
if n_components == 2:
    print("Đầu ra PCA:")
    print(X_pca)
    plt.scatter(X_pca[:, 0], X_pca[:, 1])
    plt.xlabel('Thành phần chính 1')
    plt.ylabel('Thành phần chính 2')
    plt.title('Đầu ra PCA')
    plt.show()
    
# Nếu số chiều đầu ra không phải là 2, chỉ in ra các giá trị của dữ liệu sau khi giảm chiều mà không vẽ đồ thị
else:
    print("Đầu ra PCA:")
    print(X_pca)