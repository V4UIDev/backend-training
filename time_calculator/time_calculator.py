import re

def add_time(start, duration, day="false"):
    timeArr = re.findall('[0-9]+', start)
    durationArr = re.findall('[0-9]+', duration)
   
   
    hour = int(timeArr[0])
    minute = int(timeArr[1])

    durHour = int(durationArr[0])
    durMinute = int(durationArr[1])
    dayAnnounce = ""

    morningAfternoon = re.findall('[A-Z]+', start)
    morningAfternoon = morningAfternoon[0]
    day = day.lower()
    dayCounter = 0

    if day == "monday":
        weekNumber = 1
    elif day == "tuesday":
        weekNumber = 2
    elif day == "wednesday":
        weekNumber = 3
    elif day == "thursday":
        weekNumber = 4
    elif day == "friday":
        weekNumber = 5
    elif day == "saturday":
        weekNumber = 6
    elif day == "sunday":
        weekNumber = 7
    else: weekNumber = 0


    
    
    
    if morningAfternoon == "PM":
        hour = hour + 12

    while durMinute > 0:
        minute = minute + 1
        durMinute = durMinute - 1
        if minute > 59:
            hour = hour + 1
            minute = 0
            if hour > 23:
                dayCounter = dayCounter + 1
                hour = 0

    while durHour > 0:
        hour = hour + 1
        durHour = durHour - 1
        if hour > 23:
            dayCounter = dayCounter + 1
            hour = 0

    if dayCounter == 1:
        dayAnnounce = " (next day)"
    elif dayCounter > 1:
        dayAnnounce = " (" + str(dayCounter) + " days later" + ")"

    if hour == 12:
        morningAfternoon = "PM"
    elif hour > 12:
        morningAfternoon = "PM"
        hour = hour - 12
    elif hour < 12 and hour > 0:
        morningAfternoon = "AM"
    elif hour == 0:
        morningAfternoon = "AM"
        hour = hour + 12

    dayCounterTemp = dayCounter

    if minute < 10:
        minute = "0" + str(minute)
    else: minute = str(minute)

    hour = str(hour)

   
    if weekNumber != 0:
        while dayCounterTemp > 0:
            weekNumber = weekNumber + 1
            dayCounterTemp = dayCounterTemp - 1
            if weekNumber > 7:
                weekNumber = 1

        
        if weekNumber == 1:
            WdAnnounce = "Monday"
        elif weekNumber == 2:
            WdAnnounce = "Tuesday"
        elif weekNumber == 3:
            WdAnnounce = "Wednesday"
        elif weekNumber == 4:
            WdAnnounce = "Thursday"
        elif weekNumber == 5:
            WdAnnounce = "Friday"
        elif weekNumber == 6:
            WdAnnounce = "Saturday"
        elif weekNumber == 7:
            WdAnnounce = "Sunday"

        announce = hour + ":" + minute + " " + morningAfternoon + ", " + WdAnnounce + dayAnnounce

    else: announce = hour + ":" + minute + " " + morningAfternoon + "" + dayAnnounce

   
    print(announce)





    return announce