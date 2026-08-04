import random
player = int(input("请输入您的出拳，1是石头，2是剪刀，3是布:"))
computer = random.randint(1,3)
print(f"您的出拳是{player}")
print(f"电脑的出拳是{computer}")
if player == computer:
    print('这局游戏是平局')
elif player == 1:
    if computer == 2:
        print('您赢了')
    else:
        print('电脑赢了')
elif player == 2:
    if computer == 3:
        print('您赢了')
    else:
        print('电脑赢了')
elif player == 3:
    if computer == 1:
        print('您赢了')
    else:
        print('电脑赢了')