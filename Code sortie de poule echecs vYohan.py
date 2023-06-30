# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:04:35 2023

@author: Paul FAVIER
"""

import random


joueurs = 64
tours = 7

score = [0 for x in range(joueurs)]

for i in range(tours):
    
    score.sort(reverse = True)
    
    for j in range(int(joueurs/2)):
        choix = random.randint(0,1)
        score[j*2 + choix] += 1

score.sort(reverse = True)
print(score)
