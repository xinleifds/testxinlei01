import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

# 将种类及其对应的数量放入一个DataFrame对象中
type_df = pd.DataFrame(list(type_counts.items()), columns=['Movie Type', 'Count'])

# 将种类进行排序
type_df = type_df.sort_values('Count', ascending=False)

# 设置中文字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

# 绘制柱状图
plt.bar(type_df['Movie Type'], type_df['Count'])

# 设置X轴和Y轴标签
plt.xlabel('电影上映地区', fontproperties=font)
plt.ylabel('数量', fontproperties=font)

# 设置标题
plt.title('电影上映地区统计', fontproperties=font)

# 自动旋转X轴刻度
plt.xticks(rotation=45, ha='right', fontproperties=font)

# 显示图表
plt.show()