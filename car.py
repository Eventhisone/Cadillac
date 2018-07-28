import xlsxwriter
import random
import pandas as pd
import numpy as np


df=pd.read_csv('data.csv')
df.head()


export=df[['Depth','GR']]
export.to_csv("new1.csv")
array1=[]
array2=[]
sum_1=[]
Depth=export['Depth']
array1.append(Depth)
print(array1)
GR=export['GR']
array2.append(GR)
print(array2)

export['Result']=export["Depth"]+export["GR"]
export['Data Analysis']=export["Depth"]*export["GR"]




random_data = [random.random() for _ in range(10)]

# Data location inside excel
data_start_loc = [0, 0] # xlsxwriter rquires list, no tuple
data_end_loc = [data_start_loc[0] + len(export['Depth']), 0]

data_start_loc1 = [0, 1] # xlsxwriter rquires list, no tuple
data_end_loc1 = [data_start_loc[0] + len(export['Data Analysis']), 1]



workbook = xlsxwriter.Workbook('file.xlsx')

# Charts are independent of worksheets
chart = workbook.add_chart({'type': 'line'})
chart.set_y_axis({'name': 'Depth'})
chart.set_x_axis({'name': 'Data Analysis'})
chart.set_title({'name': 'Grapth of Depth&DA'})

worksheet = workbook.add_worksheet("Brittleness")
worksheet1 = workbook.add_worksheet("Brittleness1")


# A chart requires data to reference data inside excel
worksheet.write_column(*data_start_loc, data=export['Depth'])
worksheet.write_column(*data_start_loc1, data=export['Data Analysis'])
# The chart needs to explicitly reference data
chart.add_series({
    'values': [worksheet.name] + data_start_loc + data_end_loc,  
    'categories':[worksheet.name] + data_start_loc1 + data_end_loc1,
    'name': "Plot1",
})

worksheet.insert_chart('B1', chart)

workbook.close()

print("calculations done!")
#Done
