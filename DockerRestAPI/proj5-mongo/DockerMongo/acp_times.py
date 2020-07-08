"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""



def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    table = [(0,0), (200,34), (400,32), (600,30), (1000,28)]
    if control_dist_km > table[4][0]:
        control_dist_km = table[4][0]
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km
    for i in range(len(table)-1):
         
        if control_dist_km > table[i][0]:

            # Get Brevet Start Time Hours and Minutes
            startHours = int(brevet_start_time[11:13])
            startMinutes = int(brevet_start_time[14:16])

            # Get the time to convert to minutes and hours to add to start times
            if control_dist_km > table[i][0] and control_dist_km < table[i+1][0]:
                time = ((control_dist_km-(table[i][0]))/table[i+1][1]) 
            else:
                time = (200/table[i+1][1])
            controlHours = int(time)
            controlMinutes = round((time - controlHours)*60)

            # Create totals to display on the webpage
            totalHours = controlHours+startHours
            totalMinutes = controlMinutes+startMinutes
            if (totalMinutes) >= 60:
                totalHours+=1
                totalMinutes -= 60
            day = int(brevet_start_time[8:10])
            if totalHours > 23:
               day += 1
               totalHours -= 24

            totalMinutes = str(totalMinutes)
            totalHours = str(totalHours)

            if (len(str(day))==1):
                day = brevet_start_time[:8]+'0'+str(day)
            else:
                day = brevet_start_time[:8]+str(day)
            if (len(str(totalHours)) == 1):
                totalHours = '0'+totalHours
            if (len(str(totalMinutes))== 1):
                totalMinutes = '0'+totalMinutes
                
            brevet_start_time = day + ' ' + (totalHours+':'+totalMinutes)   
            if control_dist_km > table[i][0] and control_dist_km < table[i+1][0]:
                break
    return brevet_start_time 



def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    table = [(0,0), (200,15), (400,15), (600,15), (1000,11.428)]
    if control_dist_km > table[4][0]:
        control_dist_km = table[4][0]
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km
    for i in range(len(table)-1):
         
        if control_dist_km > table[i][0]:

            # Get Brevet Start Time Hours and Minutes
            startHours = int(brevet_start_time[11:13])
            startMinutes = int(brevet_start_time[14:16])

            # Get the time to convert to minutes and hours to add to start times
            if control_dist_km > table[i][0] and control_dist_km < table[i+1][0]:
                time = ((control_dist_km-(table[i][0]))/table[i+1][1]) 
            else:
                time = (200/table[i+1][1])
            controlHours = int(time)
            controlMinutes = round((time - controlHours)*60)

            # Create totals to display on the webpage
            totalHours = controlHours+startHours
            totalMinutes = controlMinutes+startMinutes
            if (totalMinutes) >= 60:
                totalHours+=1
                totalMinutes -= 60
            day = int(brevet_start_time[8:10])
            if totalHours > 23:
               day += 1
               totalHours -= 24

            totalMinutes = str(totalMinutes)
            totalHours = str(totalHours)

            if (len(str(day))==1):
                day = brevet_start_time[:8]+'0'+str(day)
            else:
                day = brevet_start_time[:8]+str(day)
            if (len(str(totalHours)) == 1):
                totalHours = '0'+totalHours
            if (len(str(totalMinutes))== 1):
                totalMinutes = '0'+totalMinutes
                
            brevet_start_time = day + ' ' + (totalHours+':'+totalMinutes)   
            if control_dist_km > table[i][0] and control_dist_km < table[i+1][0]:
                break
    return brevet_start_time 
