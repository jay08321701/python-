#extract special column of excel
import numpy as np
import pandas as pd
import os
import xlrd
import csv
root = 'E:/MaoBoShi/shanxiemission'
path = 'E:/MaoBoShi/shanxiemission/shanxi.xlsx'
start= 1970
for i in range(0,46):
    file = start + i
    i = i + 2
    df = pd.read_excel(path, usecols=[0, 1, i])
    df.to_csv(root+"/"+str(file)+'.csv',index=None)
print(df)