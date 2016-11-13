import numpy;
import sqlite3;

database_name = "BrightBrain.sqlite";

def createTables():
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("CREATE TABLE users (uid number(10) PRIMARY KEY, name varchar(20), password varchar(20));")
    cursor.execute("CREATE TABLE exercise (userid number(10), date date, time time, name varchar, reps number, sets number, weight number, PRIMARY KEY (userid, date, time, name), foreign key (userid) references users(uid));");
    cursor.execute("CREATE TABLE food (userid number(10), date date, time time, name varchar(30), calories number, protein number, carbs number, fats number, PRIMARY KEY (userid, date, time, name), foreign key (userid) references users(uid));");
    cursor.execute("CREATE TABLE sleep (userid number(10), date date, startTime time, endTime time, PRIMARY KEY (userId, date, startTime), foreign key (userid) references users(uid));");
    cursor.execute("CREATE TABLE water (userid number(10), date date, time time, amount number, primary key (userid, date, time), foreign key (userid) references users(uid));");
    cursor.execute("CREATE TABLE stress (userid number(10), date date, rating number, primary key (userid, date), foreign key (userid) references users(uid));");
    conn.commit();
    conn.close();
    
def insertUser(uid, name, password):
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("INSERT INTO users VALUES ({ui}, {un}, {up});".format(ui=uid, un=name, up=password));
    conn.commit();
    conn.close();
    
def insertExercise(uid, time, date, name, reps, sets, weight):
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("INSERT INTO exercise VALUES ({ui}, {et}, {ed}, {en}, {er}, {es}, {ew});".format(ui=uid, et=time, ed=date, en=name, er=reps, es=sets, ew=weight));
    conn.commit();
    conn.close();
    
def insertFood(uid, date, time, name, calories, protein, carbs, fats):
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("INSERT INTO food VALUES ({ui}, {fd}, {ft}, {fn}, {fc}. {fp}, {fcr}, {ff});".format(ui=uid, fd=date, ft=time, fn=name, fc=calories, fp=protein, fcr=carbs, ff=fats));
    conn.commit();
    conn.close();
    
def insertSleep(uid, name, password):
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("INSERT INTO sleep VALUES ({ui}, {un}, {up});");
    conn.commit();
    conn.close();
    
def insertStress(uid, name, password):
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("INSERT INTO stress VALUES ({ui}, {un}, {up});");
    conn.commit();
    conn.close();
    
def insertWater(uid, name, password):
    conn = sqlite3.connect(database_name);
    cursor = conn.cursor();
    cursor.execute("INSERT INTO water VALUES ({ui}, {un}, {up});");
    conn.commit();
    conn.close();
    
def processHistory(uid):
    conn = sqlite3.connect(database_name);
    c = conn.cusor();
    mostCorr = 0;
    mostCorrFactor = "";
    mostCorrResult = "";
    tablef = "sleep";
    tabler = "stress"
    c.execute("SELECT startTime, endTime FROM sleep WHERE uid={uid} ORDER BY date".format(uid=uid));
    resultF = [];
    for x in range(0,c.rowcount):
        resultF.append(c.fetchone()[1] - c.fetchone()[0]);
    c.execute("SELECT number FROM stress WHERE uid={uid} ORDER BY date".format(uid=uid));
    resultR = [];
    for x  in range(0,c.rowcount):
        resultR.append(c.fetchone()[0]);
    correlation = numpy.correlate(resultF, resultR);
    if (mostCorr< abs(correlation)):
        mostCorr = correlation;
        mostCorrFactor = tablef;
        mostCorrResult = tabler;
    #Repeat add nauseum
    tablef = "sleep";
    tabler = "stress"
    c.execute("SELECT startTime, endTime FROM sleep WHERE uid={uid} ORDER BY date".format(uid=uid));
    resultF = [];
    for x in range(0,c.rowcount):
        resultF.append(c.fetchone()[1] - c.fetchone()[0]);
    correlation = numpy.correlate(resultF, resultR);
    if (mostCorr< abs(correlation)):
        mostCorr = correlation;
        mostCorrFactor = tablef;
        mostCorrResult = tabler;
    
    
    
    
    
    
    
    
    
    
