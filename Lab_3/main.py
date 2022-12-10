from matplotlib import rc
import regress as reg


font = {'family': 'Verdana', 'weight': 'normal'}
rc('font', **font)
# Вызов функций
reg.oneRegress()
reg.twoRegress()
