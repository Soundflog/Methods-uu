from collections import OrderedDict
import numpy as np
import scipy.io as sp
from sklearn.svm import SVC
import process_email as pe


def zan_1():
    print("zan1")
    with open('email.txt', 'r') as file:
        email = file.read().replace('\n', '')
    print(email)
    return email


def zan_2(email):
    print("zan2")
    arr = pe.process_email(email)
    print(arr)
    return arr


def zan_3(arr):
    print("zan3")
    features = pe.email_features(arr)
    print("Длина вектора признаков: ", len(features))
    print('Кол-во ненулевых результатов: ', sum(features > 0))


def zan_4():
    print("zadan 4")
    data = sp.loadmat('train.mat')
    X = data['X']
    y = data['y'].flatten()
    clf = SVC(C=0.1, kernel='linear', tol=1e-3)
    model = clf.fit(X, y)
    p = model.predict(X)
    summa = sum(p == y)
    print('Сумма: ', summa)
    accuracy = np.mean(summa) / len(y) * 100
    print('Точность: ', accuracy)
    return model


def zan_5(model):
    print("zadan 5")
    test = sp.loadmat('test.mat')
    Xtest = test['Xtest']
    ytest = test['ytest'].flatten()
    p = model.predict(Xtest)
    summa = sum(p == ytest)
    print('Сумма: ', summa)
    accuracy = np.mean(summa) / len(ytest) * 100
    print('Точность: ', accuracy)


def zan_6(model):
    print("zadan 6")
    t = sorted(list(enumerate(model.coef_[0])),
               key=lambda e: e[1], reverse=True)
    d = OrderedDict(t)
    idx = list(d.keys())
    weight = list(d.values())
    dictionary = pe.get_dictionary()
    print('Топ-15 слов в письмах со спамом: ')
    for i in range(15):
        print(' %-15s (%f)' % (dictionary[idx[i]], weight[i]))


if __name__ == '__main__':
    emails = zan_1()
    nulls = zan_2(emails)
    zan_3(nulls)
    models = zan_4()
    zan_5(models)
    zan_6(models)
