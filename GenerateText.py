import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))



text=''
with open('Data/IPList5.txt') as IPList:
  for line in IPList:
    IP = line
    RandomText = randomword(random.randrange(100))
    text = text + RandomText + IP

Output = open("Data/Text5.txt", "w")
Output.write(text)
Output.close()
