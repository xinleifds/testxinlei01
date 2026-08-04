import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置字体
mpl.rcParams['font.family'] = 'SimHei'
# 读取Excel文件并转换日期格式
df = pd.read_excel('movie.xlsx', header=0)
df['Release Date'] = pd.to_datetime(df['Release Date'], format='%Y', errors='coerce')

# 检查有多少行无效日期数据
invalid_rows = df.loc[df['Release Date'].isna()]
if len(invalid_rows) > 0:
    print(f"发现 {len(invalid_rows)} 行无效日期数据:")
    print(invalid_rows)

# 获取年份和数量信息
release_years = df['Release Date'].apply(lambda x: x.year)
year_counts = release_years.value_counts()

# 绘制柱状图
plt.bar(year_counts.index.astype(str), year_counts)

# 设置X轴标签竖向显示
plt.xticks(rotation='vertical')

# 设置标题和轴标签
plt.title('电影年份分布情况')
plt.xlabel('年份')
plt.ylabel('数量')

# 显示图表
plt.show()