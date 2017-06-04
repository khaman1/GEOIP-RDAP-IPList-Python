from findIP import *
from dbconnect import *
from cli import *
#################################################
#################################################
## Read IP from the give text file
## Collect IPs into the type DataFrame
## The IP list is generated from the software "IP List Generator" found at 'http://optinsoft.net/ipgen2.php'
## Each IP doesn't have to be retrieved all the info. Some might not belong to any country or zipcode.
## Due to the latency to the online server, it's really slow to retrieve GEOIP info so that I constrained to 100 ips in the text file.

## DEFINITIONS ##
TEXT_FILE  = 'Data/Text100.txt'
TABLE_NAME = 'iplist'
#################################################
#################################################


if __name__ == "__main__":
   cli(sys.argv[1:],TABLE_NAME)
   #MyIPList = findIP(TEXT_FILE)
   #create_table_from_iplist(MyIPList,TABLE_NAME)
