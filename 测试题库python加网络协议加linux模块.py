import random

# 直接使用，最简单
questions = [
    "列表和元组区别？", "哪些是可变类型，哪些是不可变类型？",
    "列表常见api函数操作？", "字符串常见函数操作？",
    "字典常见函数操作？", "不定长传参？",
    "断言函数？", "异常捕获关键字？",
    "break和continue关键字区别？", "列表和字符串如何转换？",
    "什么是深浅拷贝？", "什么是装饰器，有没有实现过？",
    "魔术方法？", "什么是迭代器，生成器？",
    "推导式是什么？", "讲讲多线程编程？",
    "讲讲python内存管理机制？", "讲讲python垃圾回收机制？",
    "除了http协议接口还知道哪些？", "http和https区别？",
    "cookie，session，token机制是什么？", "接口请求的几种方式？",
    "get和post请求有什么区别？", "常见返回状态码？",
    "说几个常见的linux命令", "如何通过查看日志定位分析bug",
    "进程和线程有什么区别", "会不会搭建测试环境"
]
# 随机选择一个
selected_question = random.choice(questions)

print("=" * 50)
print("随机选中的问题是：")
print(selected_question)
print("=" * 50)