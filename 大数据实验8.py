import openpyxl
import matplotlib.pyplot as plt

# 打开 Excel 文件并选择要操作的工作表
wb = openpyxl.load_workbook('movie1.xlsx')
ws = wb['Sheet1']

# 读取 Release Info 和 Rating 列的数据，并将它们存储到两个列表中
release_infos = []
ratings = []
for row in ws.iter_rows(min_row=2, max_col=2, values_only=True):
    release_infos.append(row[0])
    ratings.append(row[1])

# 统计每个地区的电影平均评分，使用 Python 字典来存储每个地区的评分
region_ratings = {}
for region, rating in zip(release_infos, ratings):
    if region not in region_ratings:
        region_ratings[region] = [rating]
    else:
        region_ratings[region].append(rating)
for region, rating_list in region_ratings.items():
    region_ratings[region] = sum(rating_list) / len(rating_list)

# 绘制柱状图
fig, ax = plt.subplots()
ax.bar(region_ratings.keys(), region_ratings.values())

# 设置图表的属性，包括图表标题、坐标轴标签等
ax.set_title('地区与评分关系')
ax.set_xlabel('地区')
ax.set_ylabel('平均评分')

# 显示图像
plt.show()