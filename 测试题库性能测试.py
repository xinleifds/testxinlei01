import random

# 直接使用，最简单
questions = [
    "你们公司性能测试怎么做的，说一下流程是什么", "jmeter参数化的几种方式？",
    "beanshell主要是做什么的", "jmeter如何实现接口关联？",
    "如何判断系统压测达到了性能拐点", "压测测试数据怎么准备？",
    "测试环境和生产环境配置怎么样的", "测试环境压测最大tps多少？",
    "说一下性能监控的命令有哪些  ", "说一下你们性能压测场景有哪些？",
    "如何分析性能需求  ", "性能测试预期指标如何得到？",
    "测试过程中都发现那些性能问题，怎么定位分析的，优化方案是什么 ",
]
# 随机选择一个
selected_question = random.choice(questions)

print("=" * 50)
print("随机选中的问题是：")
print(selected_question)
print("=" * 50)