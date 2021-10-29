import json
import pandas as pd
from parsefuncs import *

# Read file
jsonFile = open('searchResults.json', 'r')
jsonData = jsonFile.read()

# Load the value that contains all relevant data
jsonDict = json.loads(jsonData)
dataDict = jsonDict['data']

# Open file for writing output
outputFile = open("ClassEnrollment.csv", "w")

# Begin by writing to the output .csv file the HEADERS
outputFile.write("Course ID,Sec,Lab Days,Lab Time,Cap,Size,Rem,Instructor,Lab Room\n" )

for classes in dataDict:
    lineCSV = ",".join([ classes["courseNumber"]
                        ,classes["sequenceNumber"]
                        ,add_lab(classes["meetingsFaculty"])
#                         ,add_lec(classes["meetingsFaculty"])
                        ,str(classes["maximumEnrollment"])
                        ,str(classes["enrollment"])
                        ,str(classes["seatsAvailable"])
                        ,add_prof(classes["faculty"])
                        ,add_room(classes["meetingsFaculty"])
                       ])
    lineCSV += "\n"
    outputFile.write(lineCSV)
    
outputFile.close()