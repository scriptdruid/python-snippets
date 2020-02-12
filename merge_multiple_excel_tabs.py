import pandas as pd
import os

base_path = '/home/vipul/base_path/'

files = os.listdir(base_path)

files_xls = [f for f in files if f[-4:] == 'xlsx']


for f in files_xls:
    df1_temp = pd.read_excel(base_path + f, 'd1')
    df1 = df1.append(df1_temp)


path_out_path = '/home/vipul/out.xlsx'
writer = pd.ExcelWriter(path_out_path, engine='xlsxwriter')
df1.to_excel(writer, sheet_name='sheet1', index=False, columns=['a', 'b', 'c'])

writer.save()
writer.close()
