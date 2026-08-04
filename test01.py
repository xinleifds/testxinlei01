name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
height = float(input("请输入您的身高："))
print(type(name))
print(type(age))
print(type(height))
print(f"姓名：{name} 年龄：{age} 身高：{height}")
new_age = age + 5
print(f"{name}五年后的年龄是{new_age}")
man = age > 18
print(f"{name}是否成年：{man}")