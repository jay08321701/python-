#extract special column of excel
import numpy as np
import pandas as pd
import os
import xlrd
import csv
root = 'E:/MaoBoShi/shanxiemission' #设置输出的root
path = 'E:/MaoBoShi/shanxiemission/shanxi.xlsx' #读取的目录
start= 1970    #列开始的年份 
for i in range(0,46): #i遍历的次数
    file = start + i   #file为输出的excel名字
    i = i + 2          #第三列
    df = pd.read_excel(path, usecols=[0, 1, i]) #读取指定列的数据，但是usecols可以随意
    df.to_csv(root+"/"+str(file)+'.csv',index=None) #输出csv
print(df)
