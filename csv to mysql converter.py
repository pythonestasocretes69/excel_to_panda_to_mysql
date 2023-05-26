import numpy as np
import pandas as pd
import mysql.connector as sqlator

def refine(arg):
    Mysql_types = ['datetime','float','intiger']
    panda_types = ['time','float','int']
    for i in range(3):
        if str(panda_types[i] in str(arg)):
            print(i,panda_types[i],arg,panda_types[i] in str(arg))
            return (Mysql_types[i])


#panda is loading the file
file_name = input('Enter file name: ')
df = pd.read_excel(file_name)

#loading
table_name = input("Enter the table's name you want to create: ")
database_name = input ("Enter database name: ")

columns = list(df.columns)                                                           # extraction of primary key & columns
print(columns)
position= int(input('Enter the positon of the column to be taken as a primary key:'))
print(columns[position],'is the primary key')
primary_key = columns[position]

column_types = []                                      #extraction of datatypes of columns
for i in columns:
    column = (df.loc[0,i])
    panda_type = [str(type(column))]
    mysql_type = refine(panda_type)
    print(mysql_type)
    column_types+= [mysql_type]
print(column_types)

#mysql_connector
mycon = sqlator.connect(host='localhost', user='root', passwd='Plank#6.626', database='business')
if mycon.is_connected():
    print('connected')                                                                         # basic connection   object = mycon


cursor = mycon.cursor()                                                                   #cursor setup           cursor = cursor

#database checkup
try:
    cursor.execute('check database '+database_name)
except:
    cursor.execute('create database '+database_name)




    
