m1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
m3 = []
for i in range(len(m1)):
    m3.append(abs(m1[i] - m2[i]))

print(m3)
