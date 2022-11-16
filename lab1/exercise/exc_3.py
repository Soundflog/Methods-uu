import numpy as np
import lab1.lib.svm as svm
import scipy.io as sio

mat = sio.loadmat("dataset1.mat")

y = np.float64(mat["y"])
x = np.float64(mat["X"])

C = 10000

model = svm.svm_train(x, y, C, svm.linear_kernel, 0.001, 20)

svm.visualize_boundary_linear(x, y, model, "exc 3")