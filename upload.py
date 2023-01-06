##
#
#

import shutil
from bai_parser import BAI2File
import pyodbc
import os
from sys import exit
import yaml

if 'key.yml' not in os.listdir(os.getcwd()):
    exit('There is no server defined. To fix this, run \'server_setup\' file')

with open('key.yml', 'r') as file:
    config_file = yaml.safe_load(file)

server_type: str = config_file['Server']['Server Type']
server_address: str = config_file['Server']['Server Address']
database: str = config_file['Server']['Database Name']
username: str = config_file['Server']['Username']
password: str = config_file['Server']['Password']
current_directory: str = os.getcwd()
if server_type == 'SQL Server':
    conx = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server_address + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conx.cursor()

    for local_file in os.listdir(current_directory + '/bai_files'):
        file = BAI2File(local_file, current_directory + '/bai_files/' + local_file)

        """ This will insert into the table named AccountDetail
            To change this edit line 35"""
        for account in file.accounts:
            cursor.execute("""INSERT INTO [dbo].[AccountDetail]
                                ([AccountNo],[OpeningBalance],[ClosingBalance],[TotalCredits],[TotalDebits],
                                [CreditCount],[DebitCount],[FileDate],[DataLoadDT],[FileName])
                                VALUES
                                (?,?,?,?,?
                                ,?,?,?,?,?);""",
                           account['AccountNo'], account['OpeningBalance'], account['ClosingBalance'],
                           account['TotalCredits'], account['TotalDebits'],
                           account['CreditCount'], account['DebitCount'], account['FileDate'], account['DataLoadDT'],
                           account['FileName']
                           )
            conx.commit()

        """ This will insert into the table named Transactions
            To change this edit line 51"""
        for transaction in file.transactions:
            cursor.execute("""INSERT INTO [dbo].[Transactions]
                        ([BAI2FileDate],[AccountNo],[Amount],[Description],[Name]
                        ,[DataLoadDT],[FileName])
                        VALUES
                        (?,?,?,?,?
                        ,?,?);""",
                           transaction['BAI2FileDate'], transaction['AccountNo'], transaction['Amount'],
                           transaction['Description'], transaction['Name'],
                           transaction['DataLoadDT'], transaction['FileName']
                           )
            conx.commit()
            
            shutil.move(current_directory + '/bai_files/' + local_file, current_directory + '/bai_files_old/')
            
