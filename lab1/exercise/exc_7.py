import scipy.io as sio
import numpy as np

import lab1.lib.svm as svm

data1 = sio.loadmat('dataset2.mat')
y1 = np.float64(data1['y'])
X1 = data1['X']

data2 = sio.loadmat('dataset3.mat')
Xval = data2['Xval']
yval = data2['yval']
y2 = np.float64(data2['y'])
X2 = data2['X']

C1 = 1.0
sigma1 = 0.1
gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma1)
gaussian.__name__ = svm.gaussian_kernel.__name__
model1 = svm.svm_train(X1, y1, C1, gaussian)
svm.visualize_boundary(X1, y1, model1)

svm.visualize_boundary_linear(X2, y2, None, title="exc_7_1")
svm.visualize_boundary_linear(Xval, yval, None, title="exc_7_2")