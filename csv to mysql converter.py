import numpy as np
import pandas as pd
import mysql.connector as sqlator


#panda is loading the file
file_name = input('Enter file name: ')
df = pd.read_excel(file_name)

#main
table_name = input("Enter the table's name you want to create: ")
database_name = input ("Enter database name: ")

columns = list(df.columns)                                                           # extraction of primary key & columns
print(columns)
position= int(input('Enter the positon of the column to be taken as a primary key:'))
print(columns[position],'is the primary key')
primary_key = columns[position]

column_types = []                                                                     #extraction of datatypes of columns
for i in columns:
    object = (df.loc[0,i])
    column_types+= [type(object)]
'''
#mysql_connector
mycon = sqlator.connect(host='localhost', user='root', passwd='Plank#6.626', database=database_name)
if mycon.is_connected():
    print('connected')                                                                         # basic connection   object = mycon


cursor = mycon.cursor()                                                                   #cursor setup           cursor = cursor
'''
