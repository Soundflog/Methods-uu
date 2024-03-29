from matplotlib import rc, pyplot as plt
import plots as myplots
import numpy as np


# Функция загрузки данных из файла
def loadData(file: str):
    data = np.matrix(np.loadtxt(file, delimiter=','))
    return data[:, 0:-1], data[:, -1]


# Функция нормализации данных
def normalize(norm_data: np.matrix):
    tmp = np.zeros((norm_data.shape[1], 2))
    tmp[:, 0] = np.mean(norm_data, axis=0)
    tmp[:, 1] = np.std(norm_data, axis=0)
    norm_data -= tmp[:, 0]
    norm_data /= tmp[:, 1]
    return norm_data, tmp


# Функция предсказания
def findResult(X_res: np.matrix,
               theta_res, data_norm=np.matrix([0])):
    if X_res.shape[1] >= theta_res.shape[0]:
        return None
    y_res = theta_res[0, 0]
    if data_norm.shape == (1, 1):
        for i in range(X_res.shape[1]):
            y_res += theta_res[i + 1, 0] * X_res[0, i]
        return y_res
    x_res_tmp = X_res.copy()
    for i in range(x_res_tmp.shape[1]):
        x_res_tmp[0, i] -= data_norm[i, 0]
        x_res_tmp[0, i] /= data_norm[i, 1]
    for i in range(X_res.shape[1]):
        y_res += theta_res[i + 1, 0] * x_res_tmp[0, i]
    y_res *= data_norm[-1, 1]
    y_res += data_norm[-1, 0]
    return y_res


# Функция вычисления стоимости
def computeCost(X_cost: np.matrix, y_cost: np.matrix,
                theta_cost: np.matrix):
    m = X_cost.shape[0]
    h_x = X_cost * theta_cost
    cost = (1 / (2 * m) * np.power(h_x - y_cost, 2)).sum()
    return cost


# Метод наименьших квадратов
def leastSquare(X: np.matrix, y: np.matrix):
    X_ones = np.c_[np.ones((X.shape[0], 1)), X]
    return np.dot(np.linalg.pinv(
        np.dot(X_ones.T, X_ones)),
        np.dot(X_ones.T, y))


# Функция градиентного спуска
def gradient_descent(X_grad: np.matrix, y_grad: np.matrix,
                     alpha: float, iterations: int):
    m, n = X_grad.shape
    theta_grad = np.ones((n, 1))
    theta_grad[0, 0] = 0
    j_theta = np.zeros((iterations, 1))
    temp_theta = theta_grad
    for i in range(iterations):
        theta_grad = temp_theta.copy()
        j_theta[i] = computeCost(X_grad, y_grad, theta_grad)
        temp_theta = theta_grad - alpha * (1 / m) * \
                     np.dot(X_grad.T, X_grad * theta_grad - y_grad)
    return j_theta, theta_grad


# Одномерная линейная регрессия
def oneRegress():
    X, y = loadData('ex1data1.txt')
    myplots.plotTask2()
    X_ones = np.c_[np.ones((X.shape[0], 1)), X]
    theta = np.matrix('[1; 2]')
    r, t = gradient_descent(X_ones, y, 0.02, 500)
    print("'theta' найденная градиентным спуском: " + str(t).replace("\n", ""))
    myplots.plotErrors(r)
    myplots.plotTask6(X, y, t)


# Многомерная линейная регрессия для двух квартир
def twoRegress():
    data2 = loadData('ex1data2.txt')
    norm_data, norm = normalize(np.c_[data2[0], data2[1]])
    X2, y2 = norm_data[:, 0:-1], norm_data[:, -1]
    X_ones2 = np.c_[np.ones((X2.shape[0], 1)), X2]
    r2, t2 = gradient_descent(X_ones2, y2, 0.02, 500)
    last = leastSquare(data2[0], data2[1])

    quartile_area1 = input("Введите площадь квартиры для первого рассчета: ")
    number_of_rooms1 = input("Введите количество комнат для первого рассчета: ")

    quartile_area2 = input("Введите площадь квартиры для второго рассчета: ")
    number_of_rooms2 = input("Введите количество комнат для второго рассчета: ")

    print(
        "Приблезительная стоимость квартиры с площадью"
        " {} и {} комнатой(ами): {} МНК и {} градиентный спуск".format(
            str(quartile_area1),
            str(number_of_rooms1),
            str(findResult(
                np.matrix([quartile_area1, number_of_rooms1],
                          dtype=np.float), last)),
            str(
                findResult(
                    np.matrix([quartile_area1, number_of_rooms1],
                              dtype=np.float), t2, norm))))
    print(
        "Приблезительная стоимость квартиры с площадью"
        " {} и {} комнатой(ами): {} МНК и {} градиентный спуск".format(
            str(quartile_area2),
            str(number_of_rooms2),
            str(findResult(
                np.matrix([quartile_area2, number_of_rooms2],
                          dtype=np.float), last)),
            str(findResult(
                np.matrix([quartile_area2, number_of_rooms2],
                          dtype=np.float), t2, norm))))


def kursach(n, T):
    x = 1
    y_n = [0, 0, 0]
    x_n = [0, T * 1, T * 2]
    n = int(n / T)
    for i in range(3, n):
        if i < 3:
            x = 0
        else:
            x = 1
        # (-(40 * T - 15) * y_n[i - 1] - \
        #                     (15 - 80 * T + 35 * pow(T, 2)) * y_n[i - 2] - \
        #                     (32 * pow(T, 3) - 35 * pow(T, 2) + 40 * T - 5) * y_n[i - 3] + \
        #                     (32 * pow(T, 3)) * x) / 5
        y_n.append((-(439 * T - 150) * y_n[i - 1] - \
                    (150 - 878 * T + 700 * pow(T, 2)) * y_n[i - 2] - \
                    (1300 * pow(T, 3) - 700 * pow(T, 2) + 439*T - 50) * y_n[i - 3] + \
                    (1300 * pow(T, 3)) * x) / 50)
        x_n.append(T * i)

    return x_n, y_n


def plotKursach(X, y):
    plt.plot(x, y)
    plt.xlabel('T')
    plt.ylabel('Y')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    font = {'family': 'Verdana', 'weight': 'normal'}
    rc('font', **font)
    # Вызов функций
    # oneRegress()
    # twoRegress()
    x, y_n = kursach(10, 0.01)
    print("--y_n--\n", y_n)
    print("------X-------\n", x)
    plotKursach(x, y_n)
