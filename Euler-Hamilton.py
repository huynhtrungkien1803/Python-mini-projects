def is_valid_Euler(u, v, graph):
    # Kiểm tra xem có cạnh nối u và v hay không
    return graph[u][v] > 0

def eulerian_cycle(graph):
    # Tìm đỉnh xuất phát, bắt đầu từ đỉnh có bậc khác 0
    start_vertex = 0
    for i in range(len(graph)):
        if sum(graph[i]) % 2 != 0:
            start_vertex = i
            break

    # Stack để lưu chu trình
    stack = [start_vertex]
    euler_circuit = []

    while stack:
        current_vertex = stack[-1]

        # Tìm đỉnh kề đầu tiên của đỉnh hiện tại
        for next_vertex in range(len(graph[current_vertex])):
            if is_valid_Euler(current_vertex, next_vertex, graph):
                # Đánh dấu cạnh đã đi qua
                graph[current_vertex][next_vertex] -= 1
                graph[next_vertex][current_vertex] -= 1

                # Thêm đỉnh kề vào chu trình và đẩy vào stack
                stack.append(next_vertex)
                break

        # Nếu không tìm thấy đỉnh kề, pop đỉnh hiện tại ra khỏi stack và thêm vào chu trình
        if current_vertex == stack[-1]:
            stack.pop()
            euler_circuit.append(current_vertex)

    return euler_circuit


def is_valid_Hamilton(v, pos, path, graph):  #nhận diện đường đi Hamilton   
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True


def hamiltonian_cycle_util(graph, path, pos): #thử tất cả đường đi   
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        return False

    for v in range(1, len(graph)):
        if is_valid_Hamilton(v, pos, path, graph):
            path[pos] = v

            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True

            path[pos] = -1

    return False


def hamiltonian_cycle(graph): #xử lý dữ liệu
    path = [-1] * len(graph)
    path[0] = 0

    if not hamiltonian_cycle_util(graph, path, 1):
        print("- Không tìm thấy chu trình Hamilton.")
        return False
    
    
    print("- Chu trình Hamilton: ", end='')
    
    print(path[0] + 1, end=' ') 
    for i in reversed(range(0, len(path))):
        print(path[i] + 1, end=' ')
    print()

    return True
   
#MAIN:

n = int(input("Nhập số đỉnh: "))

a = []

tong=0

for i in range(0, n): #nhập ma trận
    row = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
    a.append(row)
    
print('-----------------KẾT QUẢ--------------------')

hamiltonian_cycle(a)

a = eulerian_cycle(a)
if (len(a) <= 1) or (a[0] != a[len(a)-1]): #chuẩn hóa đầu ra
    print('- Không tìm thấy chu trình Euler.')
else:
    print('- Chu Trình Euler:', end=' ')
    for i in range(0, len(a)):
        print(a[i] + 1, end=' ')
    print()

 


