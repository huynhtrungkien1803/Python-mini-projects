import sympy as sp

def solve_newton(equation, variable, initial_guess, tolerance, max_iterations):
    x = variable
    f = equation
    x_new = initial_guess
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)
    
    if f_double_prime != 0: # Loại trừ trường hợp f'(x) là một hằng số
        if abs(f_prime.evalf(subs={x: x_new})) == 0: # Loại trừ trường hợp f'(x0) == 0
            return float(x_new)  # Chuyển đổi kết quả sang số thực
        
        for i in range(max_iterations):
            f_prime = sp.diff(f, x)
            x_new = x_new - f.evalf(subs={x: x_new}) / f_prime.evalf(subs={x: x_new})
            
            if abs(f.evalf(subs={x: x_new})) < tolerance:
                return float(x_new)  # Chuyển đổi kết quả sang số thực

    else: # nếu f'(x) là một hằng số => không dùng evalf cho f'(x)
         if abs(f_prime) == 0: # Loại trừ trường hợp f'(x0) == 0
            return float(x_new)  # Chuyển đổi kết quả sang số thực
        
         for i in range(max_iterations):
            f_prime = sp.diff(f, x)
            x_new = x_new - f.evalf(subs={x: x_new}) / f_prime
            
            if abs(f.evalf(subs={x: x_new})) < tolerance:
                return float(x_new)  # Chuyển đổi kết quả sang số thực
    
    # Trả về None nếu không tìm được nghiệm trong số lần lặp tối đa

# Nhập hàm mục tiêu từ bàn phím
x = sp.symbols('x')
f_input = input('Nhập hàm mục tiêu f(x): ')
saiso = float(input('Nhập sai số cho phép: '))
loop = int(input('Nhập vòng lặp tối đa: '))
print('Nhập khoảng [a, b]')
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
f = sp.sympify(f_input)

# Tính đạo hàm của hàm số
df = sp.diff(f, x)

points_to_check = [a, b]
# Tìm các nghiệm của phương trình đạo hàm bằng 0
if (sp.diff(df, x) != 0): # Loại trừ trường hợp f''(x) == 0
    for i in range(a, b + 1):
        solve = solve_newton(df, x, i, saiso, loop)
        if (solve > a) and (solve < b):
            points_to_check.append(solve)

# Hàm chuyển đổi biểu thức sympy sang hàm số bình thường
f_lambdified = sp.lambdify(x, f, 'numpy')

# Tính giá trị của hàm tại các điểm quan trọng
values = []
for point in points_to_check:
    try:
        value = f_lambdified(float(point))
        values.append(value)
    except:
        continue

# Kiểm tra danh sách values có phần tử hợp lệ
if values:
    max_value = max(values)
    min_value = min(values)
    
    #Truy xuất x tại các điểm max min
    for i in range(len(values)):
        if values[i] == max_value:
            imax = i
            break
    for i in range(len(values)):
        if values[i] == min_value:
            imin = i
            break
    
    # Xuất kết quả
    print(f"Giá trị lớn nhất của hàm số trên đoạn [{a}, {b}] tại f({points_to_check[imax]}) là: {max_value}")
    print(f"Giá trị nhỏ nhất của hàm số trên đoạn [{a}, {b}] tại f({points_to_check[imin]}) là: {min_value}")
else:
    print("Không tìm thấy giá trị hợp lệ trong khoảng đã cho.")

