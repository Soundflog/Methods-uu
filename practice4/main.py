from recommendations import critics, sim_distance, sim_pearson, top_matches
import matplotlib.pyplot as plt


def print_plots(film1, film2):
    x = []
    y = []
    for key, value in critics.items():
        for key1, value1 in value.items():
            if key1 in film1:
                x.append(value1)
            elif key1 in film2:
                y.append(value1)

    if len(x) > len(y):
        x = x[:len(y)]
    else:
        y = y[:len(x)]

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel(f'оценки за {film1}')
    ax.set_ylabel(f'оценки за {film2}')
    plt.show()


if __name__ == '__main__':
    print_plots('Каникулы в Простоквашино', 'Зима в Простоквашино')

    print("\tЗадание 2 (sim_distance):")
    print("Метрика схожести Телёнок Гаврюша и Галчонок: ",
          sim_distance(critics, 'Телёнок Гаврюша', 'Галчонок'))
    print("Метрика схожести Кот Матроскин и Почтальон Печкин: ",
          sim_distance(critics, 'Кот Матроскин', 'Почтальон Печкин'))

    print("\tЗадание 3 (sim_pearson):")
    print("Метрика схожести Телёнок Гаврюша и Галчонок: ",
          sim_pearson(critics, 'Телёнок Гаврюша', 'Галчонок'))
    print("Метрика схожести Кот Матроскин и Почтальон Печкин: ",
          sim_pearson(critics, 'Кот Матроскин', 'Почтальон Печкин'))

    print("\tЗадание 4 (top_matches):")
    top_matches(critics, 'Кот Матроскин')
