#!Python 3

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

query = """create table if not exists owners (
    ID integer primary key autoincrement,
    firstName tinytext,
    lastName tinytext,
    phoneNum tinyint,
    email tinytext,
    adress tinytext,
    city tinytext,
    postalcode tinytext);"""
cursor.execute(query)

query = """create table if not exists pets (
    ID integer primary key autoincrement,
    name tinytext,
    type tinytext,
    breed tinytext,
    birthdate date,
    ownerID integer);"""
cursor.execute(query)

query = """create table if not exists visits (
    ID integer primary key autoincrement,
    ownerID integer,
    petID integer,
    details mediumtext,
    cost integer,
    paid integer);"""
cursor.execute(query)

#cursor.execute("PRAGMA table_info(Owners)")
#print(cursor.fetchall())

def addCustomer():
    fname = input("First name of new customer: ")
    lname = input("Last name of new customer: ")
    phoneNum = ''
    while not phoneNum.isdigit():
        phoneNum = input("Phone number of new customer: ")
        phoneNum = phoneNum.replace(' ','')
        phoneNum = phoneNum.replace('-','')
        phoneNum = phoneNum.replace('(','')
        phoneNum = phoneNum.replace(')','')
    email = input("Email adress of new customer: ")
    adress = input("Adress of new customer: ")
    city = input("City of new customer: ")
    postalcode = input("Postalcode of new customer: ")
    look = (lname,phoneNum,email,adress,city,postalcode)
    columns = ('lastName','phoneNum','email','adress','city','postalcode')
    for i in range(6):
        others = surchTalbe(look[i],'Owners','ID',columns[i])
    query = f"insert into owners (firstName,lastName,phoneNum,email,adress,city,postalcode) values ('{fname}','{lname}',{phoneNum},'{email}','{adress}','{city}','{postalcode}');"
    cursor.execute(query)
    #cursor.execute("select * from owners;")
    #print(cursor.fetchall())

def surchTalbe(surchIteam, table, find = "*", column = "ID"):
    query = f"select {find} from {table} where {column} = {surchIteam};"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

addCustomer()
print(surchTalbe(2,"Owners"))