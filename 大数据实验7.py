import openpyxl
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置字体
mpl.rcParams['font.family'] = 'SimHei'
# 打开 Excel 文件并选择要操作的工作表
wb = openpyxl.load_workbook('movie1.xlsx')
ws = wb['Sheet1']

# 读取 Release Date 和 Rating 列的数据，并将它们存储到两个列表中
release_dates = []
ratings = []
for row in ws.iter_rows(min_row=2, max_col=2, values_only=True):
    release_dates.append(row[0])
    ratings.append(row[1])

# 统计每年的电影平均评分，使用 Python 字典来存储每年的评分
yearly_ratings = {}
for year, rating in zip(release_dates, ratings):
    if year not in yearly_ratings:
        yearly_ratings[year] = [rating]
    else:
        yearly_ratings[year].append(rating)
for year, rating_list in yearly_ratings.items():
    yearly_ratings[year] = sum(rating_list) / len(rating_list)

# 绘制柱状图
fig, ax = plt.subplots()
ax.bar(yearly_ratings.keys(), yearly_ratings.values())

# 设置图表的属性，包括图表标题、坐标轴标签等
ax.set_title('电影发行年份与评分关系')
ax.set_xlabel('电影发行年份')
ax.set_ylabel('平均评分')

# 显示图像
plt.show()