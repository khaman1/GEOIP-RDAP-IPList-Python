from ReadIP import *
from findIP import *
from GUI import *
import numpy
#################################################
#################################################
## Read IP from the give text file
## Collect IPs into the type DataFrame
## The IP list is generated from the software "IP List Generator" found at 'http://optinsoft.net/ipgen2.php'
## Each IP doesn't have to be retrieved all the info. Some might not belong to any country or zipcode.
## Due to the latency to the online server, it's really slow to retrieve GEOIP info so that I constrained to 100 ips in the text file.

#MyIPList = findIP('Text5000.txt')
MyIPList = findIP('Text100.txt')

MyDataFrame = ReadIPFromList(MyIPList,1)

## Get the header for each columns
## Convert every row of the DataFrame into a tuple
column_header = tuple(MyDataFrame.columns.values)
values_list=tuple(MyDataFrame.itertuples(index=False))

########
## There are many attributes from a RDAP info so I don't know what attributes you need
## Just add more columns for values of the RDAP attributes
## We will do the same as the way we get an IP info
#MyRDAP = ReadIPFromList(MyIPList,2)


## Use Tkinter to draw the table
root = Tk()
root.title('Filter List')
## Create the table with column_header and values_list
app = GUI(column_header, values_list)
app.mainloop()







