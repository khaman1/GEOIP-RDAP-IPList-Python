import pandas
import requests
import json

def ReadIPFromList(IPList, mode):
  ## Create an empty DataFrame
  dataframe = pandas.DataFrame()

  i=0
  for line in IPList:
    i=i+1
    print "Processing IP " + str(i) + '...'
    # Assign an IP as a single line from the given file
    IP = line

    # Request information of the IP via http request
    # Sometimes, due to the Internet connection, the information might not be retrieved or fast
    # I don't know why we can't use 3rd packages but this way is really slow.
    if mode == 1:
      PageRequest = 'http://freegeoip.net/json/' + ''.join(IP)
    elif mode == 2:
      PageRequest = 'http://rdap.arin.net/registry/ip/' + ''.join(IP)

    # Get rid of the newline character at the end by rstrip()
    data = requests.get(PageRequest.rstrip())

    # Parse the collected json text into data frame
    info = json.loads(data.text)
    
    parsed_json_into_dataframe = pandas.io.json.json_normalize(info)

    # Acculumate the dataframe
    dataframe = dataframe.append(parsed_json_into_dataframe)

  return dataframe









def ReadIPFromFile(IPListPath, mode):
  ## Create an empty DataFrame
  dataframe = pandas.DataFrame()
  
  with open(IPListPath) as IPList:
    for line in IPList:
      # Assign an IP as a single line from the given file
      IP = line

      # Request information of the IP via http request
      # Sometimes, due to the Internet connection, the information might not be retrieved or fast
      if mode == 1:
        PageRequest = 'http://freegeoip.net/json/' + ''.join(IP)
      elif mode == 2:
        PageRequest = 'http://rdap.arin.net/registry/ip/' + ''.join(IP)

      # Get rid of the newline character at the end by rstrip()
      data = requests.get(PageRequest.rstrip())

      # Parse the collected json text into data frame
      info = json.loads(data.text)
      
      parsed_json_into_dataframe = pandas.io.json.json_normalize(info)

      # Acculumate the dataframe
      dataframe = dataframe.append(parsed_json_into_dataframe)

  return dataframe
