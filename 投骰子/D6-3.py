from plotly.graph_objs import Bar,Layout
from  plotly import offline

from  die import Die

# 创建三个 D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷几次骰子并将结果存在同一个列表
results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()+die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides+die_2.num_sides+die_3.num_sides
for value in range(3,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config={'title': '结果', 'dtick': 1}
y_axis_config={'title': '结果的频率'}
my_layout = Layout(title='掷三个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout},filename='d6_d6.html')