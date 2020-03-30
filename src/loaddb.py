import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer
import pandas as pd
import pyodbc

# set up connection to database (with username/pw if needed)
engine = create_engine('mssql+pyodbc://sa:pwd@192.168.1.2/covid19?driver=ODBC Driver 17 for SQL Server')
print sqlalchemy.__version__ 

def initializeDB():
    print("Initializing DB...")
    result = engine.execute('DROP TABLE IF EXISTS covid19cases;')
    print("Initializing DB - Done")

def loadcsv():
    print("Loading CSV...")            
    # read csv data to dataframe with pandas|datatypes will be assumed
    df = pd.pandas.read_csv(r'../data/covidcases2020.csv', 
        encoding='latin-1',
        sep=',')

    # write to sql table... pandas will use default column names and dtypes
    df.to_sql('covid19cases',engine,index=True,index_label='id')
    print("Loading CSV - Done")            

def loadDB():
    loadcsv()

    
