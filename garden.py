# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

garden = [['Blumen', 10, 1, 1], ['Petersilie', 15, 1, 1], ['Karotten',20, 0.5,1]]
print('Welcome to our semi-automatic garden')
for days in range(30):
    print("Heute ist Tag "+str(days+1))
    for plant in garden:
        plant[3]-=plant[2]
        if plant[3]==0:
            print(plant[0]+' is being watered automatically')
            plant[3]+=1
        nachricht = ''
        if days>plant[1]:
            nachricht += plant[0]+' blüht!'
        else:
            nachricht = nachricht + plant[0] +' brauchen noch '+ str(plant[1]-days)
        print(nachricht)
    print('\n')