import re

ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

def findIP(textPath):
  with open(textPath, 'r') as myfile:
    data=myfile.read()
    findIPList = re.findall(ipPattern,data)

    return findIPList
