import lab1.lib.svm as svm
import numpy as np
import scipy.io as sio

mat = sio.loadmat("dataset1.mat")

y = np.float64(mat["y"])
x = np.float64(mat["X"])
#coordinats x, y, , title
svm.visualize_boundary_linear(x, y, "", "exc 1")
