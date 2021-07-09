#import data & calculate overall average of all batting situation
#order:1B,2B,3B,HR,BB,OUT
from os import X_OK
from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
#function

#用全聯盟的平均去推算每個打者上來打擊,不同結果所發生的機率
def single_play():
    global overall_percentage_of_play
    outcome=random.choices(['1B','2B','3B','HR','BB','out'],weights=overall_percentage_of_play,k=1)
    return ''.join(outcome)
#用大谷目前為止的成績推算每次上來打擊不同結果發生的機率
def ohtani_single_play():
    global ohtani_percentage_of_play
    outcome=random.choices(['1B','2B','3B','HR','BB','out'],weights=ohtani_percentage_of_play,k=1)
    return ''.join(outcome)
#每次上來打擊都是BB
def IBB_single_play():
    return 'BB'
#同single_play(),但是所有的'安打'都轉成'HR'
def onlyHR_single_play():
    outcome=random.choices(['1B','2B','3B','HR','BB','out'],weights=[0,0,0,20599/94342,8584/94342,65159/94342],k=1)
    return ''.join(outcome)
#計算每場比賽的得分
def playball():
    run,inning,out,batter,field=0,1,0,1,[]
    #game start
    while inning<=9:
        #start of the inning
        while out<3:
            if batter==10:
                batter=1
            play=single_play()
            if play == '1B':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1壘有人
                    field=[1,2]
                elif field==[2] and out!=2:     #2壘有人 & 0,1 out
                    field=[1,3]
                elif field==[2] and out==2:     #2壘有人 & 2 out
                    field=[1]
                    run+=1
                elif field==[3]:                #3壘有人
                    field=[1]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[1,2,3]
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[1,2]
                    run+=1
                elif field==[1,3]:              #1,3
                    field=[1,2]
                    run+=1
                elif field==[2,3] and out!=2:   #2,3 & 0,1 out
                    field=[1,3]
                    run+=1
                elif field==[2,3] and out==2:   #2,3 & 2 out
                    field=[1]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[1,2,3]
                    run+=1
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[1,2]
                    run+=2
            elif play == '2B':
                if field==[]:                   #無人在壘
                    field=[2]
                elif field==[1]:                #1壘有人 & 0,1 out
                    field=[2,3]
                elif field==[1] and out==2:     #1 & 2 out
                    field=[2]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[2]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[2]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[2]
                    run+=2
                elif field==[1,3] and out!=2:   #1,3 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,3] and out==2:   #1,3 & 2 out
                    field=[2]
                    run+=2  
                elif field==[2,3]:              #2,3
                    field=[2]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[2,3]
                    run+=2
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[2]
                    run+=3
            elif play == '3B':
                if field==[]:                   #無人在壘
                    field=[3]
                elif field==[1]:                #1
                    field=[3]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[3]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[3]
                    run+=1
                elif field==[1,2]:              #1,2壘有人
                    field=[3]
                    run+=2
                elif field==[1,3]:              #1,3
                    field=[3]
                    run+=2
                elif field==[2,3]:              #2,3
                    field=[3]
                    run+=2
                elif field==[1,2,3]:            #滿壘
                    field=[3]
                    run+=3
            elif play == 'HR':
                if field==[]:                   #無人在壘
                    run+=1
                elif field==[1]:                #1
                    field=[]
                    run+=2
                elif field==[2]:                #2壘有人
                    field=[]
                    run+=2;
                elif field==[3]:                #3壘有人
                    field=[]
                    run+=2
                elif field==[1,2]:              #1,2壘有人
                    field=[]
                    run+=3
                elif field==[1,3]:              #1,3
                    field=[]
                    run+=3
                elif field==[2,3]:              #2,3
                    field=[]
                    run+=3
                elif field==[1,2,3]:            #滿壘
                    field=[]
                    run+=4
            elif play == 'BB':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1
                    field=[1,2]
                elif field==[2]:                #2壘有人
                    field=[1,2]
                elif field==[3]:                #3壘有人
                    field=[1,3]
                elif field==[1,2]:              #1,2壘有人
                    field=[1,2,3]
                elif field==[1,3]:              #1,3
                    field=[1,2,3]
                elif field==[2,3]:              #2,3
                    field=[1,2,3]
                elif field==[1,2,3]:            #滿壘
                    field=[1,2,3]
                    run+=1
            elif play == 'out':
                out+=1
            batter+=1
            #3 outs
        out=0
        field=[]
        inning+=1
        #next inning
    return run
#計算大谷在第二棒時每場比賽的得分
def playball_with_ohtani():
    run,inning,out,batter,field=0,1,0,1,[]
    #game start
    while inning<=9:
        #start of the inning
        while out<3:
            if batter==10:
                batter=1
            if batter==2:                   ##和playball()的差異
                play=ohtani_single_play()
            else:
                play=single_play()
            if play == '1B':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1壘有人
                    field=[1,2]
                elif field==[2] and out!=2:     #2壘有人 & 0,1 out
                    field=[1,3]
                elif field==[2] and out==2:     #2壘有人 & 2 out
                    field=[1]
                    run+=1
                elif field==[3]:                #3壘有人
                    field=[1]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[1,2,3]
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[1,2]
                    run+=1
                elif field==[1,3]:              #1,3
                    field=[1,2]
                    run+=1
                elif field==[2,3] and out!=2:   #2,3 & 0,1 out
                    field=[1,3]
                    run+=1
                elif field==[2,3] and out==2:   #2,3 & 2 out
                    field=[1]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[1,2,3]
                    run+=1
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[1,2]
                    run+=2
            elif play == '2B':
                if field==[]:                   #無人在壘
                    field=[2]
                elif field==[1]:                #1壘有人 & 0,1 out
                    field=[2,3]
                elif field==[1] and out==2:     #1 & 2 out
                    field=[2]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[2]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[2]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[2]
                    run+=2
                elif field==[1,3] and out!=2:   #1,3 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,3] and out==2:   #1,3 & 2 out
                    field=[2]
                    run+=2  
                elif field==[2,3]:              #2,3
                    field=[2]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[2,3]
                    run+=2
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[2]
                    run+=3
            elif play == '3B':
                if field==[]:                   #無人在壘
                    field=[3]
                elif field==[1]:                #1
                    field=[3]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[3]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[3]
                    run+=1
                elif field==[1,2]:              #1,2壘有人
                    field=[3]
                    run+=2
                elif field==[1,3]:              #1,3
                    field=[3]
                    run+=2
                elif field==[2,3]:              #2,3
                    field=[3]
                    run+=2
                elif field==[1,2,3]:            #滿壘
                    field=[3]
                    run+=3
            elif play == 'HR':
                if field==[]:                   #無人在壘
                    run+=1
                elif field==[1]:                #1
                    field=[]
                    run+=2
                elif field==[2]:                #2壘有人
                    field=[]
                    run+=2;
                elif field==[3]:                #3壘有人
                    field=[]
                    run+=2
                elif field==[1,2]:              #1,2壘有人
                    field=[]
                    run+=3
                elif field==[1,3]:              #1,3
                    field=[]
                    run+=3
                elif field==[2,3]:              #2,3
                    field=[]
                    run+=3
                elif field==[1,2,3]:            #滿壘
                    field=[]
                    run+=4
            elif play == 'BB':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1
                    field=[1,2]
                elif field==[2]:                #2壘有人
                    field=[1,2]
                elif field==[3]:                #3壘有人
                    field=[1,3]
                elif field==[1,2]:              #1,2壘有人
                    field=[1,2,3]
                elif field==[1,3]:              #1,3
                    field=[1,2,3]
                elif field==[2,3]:              #2,3
                    field=[1,2,3]
                elif field==[1,2,3]:            #滿壘
                    field=[1,2,3]
                    run+=1
            elif play == 'out':
                out+=1
            batter+=1
            #3 outs
        out=0
        field=[]
        inning+=1
        #next inning
    return run
#計算每場每次遇到第二棒都IBB的得分
def playball_with_IBB():
    
    run,inning,out,batter,field=0,1,0,1,[]
    #game start
    while inning<=9:
        #start of the inning
        while out<3:
            if batter==10:
                batter=1
            if batter==2:                   ##和playball()的差異
                play='BB'
            else:
                play=single_play()
            if play == '1B':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1壘有人
                    field=[1,2]
                elif field==[2] and out!=2:     #2壘有人 & 0,1 out
                    field=[1,3]
                elif field==[2] and out==2:     #2壘有人 & 2 out
                    field=[1]
                    run+=1
                elif field==[3]:                #3壘有人
                    field=[1]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[1,2,3]
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[1,2]
                    run+=1
                elif field==[1,3]:              #1,3
                    field=[1,2]
                    run+=1
                elif field==[2,3] and out!=2:   #2,3 & 0,1 out
                    field=[1,3]
                    run+=1
                elif field==[2,3] and out==2:   #2,3 & 2 out
                    field=[1]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[1,2,3]
                    run+=1
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[1,2]
                    run+=2
            elif play == '2B':
                if field==[]:                   #無人在壘
                    field=[2]
                elif field==[1]:                #1壘有人 & 0,1 out
                    field=[2,3]
                elif field==[1] and out==2:     #1 & 2 out
                    field=[2]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[2]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[2]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[2]
                    run+=2
                elif field==[1,3] and out!=2:   #1,3 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,3] and out==2:   #1,3 & 2 out
                    field=[2]
                    run+=2  
                elif field==[2,3]:              #2,3
                    field=[2]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[2,3]
                    run+=2
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[2]
                    run+=3
            elif play == '3B':
                if field==[]:                   #無人在壘
                    field=[3]
                elif field==[1]:                #1
                    field=[3]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[3]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[3]
                    run+=1
                elif field==[1,2]:              #1,2壘有人
                    field=[3]
                    run+=2
                elif field==[1,3]:              #1,3
                    field=[3]
                    run+=2
                elif field==[2,3]:              #2,3
                    field=[3]
                    run+=2
                elif field==[1,2,3]:            #滿壘
                    field=[3]
                    run+=3
            elif play == 'HR':
                if field==[]:                   #無人在壘
                    run+=1
                elif field==[1]:                #1
                    field=[]
                    run+=2
                elif field==[2]:                #2壘有人
                    field=[]
                    run+=2;
                elif field==[3]:                #3壘有人
                    field=[]
                    run+=2
                elif field==[1,2]:              #1,2壘有人
                    field=[]
                    run+=3
                elif field==[1,3]:              #1,3
                    field=[]
                    run+=3
                elif field==[2,3]:              #2,3
                    field=[]
                    run+=3
                elif field==[1,2,3]:            #滿壘
                    field=[]
                    run+=4
            elif play == 'BB':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1
                    field=[1,2]
                elif field==[2]:                #2壘有人
                    field=[1,2]
                elif field==[3]:                #3壘有人
                    field=[1,3]
                elif field==[1,2]:              #1,2壘有人
                    field=[1,2,3]
                elif field==[1,3]:              #1,3
                    field=[1,2,3]
                elif field==[2,3]:              #2,3
                    field=[1,2,3]
                elif field==[1,2,3]:            #滿壘
                    field=[1,2,3]
                    run+=1
            elif play == 'out':
                out+=1
            batter+=1
            #3 outs
        out=0
        field=[]
        inning+=1
        #next inning
    return run
#計算每場比賽中第二棒的安打都是全壘打的得分
def playball_with_onlyHR():
    run,inning,out,batter,field=0,1,0,1,[]
    #game start
    while inning<=9:
        #start of the inning
        while out<3:
            if batter==10:
                batter=1
            if batter == 2:
                play=onlyHR_single_play()
            else:
                play=single_play()
            if play == '1B':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1壘有人
                    field=[1,2]
                elif field==[2] and out!=2:     #2壘有人 & 0,1 out
                    field=[1,3]
                elif field==[2] and out==2:     #2壘有人 & 2 out
                    field=[1]
                    run+=1
                elif field==[3]:                #3壘有人
                    field=[1]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[1,2,3]
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[1,2]
                    run+=1
                elif field==[1,3]:              #1,3
                    field=[1,2]
                    run+=1
                elif field==[2,3] and out!=2:   #2,3 & 0,1 out
                    field=[1,3]
                    run+=1
                elif field==[2,3] and out==2:   #2,3 & 2 out
                    field=[1]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[1,2,3]
                    run+=1
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[1,2]
                    run+=2
            elif play == '2B':
                if field==[]:                   #無人在壘
                    field=[2]
                elif field==[1]:                #1壘有人 & 0,1 out
                    field=[2,3]
                elif field==[1] and out==2:     #1 & 2 out
                    field=[2]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[2]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[2]
                    run+=1
                elif field==[1,2] and out!=2:   #1,2壘有人 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,2] and out==2:   #1,2壘有人 & 2 out
                    field=[2]
                    run+=2
                elif field==[1,3] and out!=2:   #1,3 & 0,1 out
                    field=[2,3]
                    run+=1
                elif field==[1,3] and out==2:   #1,3 & 2 out
                    field=[2]
                    run+=2  
                elif field==[2,3]:              #2,3
                    field=[2]
                    run+=2
                elif field==[1,2,3] and out!=2: #滿壘 & 0,1 out
                    field=[2,3]
                    run+=2
                elif field==[1,2,3] and out==2: #滿壘 2 out
                    field=[2]
                    run+=3
            elif play == '3B':
                if field==[]:                   #無人在壘
                    field=[3]
                elif field==[1]:                #1
                    field=[3]
                    run+=1
                elif field==[2]:                #2壘有人
                    field=[3]
                    run+=1;
                elif field==[3]:                #3壘有人
                    field=[3]
                    run+=1
                elif field==[1,2]:              #1,2壘有人
                    field=[3]
                    run+=2
                elif field==[1,3]:              #1,3
                    field=[3]
                    run+=2
                elif field==[2,3]:              #2,3
                    field=[3]
                    run+=2
                elif field==[1,2,3]:            #滿壘
                    field=[3]
                    run+=3
            elif play == 'HR':
                if field==[]:                   #無人在壘
                    run+=1
                elif field==[1]:                #1
                    field=[]
                    run+=2
                elif field==[2]:                #2壘有人
                    field=[]
                    run+=2;
                elif field==[3]:                #3壘有人
                    field=[]
                    run+=2
                elif field==[1,2]:              #1,2壘有人
                    field=[]
                    run+=3
                elif field==[1,3]:              #1,3
                    field=[]
                    run+=3
                elif field==[2,3]:              #2,3
                    field=[]
                    run+=3
                elif field==[1,2,3]:            #滿壘
                    field=[]
                    run+=4
            elif play == 'BB':
                if field==[]:                   #無人在壘
                    field=[1]
                elif field==[1]:                #1
                    field=[1,2]
                elif field==[2]:                #2壘有人
                    field=[1,2]
                elif field==[3]:                #3壘有人
                    field=[1,3]
                elif field==[1,2]:              #1,2壘有人
                    field=[1,2,3]
                elif field==[1,3]:              #1,3
                    field=[1,2,3]
                elif field==[2,3]:              #2,3
                    field=[1,2,3]
                elif field==[1,2,3]:            #滿壘
                    field=[1,2,3]
                    run+=1
            elif play == 'out':
                out+=1
            batter+=1
            #3 outs
        out=0
        field=[]
        inning+=1
        #next inning
    return run
#從CSV中讀取資料再計算全聯盟平均1B,2B,3B,HR,BB,out的機率
def overall():
    data=pd.read_csv('mlb_stat.csv')
    for index,row in data.iterrows():
        data.loc[index,'AB']=int(row['AB'][0:1]+row['AB'][2:])
    total_AB=data['AB'].agg(sum)
    total_H=data['H'].agg(sum)
    total_2B=data['2B'].agg(sum)
    total_3B=data['3B'].agg(sum)
    total_HR=data['HR'].agg(sum)
    total_BB=data['BB'].agg(sum)
    total_1B=total_H-(total_2B+total_3B+total_HR)
    total_out=total_AB-total_H
    total_PA=total_AB+total_BB
    overall_percentage_of_play=[
        total_1B/total_PA,
        total_2B/total_PA,
        total_3B/total_PA,
        total_HR/total_PA,
        total_BB/total_PA,
        total_out/total_PA
    ]
    return overall_percentage_of_play
#計算大谷上述數據的機率
def ohtani(): 
    ohtani_percentage_of_play=[27/326,18/326,4/326,32/326,36/326,209/326]
    return ohtani_percentage_of_play

#main
overall_percentage_of_play=overall()
ohtani_percentage_of_play=ohtani()
overall_list=[]
ohtani_list=[]
IBB_list=[]
onlyHR_list=[]
for i in range(1):
    run=playball()
    overall_list.append(run)
    run_ohtani=playball_with_ohtani()
    ohtani_list.append(run_ohtani)
    run_IBB=playball_with_IBB()
    IBB_list.append(run_IBB)
    run_onlyHR=playball_with_onlyHR()
    onlyHR_list.append(run_onlyHR)
name_list=['Overall','Ohtani','IBB','onlyHR']
value_list=[np.mean(overall_list),np.mean(ohtani_list),np.mean(IBB_list),np.mean(onlyHR_list)]
plt.bar(name_list,value_list)
plt.xticks(name_list,rotation=45)
plt.xlabel('Type of Game')
plt.ylabel('Average Scores of a Game')
plt.title('Calculate the Average Score of Different Type of Game')
plt.grid()
plt.show()