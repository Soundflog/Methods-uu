import numpy as np


def readData():
    df = np.matrix(np.loadtxt('var3.txt',
                              delimiter=' ',
                              skiprows=1,
                              dtype='str'))
    return df[:, 1:].astype(np.float64)


# Функция расчета стоимости заданного пути
def cost(arr: np.ndarray, data: np.matrix):
    res_cost = 0
    curr = int(arr[0])
    for i in arr.astype(int):
        res_cost += data[curr - 1, i - 1]
        curr = i
    res_cost += data[curr - 1, int(arr[0] - 1)]
    return res_cost


# Функция мутации
def mutation(arr: np.ndarray):
    i = np.random.choice(arr)
    j = np.random.choice(arr)
    while i == j:
        j = np.random.choice(arr)
    r = np.where(arr == i)
    arr[arr == j] = i
    arr[r] = j
    return arr


# Функция нахождения кратчайшего расстояния
def shortestDistance(arr1: np.ndarray, new_arr: np.ndarray, data: np.matrix):
    curr_index = np.where(new_arr == 0)[0][0]
    curr = int(new_arr[curr_index - 1])
    arri = np.where(arr1 == curr)[0][0]
    for i in range(1, new_arr.shape[0]):
        l_index = int(arr1[arri - i])
        r_index = int(arr1[(arri + i) % new_arr.shape[0]])
        if l_index in new_arr and r_index in new_arr:
            continue
        if l_index in new_arr and r_index not in new_arr:
            new_arr[curr_index] = r_index
            return new_arr
        if l_index not in new_arr and r_index in new_arr:
            new_arr[curr_index] = l_index
            return new_arr
        l_cost = data[curr - 1, l_index - 1]
        r_cost = data[curr - 1, r_index - 1]
        if l_cost > r_cost:
            new_arr[curr_index] = r_index
            return new_arr
        else:
            new_arr[curr_index] = l_index
            return new_arr
    return new_arr


# Функция кроссинговера
def cross(arr1: np.ndarray, arr2: np.ndarray, data: np.matrix):
    if arr1.shape[0] != arr2.shape[0]:
        return None
    new_arr = np.zeros(arr1.shape[0])
    j = np.random.choice(arr1)
    new_arr[0] = j
    for i in range(new_arr.shape[0] - 1):
        if i == 0 or i % 2 == 0:
            new_arr = shortestDistance(arr1, new_arr, data)
        else:
            new_arr = shortestDistance(arr2, new_arr, data)
    return new_arr


# Функция нахождения потомков для всех родителей
def solvePopulation(parents, data):
    tmp2 = []
    for j in range(parents.shape[0]):
        p1 = parents[j]
        for k in range(j + 1, parents.shape[0]):
            p2 = parents[k]
            child = cross(p1[0], p2[0], data)
            tmp2.append(child)
    return tmp2


# Функция поиска решения с помощью генетического алгоритма
def gen(data: np.matrix, parents_count, iterations, mut_chanel):
    n = data.shape[0]
    arr = np.zeros((parents_count, 2)).astype(np.ndarray)
    for i in range(parents_count):
        v = np.arange(1, n + 1)
        np.random.shuffle(v)
        arr[i, 0] = v
        arr[i, 1] = cost(v, data)
    tmp_parent = np.array(arr)
    for i in range(iterations):
        tmp2 = solvePopulation(tmp_parent, data)
        tmp = np.zeros((len(tmp2), 2)).astype(np.ndarray)
        for j in range(tmp.shape[0]):
            var = np.random.randint(0, 101)
            if var == mut_chanel * 100:
                tmp2[j] = mutation(tmp2[j])
            tmp[j, 0] = tmp2[j]
            tmp[j, 1] = cost(tmp2[j], data)
        tmp = tmp[np.argsort(tmp[:, 1])]
        tmp_parent = tmp[0:n + 1, :]
    return tmp_parent


if __name__ == "__main__":
    input_data = readData()
    print(input_data)
    res = gen(input_data, 100, 500, 0.1)
    print(res)
    print("\nДлина оптимального пути: " + str(res[0, 1]))
