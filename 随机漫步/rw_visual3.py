import matplotlib.pyplot as plt
from random_walk3 import RandomWalk3
from mpl_toolkits import mplot3d

while True:
    # 创建一个 RandomWalk实列
    rw = RandomWalk3(50_000)
    rw.fill_walk()
    plt.style.use('classic')
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, rw.z_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    # 突然起点和终点
    ax.scatter(0, 0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], rw.z_values[-1], c='red', edgecolors='none', s=100)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.get_zaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk(y/n):?")
    if keep_running == 'n':
        break
