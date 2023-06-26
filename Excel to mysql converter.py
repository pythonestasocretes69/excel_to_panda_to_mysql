import numpy as np
import pandas as pd
import mysql.connector as sqlator


def refine(arg):
    Mysql_types = ['datetime', 'float', 'integer', 'char(20)']
    panda_types = ['time', 'float', 'int', 'str']
    for i in range(len(Mysql_types)):
        print('Type:', arg)
        if str(panda_types[i]) in str(arg):
            return Mysql_types[i]


# panda is loading the file
file_name = input('Enter file name: ')
df = pd.read_excel(file_name)

# loading
table_name = input("Enter the table's name you want to create: ")
database_name = input("Enter database name: ")

# extraction of primary key & columns
columns = list(df.columns)
print(columns)
position = int(input('Enter the position of the column to be taken as a primary key:'))
print(columns[position], 'is the primary key')
primary_key = columns[position]

# extraction of datatypes of columns
column_types = []
for i in columns:
    column = (df.loc[0, i])
    panda_type = [str(type(column))]
    mysql_type = refine(panda_type)
    column_types += [mysql_type]
print(column_types, 'are the datatypes of columns')

# mysql_connector
mycon = sqlator.connect(host='localhost', user='root', passwd='Plank#6.626', database='business')
if mycon.is_connected():
    print('connected')  # basic connection   object = mycon

# cursor setup
cursor = mycon.cursor()

# database checkup
try:
    cursor.execute('use ' + database_name)
except:
    cursor.execute('create database ' + database_name)

# creation of table
description = ' '
for i in range(len(columns)):
    if i > 0:
        description += ','
    description += columns[i] + ' '
    description += column_types[i] + ' '
    if i == position:
        description += ' primary key '
table = "create table " + table_name + '(' + description + ')'
print(table)
cursor.execute(table)
mycon.commit()

# Entering data
n = (len(df.index))
command = "insert into " + table_name + ' values('

for i in column_types:
    if i == 'datetime' or i == 'char(20)':
        command = command + "'{}',"
    else:
        command = command + "{},"
command = command[0:-1] + ')'
print(command)

for i in range(n):
    entry_list = list(df.iloc[i, :])
    for j in column_types:
        if j == 'datetime':
            pos = column_types.index(j)
            entry_list[pos] = str(entry_list[pos])
    entry_tuple = tuple(entry_list)
    cursor.execute(command.format(*entry_tuple))

mycon.commit()
