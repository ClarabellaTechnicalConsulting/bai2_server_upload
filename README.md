# bai2_server_upload
This repository contains all of the necessary files to parse BAI2 files and insert the data to a database.

# Intructions

## 0. Initialization

First you will need to run the setup_server.py file. This will prompt you to input the necessary information to access your server. This only needs to be run when configuring a server for the first time. 

## 1. Files

Simply put the BAI2 files into the bai_files directory. The program will upload every file that is in that directory. After each file is uploaded to the server, the file will be moved to the bai_files_old directory. This is done to ensure no files are uploaded twice.

## 2. Run

Run the upload.py file

## Comments

1. The program currently can only insert data into SQL Server but we are looking to add the ability to insert into other servers such as PosgreSQL and MySQL.
