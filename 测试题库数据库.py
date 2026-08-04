import random

# 直接使用，最简单
questions = [
    "主键，外键？", "什么是事务？",
    "事务的四个重要特性，ACID？", "什么是索引，有什么作用？",
    "索引是针对数据库表字段的，如何查看有没有添加索引？", "如何在某字段加索引？",
    "加索引有什么优势，好处？", "一般在什么字段上加索引？",
    "索引加的越多越好么？", "什么是存储过程，有什么用途？",
    "存储过程有什么缺点和弊端？"
]
# 随机选择一个
selected_question = random.choice(questions)

print("=" * 50)
print("随机选中的问题是：")
print(selected_question)
print("=" * 50)