#making an attendance tracker
import csv
import sys


class color:
    RESET    = '\033[0m'
    BLACK    = '\033[30m'
    RED      = '\033[31m'
    GREEN    = '\033[32m'
    YELLOW   = '\033[33m'
    BLUE     = '\033[34m'
    MAGENTA  = '\033[35m'
    CYAN     = '\033[36m'
    WHITE    = '\033[97m'

#open attendance file
#create buffer that will store all last names of people who attended
buff = ''


count = 0; #used to skip certain lines
with open('OrganizationEventAttendances.csv',mode='r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in csvfile:
        if(count < 5): #need to skip first lines because they don't contain anything useful and break code below it
            count = count + 1
            continue
        temp = row.split(',') #make one string multiple strings in a list
        buff = buff + temp[1] #add last name to buffer



#open roster file now to compare who was here and not
roster = open('roster.txt', 'r')
line = roster.readline() #get first line of roster
while line:
    temp = line.split(' ') #split into first and last names in list format

    #print to console in color format
    if(buff.find(temp[1].rstrip()) != -1):
        print(color.GREEN + temp[0] + ' ' + temp[1] + color.RESET)
        
    else:
        print(color.RED + temp[0] + ' ' + temp[1])

    line = roster.readline() #iterate next line

#close files
csvfile.close()
roster.close()
