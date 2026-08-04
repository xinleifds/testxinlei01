import random

# 直接使用，最简单
questions = [
    "mq的优缺点是什么？", "你们公司用的是什么mq消息队列？",
    "说说你们项目中mq是怎么测试的，有哪些注意的点？", "保险项目哪些地方使用了mq？",
    "结合你们的保险项目说说如何测试mq？", "如何查询mq？",
    "什么是redis？", "什么数据存入redis缓存？",
    "redis为什么快？", "为什么使用redis，它的优势是什么？",
    "redis的五种数据结构？", "结合保险项目讲讲redis是怎么测试的？"
]
# 随机选择一个
selected_question = random.choice(questions)

print("=" * 50)
print("随机选中的问题是：")
print(selected_question)
print("=" * 50)