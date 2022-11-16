import random as rnd

# print("Первое задание:")
# m1 = rnd.sample(range(0, 20), 5)
# m2 = rnd.sample(range(0, 20), 5)
# print(m1)
# print(m2)
# m3 = []
# for i in range(len(m1)):
#     m3.append(abs(m1[i] - m2[i]))
# print(m3)
#
# print("Четвёртое задание")
# mas_count = int(input("Введите кол-во массивов: "))
# mas_elem = int(input("Введите кол-во элементов массива: "))
# arrayA = []
# for i in range(mas_count):
#     arrayB = []
#     for i in range(mas_elem):
#         arrayB.append(rnd.randint(0, 100))
#     print(str(arrayB) + " - его сумма=" + str(sum(arrayB)))
#     if sum(arrayB) > sum(arrayA):
#         arrayA = arrayB
# print("Сумма элементов массива наибольшая:")
# print(arrayA)

print("Пятое задание")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(0, 0, 0)
ax.scatter(3, 3, 0)
plt.show()

point_1 = np.array((0, 0, 0))
point_2 = np.array((3, 3, 0))
square = np.square(point_1 - point_2)
sum_square = np.sum(square)
distance = np.sqrt(sum_square)
print(distance)

