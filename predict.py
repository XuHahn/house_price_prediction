import numpy as np
import sklearn
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from convert_to_digital import *
from sklearn.tree import DecisionTreeRegressor
import pydotplus
import graphviz
from sklearn import tree as t
x = np.array(x, np.float32).round(2)
y = np.array(y, np.int)
x = preprocessing.StandardScaler().fit(x).transform(x)
x, y = sklearn.utils.shuffle(x, y)
x, x_test, y, y_test = train_test_split(x, y, test_size=0.1, shuffle=True)

print('-------------------------------------')

line = LinearRegression()
tree = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
print('- Fitting...')
line.fit(x, y)
tree.fit(x, y)
print('- Fit end')
#                            ['面积均价', '面积', '户型', '朝向', '交通配套', '城市',]
test = np.expand_dims(np.array([80000,    100,    53,     2,      1,       5]),axis=0)

dot_data = t.export_graphviz(tree, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("tree.png")

print('LinearRegression predict: ',line.predict(test))
print('DecisionTreeRegressor predict: ',tree.predict(test))
print('-------------------------------------')
y_pre = line.predict(x_test)
y_pre_tree = tree.predict(x_test)
ts = np.transpose(x, (1, 0))
coef = line.coef_
intercept = line.intercept_
print(f'- LinearRegression coef:{coef.round(2)}')
print(f'- LinearRegression intercept:{round(intercept, 2)}')
print(f'- LinearRegression score:{round(line.score(x_test, y_test), 2)}')
print(f'- LinearRegression mean_absolute_error:{round(mean_absolute_error(y_test, y_pre), 2)}')
print(f'- LinearRegression mean_squared_error:{round(mean_squared_error(y_test, y_pre), 2)}')
print(f'- LinearRegression r2_score:{round(r2_score(y_test, y_pre), 2)}')
print('-------------------------------------')
print(f'- DecisionTreeRegressor score:{round(tree.score(x_test, y_test), 2)}')
print(f'- DecisionTreeRegressor mean_absolute_error:{round(mean_absolute_error(y_test, y_pre_tree), 2)}')
print(f'- DecisionTreeRegressor mean_squared_error:{round(mean_squared_error(y_test, y_pre_tree), 2)}')
print(f'- DecisionTreeRegressor r2_score:{round(r2_score(y_test, y_pre_tree), 2)}')

corr = list(map(lambda x: list(x), [i for i in list(np.corrcoef(ts, y))]))

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
