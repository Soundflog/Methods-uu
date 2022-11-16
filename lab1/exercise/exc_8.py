import lab1.lib.svm as svm
import scipy.io as sio
import numpy as np

data2 = sio.loadmat('dataset3.mat')
Xval = data2['Xval']
yval = data2['yval']
y2 = np.float64(data2['y'])
X2 = data2['X']

C2 = 1.0
sigma2 = 0.5
gaussian1 = svm.partial(svm.gaussian_kernel, sigma=sigma2)
gaussian1.__name__ = svm.gaussian_kernel.__name__
model2 = svm.svm_train(X2, y2, C2, gaussian1)
svm.visualize_boundary(X2, y2, model2)