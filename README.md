# bai2_server_upload
This repository contains all of the necessary files to parse BAI2 files and insert the data to a database.

# Intructions

## 0. Initialization

First you will need to run the setup_server.py file. This will prompt you to input the necessary information to access your server. This only needs to be run when configuring a server for the first time. 

## 1. Files

Simply put the BAI2 files into the bai_files directory. The program will upload every file that is in that directory even if it has already been added to the database so be sure to take the files out after you run them. 

## 2. Run

Run the upload.py file

## Comments

1. The program currently can only insert data into SQL Server but we are looking to add the ability to insert into other servers such as PosgreSQL and MySQL.
2. We are working on a feature that can move files to another directory after being uploaded.
