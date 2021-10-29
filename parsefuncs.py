# Function to fill days for LEC, LAB, etc...
# 'x' is the json object 'meetingTime'
def add_days(x):
    days = ""
    
    noDaysProvided = True
    
    # Add all present days and keep track of whether the lab has any days provided
    if x['monday']:
        days += "M"
        noDaysProvided = False
    if x['tuesday']:
        days += "T"
        noDaysProvided = False
    if x['wednesday']:
        days += "W"
        noDaysProvided = False
    if x['thursday']:
        days += "R"
        noDaysProvided = False
    if x['friday']:
        days += "F"
        noDaysProvided = False
    if x['saturday']:
        days += "S"
        noDaysProvided = False
    if x['sunday']:
        days += "U"
        noDaysProvided = False
    
    # if the lab has no days, write N/A
    if noDaysProvided:
        days += "N/A"
    
    # Separate days from time for .csv
    days += ","
    
    if x['beginTime']:
        days += x["beginTime"] + " - " + x["endTime"]
    else:
        days += "N/A"
    return days


# Quick function to add lab days and times
def add_lab(meetingsFaculty):
    val = ""
    
    # search through all "meetingTimes" to find type "LAB"
    for facultyObject in meetingsFaculty: 
        x = facultyObject["meetingTime"]
        if x["meetingType"] == "LAB":
            val += add_days(x)
            return val
    
    # This course has no LAB so n/a for DAYS, TIMES
    val += "N/A,N/A"
    return val


# Quick function to add lecture days and times
def add_lec(meetingsFaculty):
    val = ""
    for facultyObject in meetingsFaculty:
        x = facultyObject["meetingTime"]
        if x["meetingType"] == "LEC":
            val += add_days(x)
            return val
    
    # This course has no LECTURE so n/a for DAYS, TIMES
    val += "N/A,N/A"
    return val


# Function to fetch room number for labs because some classes do not have room number :)
def add_room(meetingsFaculty):
    room = ""
    noLab = True
    for facultyObject in meetingsFaculty:
        x = facultyObject['meetingTime']
        if (x['meetingType'] == 'LAB'):
            noLab = False
            if x['building'] == 'ONLINE':
                room += "ONLINE"
            elif x['building'] == None:
                room += "N/A"
            else:
                room += x['building'] + " " + str(x['room'])
            break
    
    # Course has no LAB so LAB_ROOM is N/A
    if noLab:
        room += "N/A"
        
    return room

# Function to fetch instructor because some classes do not list a professor :)
def add_prof(faculty):
    prof = ""
    for x in faculty:
        prof += x['displayName'] if x['displayName'] else "N/A"
        break
    return prof