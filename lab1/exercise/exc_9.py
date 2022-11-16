import lab1.lib.svm as svm
import scipy.io as sio
import numpy as np

data2 = sio.loadmat('dataset3.mat')
Xval = data2['Xval']
yval = data2['yval']
y2 = np.float64(data2['y'])
X2 = data2['X']

minError = 9999
C4 = 0
sigma4 = 0

for C3 in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
    for sigma3 in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        gaussian2 = svm.partial(svm.gaussian_kernel, sigma=sigma3)
        gaussian2.__name__ = svm.gaussian_kernel.__name__
        model3 = svm.svm_train(X2, y2, C3, gaussian2)

        ypred = svm.svm_predict(model3, Xval)

        error = np.mean(ypred != yval.ravel())
        if error < minError:
            minError = error
            C4 = C3
            sigma4 = sigma3

gaussian4 = svm.partial(svm.gaussian_kernel, sigma=sigma4)
gaussian4.__name__ = svm.gaussian_kernel.__name__
model = svm.svm_train(X2, y2, C4, gaussian4)
svm.visualize_boundary(X2, y2, model)