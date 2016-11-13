import numpy;
import sqlite3;

database_name = "BrightBrain.sqlite";

def createTables():
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("CREATE TABLE users (id number(10) PRIMARY KEY, name varchar(20), password varchar(20));")
    cursor.execute("CREATE TABLE exercise (userid number(10), date date, time time, reps number, sets number, weight number, PRIMARY KEY (userid, date, time), foreign key (userid) references users(id));");
    cursor.execute("CREATE TABLE food (userid number(10), date date, time time, name varchar(30), calories number, protein number, carbs number, fats number, PRIMARY KEY (userid, date, time, name), foreign key (userid) references users(id));");
    cursor.execute("CREATE TABLE sleep (userid number(10), date date, startTime time, endTime time, PRIMARY KEY (userId, date, startTime), foreign key (userid) references users(id));");
    cursor.execute("CREATE TABLE water (userid number(10), date date, time time, amount number, primary key (userid, date, time), foreign key (userid) references users(id));");
    cursor.execute("CREATE TABLE stress (userid number(10), date date, rating number, primary key (userid, date), foreign key (userid) references users(id));");
    conn.commit();
    conn.close();
    
