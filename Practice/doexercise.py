# -*- coding:utf8 -*-
"01.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"
# num = []
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a != b and a != c and b != c:
#                 item = a,b,c
#                 num.append(item)
# print(len(num))

"03.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？"

# node = [1000000,600000,400000,200000,100000,0]
# rate = [0.01,0.015,0.03,0.05,0.075,0.1]
# bonus = 0
# I = int(input("输入当月利润为："))
#
# for i in range(6):
#     if I > node[i]:
#         bonus += (I-node[i])*rate[i]
#         I = node[i]
# print(bonus)

"一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？"

"30.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。"
# a =  str(input("输入一个五位数："))
# flag = True
#
# for i in range(int(len(a)/2)):
#     if a[i] != a[-i-1]:
#         flag = False
#         break
#
# if flag == True:
#     print("{}是回文数".format(a))
# else:
#     print("{}不是回文数".format(a))
