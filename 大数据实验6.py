import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置字体
mpl.rcParams['font.family'] = 'SimHei'
# 读取Excel文件
df = pd.read_excel('movie.xlsx', header=0)

# 获取'Movie Types'列的值
movie_types = df['Release Info']

# 将所有种类放入一个列表中
all_movie_types = []
for types in movie_types:
  all_movie_types.extend(types.split(', '))

# 统计每个种类的数量
type_counts = dict()
for movie_type in all_movie_types:
  if movie_type in type_counts:
    type_counts[movie_type] += 1
  else:
    type_counts[movie_type] = 1

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(type_counts.values(), labels=type_counts.keys(), autopct='%1.1f%%')

# 添加图例，并设置位置
ax.legend(loc='center right', bbox_to_anchor=(1.5, 0.5))

# 设置标题
ax.set_title('电影上映地区占比')

# 显示图表
plt.show()