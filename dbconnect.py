import MySQLdb
import requests
import json
import pprint

ip_table_columns = ['id', 'city', 'region_code', 'region_name', 'ip', 'time_zone',\
                 'longitude', 'metro_code', 'latitude', 'country_code', 'zip_code']
def dbconnect():
    try:
        db = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='myweb'
        )
        #print "Connected to the database ..."

        return db
    except Exception as e:
        print "Can't connect to database"
        quit

def db_init_ip_table(table_name):
    sql_query = 'CREATE TABLE IF NOT EXISTS ' + table_name + '(\
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
                city VARCHAR(30),\
                region_code VARCHAR(10),\
                region_name VARCHAR(30),\
                ip VARCHAR(30),\
                time_zone VARCHAR(30),\
                longitude FLOAT,\
                metro_code VARCHAR(30),\
                latitude FLOAT,\
                country_code VARCHAR(5),\
                country_name VARCHAR(30),\
                zip_code VARCHAR(10)\
                )'
    
    db = dbconnect()
    cursor = db.cursor()
    cursor.execute(sql_query)
    cursor.close()

def db_insert(table_name, column_names_str, values_str):
    try:
        db = dbconnect()
        cursor = db.cursor()
        sql_query = 'INSERT INTO ' + table_name + ' (' + column_names_str + \
                    ') VALUES ('   + values_str + ')'
        #print sql_query
        
        cursor.execute(sql_query)
        db.commit()
        cursor.close()
    except Exception as e:
        print e


def create_table_from_iplist(IPList, table_name):
    db_init_ip_table(table_name)
    
    IPCnt=0
    for line in IPList:
      IPCnt=IPCnt+1
      print "Processing IP " + str(IPCnt) + '...'
      # Assign an IP as a single line from the given file
      IP = line

      PageRequest = 'http://freegeoip.net/json/' + ''.join(IP)
      # Get rid of the newline character at the end by rstrip()
      data = requests.get(PageRequest.rstrip())

      # Parse the collected json text into data frame
      info = json.loads(data.text)

      # Get column names and values in string
      if IPCnt==1:
        column_names = info.keys()
        column_names_str = ','.join(column_names)


      values = info.items()
      values_list = list()
      for i in range (0,len(column_names)):
          try:
              values_list.append('\''+ str(values[i][1]) + '\'')

          except UnicodeEncodeError:
              values_list.append('\''+ '\'')
        
      values_str = ','.join(values_list)

      
      db_insert(table_name,column_names_str,values_str)


def db_show(table_name):
    db = dbconnect()
    cursor = db.cursor()

    ## SHOW COLUMNS
    sql_query = 'SHOW COLUMNS FROM ' + table_name
    cursor.execute(sql_query)
    print [column[0] for column in cursor.fetchall()]

    ## SHOW DATA
    cursor.execute('SELECT * from ' + table_name)
    row = cursor.fetchone()
    while row is not None:
        print ", ".join([str(c) for c in row])
        row = cursor.fetchone()

    cursor.close()

def db_search(table_name, column_name, keyword):
    db = dbconnect()
    cursor = db.cursor()

    if column_name is not None:
        sql_query = 'SELECT * from ' + table_name + ' WHERE ' + \
                    column_name + ' LIKE \'%' + keyword + '%\''
    else:
        sql_query = 'SELECT * from ' + table_name + ' WHERE '

        for col in ip_table_columns:
            sql_query = sql_query + col + ' LIKE \'%' + keyword + '%\''
            if col != ip_table_columns[-1]:
                sql_query = sql_query + ' OR '

    #print sql_query

    cursor.execute(sql_query)
    #####
    row = cursor.fetchone()
    if row is not None:
        while row is not None:
            print ", ".join([str(c) for c in row]) + '\n'
            row = cursor.fetchone()
    else:
        print "NOTHING FOUND!"
        
    cursor.close()
    
