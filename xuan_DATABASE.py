from re import I
import sqlite3
#c.execute('''CREATE TABLE STATE( PHONEID TEXT NOT NULL, LOCAL TEXT NOT NULL);''')
#print ("数据表创建成功")
# c.execute(("INSERT INTO CLASS (ID,NAME,ISORNOT) VALUES('123','lyj','30')")
import wechat 
import json


def add_data1(DBname,f_name,ID,name,isornot):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute(("INSERT INTO {F_name} (ID,NAME,ISORNOT) VALUES({Id},{Name},{Isornot})").format(F_name = f_name,Id = ID,Name = name,Isornot = isornot))
     print("数据库添加成功")       
     conn.commit()
     conn.close()
     
def add_data2(DBname,f_name,PHONEID,LOCAL):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute(("INSERT INTO {F_name} (PHONEID,LOCAL) VALUES({Id},{Local})").format(F_name = f_name,Id = PHONEID,Local = LOCAL))
     print("数据库添加成功")       
     conn.commit()
     conn.close()


def get_all_data1(DBname,f_name):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     cursor1 = c.execute("SELECT id, name, ISORNOT from {F_name}".format(F_name = f_name))
     for row in cursor1:
          print ("ID = ", row[0])
          print ("NAME = ", row[1])
          print ("ISORNOT = ", row[2], "\n")
     conn.commit()
     conn.close()

     
     
def get_all_data2(DBname,f_name):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     cursor1 = c.execute("SELECT PHONEID, LOCAL from {F_name}".format(F_name = f_name))
     for row in cursor1:
          print ("PHONEID = ", row[0])
          print ("LOCAL = ", row[1],"\n" )
     conn.commit()
     conn.close()


def get_IS_data1(DBname,f_name,name):
     #NAME = '''"'{a}'" '''.format(a=name)
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     cursor1 = c.execute("SELECT ISORNOT from {F_name} where NAME = {AME}".format(F_name= f_name,AME=name))
     for row in cursor1:
          return row[0]
     conn.commit()
     conn.close()
     
def get_IS_data2(DBname,f_name,phoneid):
     phoneid = '''"'{a}'" '''.format(a=phoneid)
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     cursor1 = c.execute("SELECT LOCAL from {F_name} where PHONEID = {Phoneid}".format(F_name= f_name,Phoneid=phoneid))
     for row in cursor1:
          return int(row[0])
     conn.commit()
     conn.close()



def change_databese1(DBname,f_name,name,ISORNOT):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute("UPDATE {F_name} set ISORNOT = {Isornot} where NAME={NAME}".format(F_name = f_name,NAME=name,Isornot=ISORNOT))
     conn.commit()
     print ("Total number of rows updated :{ABC}".format(ABC=conn.total_changes))
     conn.commit()
     conn.close()
     
def change_databese2(DBname,f_name,phoneid,Local):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute("UPDATE {F_name} set LOCAL = {Local} where PHONEID={Phoneid}".format(F_name = f_name,Phoneid =phoneid,Local = Local))
     conn.commit()
     print ("Total number of rows updated :{ABC}".format(ABC=conn.total_changes))
     conn.commit()
     conn.close()

def del_data1(DBname,f_name,name):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute("DELETE from {F_name} where NAME={NAME}".format(F_name = f_name,NAME=name))
     print ("Total number of rows updated(delete) :{ABC}".format(ABC=conn.total_changes))
     conn.commit()
     conn.close()
     
def del_data2(DBname,f_name,phoneid):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute("DELETE from {F_name} where PHONEID={PHONEID}".format(F_name = f_name,PHONEID=phoneid))
     print ("Total number of rows updated(delete) :{ABC}".format(ABC=conn.total_changes))
     conn.commit()
     conn.close()

def del_f(DBname,f_name):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     c.execute("DELETE from {F_name}".format(F_name = f_name))
     print ("Total number of rows updated(delete) :{ABC}".format(ABC=conn.total_changes))
     conn.commit()
     conn.close()

def get_diaodu_where(where):
     conn = sqlite3.connect('test.db')
     c = conn.cursor()
     cursor1 = c.execute("SELECT PHONEID, LOCAL from STATE")
     i=0
     Local=set()
     for row in cursor1:
          Local.add(row[1])
          i= i+1
     conn.commit()
     conn.close()
     if((where&Local)!=0):
          return list(where - Local)[0]
     else:
          return 0

def savingornot(name):
     #name = '''"'{a}'" '''.format(a=name)
     conn = sqlite3.connect('test.db')
     c = conn.cursor()
     cursor1 = c.execute("SELECT PHONEID from STATE")
     state1=set()
     for row in cursor1:
          state1.add(row[0])
     conn.commit()
     conn.close()
     print("name:"+str(name))
     print("state1",end=':')
     print(list(state1))
     for a in list(state1):
         if name == a[1:-1]:
             return 1
         else:
             return 0

def localtoname(DBname,f_name,Local):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     cursor1 = c.execute("SELECT PHONEID from {F_name} where LOCAL={locall}".format(F_name= f_name,locall=Local))
     for row in cursor1:
          return row[1]
     conn.commit()
     conn.close()

def getisornot_num(num):
     b = get_IS_data1('test','class',"'{num1}'".format(num1 = localtoname('test','STATE',num)))
     return b[1]


def getisornot_name(name):
    name = ''''{n}' '''.format(n=name)
    return get_IS_data1('test','CLASS',"{n}".format(n=name))
    

def get_all_user_zhuce(DBname,f_name):
     conn = sqlite3.connect('{db}.db'.format(db = DBname))
     c = conn.cursor()
     cursor1 = c.execute("SELECT NAME from {F_name}".format(F_name = f_name))
     name=set()
     for row in cursor1:
          name.add(row[0])
     conn.commit()
     conn.close()
     return name

nametoid={
  2: "谢轩"
  }

def get_enroll_state(id):
     b = get_all_user_zhuce('test','CLASS')
     name = nametoid[id]
     if name in b:
          return 1
     else:
          return 0

def idtoname(id):
    return nametoid[id]
#add_data1('test','CLASS',1,"'lyj'",2)
#add_data2('test','STATE',"'陆永佳'","2")
#del_f('test','CLASS')
#del_data('test','CLASS',"'lyj'")
# change_databese1('test','CLASS',"'谢轩'",ISORNOT="11")
# get_all_data1('test','CLASS')


#get_all_data2('test','STATE')
#print(get_data(1))
#print(get_data(2))
#print(get_data(3))
#print(get_data('test','CLASS',"'陆永佳'"))
#print(wechat.get('student_list'))
#del_data2('test','STATE',"'谢轩'")
#add_data2('test','STATE',"'谢轩'",'18')
#print(get_IS_data2('test','STATE',"谢轩"))
#name = "谢轩"
#print(get_IS_data2('test','STATE',name))