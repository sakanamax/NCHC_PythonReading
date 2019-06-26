#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

age_of_ironman = random.randint(1,100)

count = 0

while True:
    if count >= 10:
        break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_ironman:
        print("Bingo, You got it!!!")
        break
    elif guess_age > age_of_ironman:
        print("You may think smaller...")
    else:
        print("You may think bigger...")
    count += 1