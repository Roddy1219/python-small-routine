#!/bin/env python
# -*- coding:utf-8 -*-
###############################################
#猜数字游戏,用户猜测数字，直到猜中为准并输出结果
###############################################

from random import randint

#游戏次数
game_count = 0
all_counts = []
while True:
    game_count += 1 
    guess_count = 0
    answer = randint(0,99)
    while True:
        guess = int(input("请输入您所猜的数字:"))
        guess_count +=1
        if guess > answer:
            print "您输入的数字太大!"
            continue
        elif guess < answer:
            print "您输入的数字太小!"
            continue
        else:
            print "恭喜您，猜中!"
            all_counts.append(guess_count)
            break
    onemore = raw_input("还要玩吗?(Y/N):")
    print onemore
    if onemore != 'Y' and onemore != 'y':
         print "欢迎下次再来"
         print "您的成绩如下："
         print all_counts
         print "平均猜中次数:" + str(sum(all_counts) / float(len(all_counts)))
         break
    

