# словарь критиков и их оценок для небольшого числа мультфильмов
import math
import numpy as np
import matplotlib.pyplot as plt

critics = {
    'Кот Матроскин': {
        'Зима в Простоквашино': 2.5,
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 3.0,
        'Винни-Пух': 3.5,
        'Ну, погоди!': 2.5,
        'Котёнок по имени Гав': 3.0
    },
    'Пёс Шарик': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 1.5,
        'Винни-Пух': 5.0,
        'Котёнок по имени Гав': 3.0,
        'Ну, погоди!': 3.5
    },
    'Почтальон Печкин': {
        'Зима в Простоквашино': 2.5,
        'Каникулы в Простоквашино': 3.0,
        'Винни-Пух': 3.5,
        'Котёнок по имени Гав': 4.0
    },
    'Корова Мурка': {
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 3.0,
        'Котёнок по имени Гав': 4.5,
        'Винни-Пух': 4.0,
        'Ну, погоди!': 2.5
    },
    'Телёнок Гаврюша': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 4.0,
        'Ёжик в тумане': 2.0,
        'Винни-Пух': 3.0,
        'Котёнок по имени Гав': 3.0,
        'Ну, погоди!': 2.0
    },
    'Галчонок': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 4.0,
        'Котёнок по имени Гав': 3.0,
        'Винни-Пух': 5.0,
        'Ну, погоди!': 3.5
    },
    'Дядя Фёдор': {
        'Каникулы в Простоквашино': 4.5,
        'Ну, погоди!': 1.0,
        'Винни-Пух': 4.0
    },
}


def sim_pearson(critics, first_critic_name, second_critic_name):
    first_crit_dict = critics[first_critic_name]
    second_crit_dict = critics[second_critic_name]
    X = []
    Y = []
    for key, value in first_crit_dict.items():
        for key1, value1 in second_crit_dict.items():
            if key == key1:
                X.append(value)
                Y.append(value1)
            else:
                pass

    sumXY = 0
    sumX = 0
    sumY = 0
    quadratic_sumX = 0
    quadratic_sumY = 0
    for i in range(len(X)):
        sumXY += X[i] * Y[i]
        sumX += X[i]
        sumY += Y[i]
        quadratic_sumX += X[i] ** 2
        quadratic_sumY += Y[i] ** 2

    # print(sumX)
    # print(sumY)
    # print(sumXY)
    P = (sumXY - sumX * sumY / len(X)) / math.sqrt(
        (quadratic_sumX - sumX ** 2 / len(X)) *
        (quadratic_sumY - sumY ** 2 / len(X))
    )
    # print(P)
    return P


def sim_distance(critics, first_critic_name, second_critic_name):
    first_crit_dict = critics[first_critic_name]
    second_crit_dict = critics[second_critic_name]
    c_1_i = []
    c_2_i = []
    for key, value in first_crit_dict.items():
        for key1, value1 in second_crit_dict.items():
            if key == key1:
                c_1_i.append(value)
                c_2_i.append(value1)
            else:
                pass

    quadratic_sum = 0
    for i in range(len(c_1_i)):
        quadratic_sum += (c_1_i[i] - c_2_i[i]) ** 2
    P = 1 / (1 + math.sqrt(quadratic_sum))
    return P


def top_matches(critics, critic_name):
    critics_coefs = {}
    for key in critics.keys():
        if critic_name != key:
            critics_coefs[key] = sim_pearson(critics, critic_name, key)

    critics_coefs = dict(sorted(critics_coefs.items(), key=lambda item: item[1]))
    critics_coefs = dict(critics_coefs.items().__reversed__())
    print(f"Метрика схожести (коэфф корр Пирсона) между критиком {critic_name} и всеми остальными:")
    for name, value in critics_coefs.items():
        print("{0} = {1}".format(name, value))
    coefficient_list = list(critics_coefs.items())
    best_user_name = coefficient_list[0][0]
    worst_user_name = coefficient_list[-1][0]
    print("\nНаиболее похожий пользователь: ", best_user_name)
    print("Наименее похожий пользователь: ", worst_user_name)
    plot_best_worst_users(critics, critic_name, best_user_name)
    plot_best_worst_users(critics, critic_name, worst_user_name)


def plot_best_worst_users(critics, critic_name, second_name):
    x = []
    y = []
    fig, ax = plt.subplots(1)
    for key1, value1 in critics[critic_name].items():
        for key2, value2 in critics[second_name].items():
            if key1 == key2:
                x.append(value1)
                y.append(value2)
                plt.annotate(key1, (value1, value2))
    ax.scatter(x, y)
    ax.set_xlabel(critic_name)
    ax.set_ylabel(second_name)
    a = np.polyfit(x, y, 1)
    b = np.poly1d(a)
    plt.plot(x, b(x), 'r')
    plt.grid()
    plt.show()
