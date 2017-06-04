import sys, getopt
from findIP import *
from dbconnect import *

def cli(argv,TABLE_NAME):
  
  try:
      opts, args = getopt.getopt(argv,"hi:s:c:")

  except getopt.GetoptError:
    #print 'test.py -i <inputfile> -o <outputfile>'
    sys.exit(2)

  search_column=''
  keyword=''
  for opt, arg in opts:
    if opt == '-h':
       print 'test.py -i <inputfile> -s <search_keyword> -c <column_to_search>'
       print 'If the input file is available, it will automatically collect ips and their info from the file'
       print 'If there is no column_to_search, it will search it in all columns'
       sys.exit()
    elif opt == '-i':
       inputfile = arg
       MyIPList = findIP(inputfile)
       create_table_from_iplist(MyIPList,TABLE_NAME)
    elif opt == '-s':
      keyword = arg
    elif opt == '-c':
      search_column = arg
      

  if keyword != '':
    if search_column !='':
      if search_column in ip_table_columns:
        db_search(TABLE_NAME,search_column,keyword)
      else:
        print search_column + ' doesn\'t exist in our database. Please choose any from the list\n[' + \
              ','.join(ip_table_columns) +']'
    else:
      db_search(TABLE_NAME,None,keyword)

  for arg in args:
    if arg == 'show':
      db_show(TABLE_NAME)
