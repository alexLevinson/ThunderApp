#wiritten by Alex Levinson for OKC Thunder
import csv

fgm_C3_A = fga_C3_A = 0     #vars to hold num of made & attempted corner 3s by team A
fgm_NC3_A = fga_NC3_A = 0   #count vars for non-corner 3s
fgm_2PT_A = fga_2PT_A = 0   #vars for 2 pofloaters

#same vars but for team B
fgm_C3_B = fga_C3_B = fgm_NC3_B = fga_NC3_B = fgm_2PT_B = fga_2PT_B = 0

fga_tot_A = fga_tot_B = 0   #hold total amount of shots per team (used for verification)


with open("shots_data.csv", 'r') as csvfile:    #open file
    reader = csv.reader(csvfile)                #create reader
    next(reader)                                #iterate past first row, since it contains headers and not actual data
    for row in reader:
        team = (row[0][5] == 'A')   #boolean team is 1 if team A, 0 if team B
        
        if team:    
            fga_tot_A += 1     #this means that the shot was taken by team A, so increment fga_tot_A
            if abs(float(row[1])) > 22 and float(row[2]) < 7.8:    #all shots to get past this if are corner 3s by team A
                fga_C3_A += 1       #increment C3 fga var
                if float(row[3]) == 1:     #if shot was made, also increment C3 fgm var
                    fgm_C3_A += 1
            elif (float(row[1]) ** 2 + float(row[2]) ** 2) > 23.75 ** 2:  #use pythagorean theorem to test if shot is behind the 3pt arc
                fga_NC3_A += 1      #increment vars
                if float(row[3]) == 1:
                    fgm_NC3_A += 1
            else:                   #if shot isnt a 3, then it must be a 2
                fga_2PT_A += 1      #increment vars
                if float(row[3]) == 1:
                    fgm_2PT_A += 1


        else:   #same logic as with team A, just update team B's vars
            fga_tot_B += 1
            if abs(float(row[1])) > 22 and float(row[2]) < 7.8:
                fga_C3_B += 1       
                if float(row[3]) == 1:     
                    fgm_C3_B += 1
            elif (float(row[1]) ** 2 + float(row[2]) ** 2) > 23.75 ** 2:  
                fga_NC3_B += 1     
                if float(row[3]) == 1:
                    fgm_NC3_B += 1
            else:                   
                fga_2PT_B += 1      
                if float(row[3]) == 1:
                    fgm_2PT_B += 1

assert (fga_C3_A + fga_NC3_A + fga_2PT_A) == fga_tot_A  #make sure the zone totals add up to the team total
assert (fga_C3_B + fga_NC3_B + fga_2PT_B) == fga_tot_B

#print data, performing efg and shot distr calculations
print("team A: corner 3s -- efg: " + str((1.5 * fgm_C3_A)/fga_C3_A) + " distr: " + str(fga_C3_A/fga_tot_A))
print("team A: non-corner 3s -- efg: " + str((1.5 * fgm_NC3_A)/fga_NC3_A) + " distr: " + str(fga_NC3_A/fga_tot_A))
print("team A: 2s -- efg: " + str(fgm_2PT_A/fga_2PT_A) + " distr: " + str(fga_2PT_A/fga_tot_A))
print("----------------")
print("team B: corner 3s -- efg: " + str((1.5 * fgm_C3_B)/fga_C3_B) + " distr: " + str(fga_C3_B/fga_tot_B))
print("team B: non-corner 3s -- efg: " + str((1.5 * fgm_NC3_B)/fga_NC3_B) + " distr: " + str(fga_NC3_B/fga_tot_B))
print("team B: 2s -- efg: " + str(fgm_2PT_B/fga_2PT_B) + " distr: " + str(fga_2PT_B/fga_tot_B))




        
