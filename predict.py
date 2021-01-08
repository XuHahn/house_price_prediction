import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from convert_to_digital import *

x = np.array(x, np.float64).round(2)
y = np.array(y, np.int)
print('-------------------------------------')
x, x_test, y, y_test = train_test_split(x, y, test_size=0.1, shuffle=True)
line = LinearRegression()
print('- Fitting...')
line.fit(x, y)
print('- Fit end')
#                            ['面积均价', '面积', '户型', '朝向', '交通配套', '城市',]
# test = np.expand_dims(np.array([80000,    100,    53,     2,      1,       5]),axis=0)
# line.predict()

y_pre = line.predict(x_test)

ts = np.transpose(x, (1, 0))
coef = line.coef_
intercept = line.intercept_
print(f'- LinearRegression coef:{coef.round(2)}')
print(f'- LinearRegression intercept:{round(intercept, 2)}')
print(f'- LinearRegression score:{round(line.score(x_test, y_test), 2)}')
print(f'- LinearRegression mean_absolute_error:{round(mean_absolute_error(y_test, y_pre), 2)}')
print(f'- LinearRegression mean_squared_error:{round(mean_squared_error(y_test, y_pre), 2)}')
print(f'- LinearRegression r2_score:{round(r2_score(y_test, y_pre), 2)}')

corr = list(np.corrcoef(ts, y))
corr = list(map(lambda x: list(x), [i for i in corr]))

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False
plt.imshow(corr, cmap=plt.cm.hot, vmin=0, vmax=1)
plt.xticks(ticks=[i for i in range(7)], labels=['面积均价', '面积', '户型', '朝向', '交通配套', '城市', '总价'])
plt.yticks(ticks=[i for i in range(7)], labels=['面积均价', '面积', '户型', '朝向', '交通配套', '城市', '总价'])
plt.colorbar()
plt.show()

plt.figure()
for i in range(x.shape[1]):
    plt.subplot(3, 3, i + 1)
    plt.scatter(x[:, i], y)
    plt.plot(x[:, i], x[:, i] * coef[i] + intercept, color='r')
plt.show()
