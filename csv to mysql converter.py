'''
import numpy as np
import pandas as pd
import mysql.connector as sqlator

def loader(file_name):
    df = pd.read_csv(file_name)

#main
file_name = input('Enter file name: ')
table_name = input("Enter the table's name you want to create: ")
database_name = input ("Enter database name: ")

#mysql_connector
mycon = sqlator.connect(host='localhost', user='root', passwd='Plank#6.626', database=database_name)
if mycon.is_connected():
    print('connected')                                                                         # basic connection   object = mycon


cursor = mycon.cursor()                                                                   #cursor setup           cursor = cursor
'''
