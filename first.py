## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#
import pandas as pd
#da= pd.read_csv("D:/Projects/RSA/newsetdata/testdata/4montsdata/allnewdataset/alldatafinaldate.csv")
#print (da.head(4))
#
#string_outcome=str(da.claimstatus)
#type(da.claimstatus)
#from datetime import datetime
#char_date='APR 3 2017'
#date_obj=datetime.strptime(char_date, '%b %d %Y' )
#tabledata=pd.DataFrame({'ID':[1,1,2,2],'PRODUCT':['aaa','bbb','dddd','fff'],'SALES':[30,45,78,45]})
#print(tabledata)
#result=tabledata.pivot(index='ID',columns='PRODUCT',values='SALES')
#print(result)
#result.fillna(0)
#print(tabledata.sort_index(['PRODUCT','SALES'],ascending=[True,False]))
#print (tabledata.sort_values(['PRODUCT','SALES'], ascending=[True, False]))

import matplotlib.pyplot as plt
plt_data=pd.DataFrame({'EmpID':['E001','E002','E003','E004','E005','E006','E007','E008','E009','E010'],'Gender':['M','F','F','M','F','M','M','F','M','M'],'Age':[34,45,23,45,26,35,38,67,38,20],'Sales':[123,234,345,456,567,678,789,240,456,567]})
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.hist(plt_data['Sales'],bins = 5)

plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Employee')
plt.show()



#x = [1, 2, 3, 4, 5]
#y = [1, 4, 9, 16, 25]
#fig = plt.figure()
#fig.add_subplot(111)
#plt.scatter(x, y)
#plt.show()
























