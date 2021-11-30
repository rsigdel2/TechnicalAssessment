#treat center of hoop as origin

import csv

#team a variables
teamA = []
Ax = []
Ay = []
C3countA = 0
C3MadeA = 0
NC3countA = 0
NC3MadeA = 0
TwoPointCountA = 0
TwoPointMadeA = 0
totalShotsA = 0
totalMadeA = 0

#team b variables
teamB = []
Bx = []
By = []
C3countB = 0
C3MadeB = 0
NC3countB = 0
NC3MadeB = 0
TwoPointCountB = 0
TwoPointMadeB = 0
totalShotsB = 0
totalMadeB = 0

with open('shots_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for column in csv_reader:

        #organize what each column is
        team = column[0]
        Xcord = column[1]
        Ycord = column[2]
        madeShot = column[3]

        A = "Team A"
        B = "Team B"
        if team == A:
            if float(madeShot) == 1:
                totalMadeA += 1
            #store coordinates for team A
            XcordA = float(Xcord)
            YcordA = float(Ycord)
            #store coordinates into list
            Ax.append(XcordA)
            Ay.append(YcordA)
            #if its not a shot attempted below 7.8 feet
            if YcordA > 7.8:
                #checks if its a 3 or not only using y cord because it is going to be independent of x
                if YcordA > 23.75:
                    #keeps track of made shots in each zone
                    if float(madeShot) == 1:
                        totalShotsA += 1
                        NC3countA += 1
                        NC3MadeA += 1
                        #print("non corner 3 made", NC3MadeA)
                    else:
                        totalShotsA += 1
                        NC3countA += 1
                        #print("non corner 3 missed")
                #check if 3 or not also using x because it is dependent on y
                if YcordA > 7.8 and XcordA > 23.75:
                    if float(madeShot) == 1:
                        totalShotsA += 1
                        NC3countA += 1
                        NC3MadeA += 1
                        #print("non corner 3 made", NC3MadeA)
                    else:
                        totalShotsA += 1
                        NC3countA += 1
                        #print("non corner 3 missed")
                if YcordA < 23.75:
                    if float(madeShot) == 1:
                        totalShotsA += 1
                        TwoPointCountA += 1
                        TwoPointMadeA += 1
                        #print("2 point made", TwoPointMadeA)
                    else:
                        totalShotsA += 1
                        TwoPointCountA += 1
                        #print("2 point attempt missed")
            #check for corner 3s
            if YcordA <= 7.8:
                #will be independent of y cord because its below 7.8
                if abs(XcordA) > 22:
                    if float(madeShot) == 1:
                        totalShotsA += 1
                        C3MadeA += 1
                        C3countA += 1
                        #print("corner 3 made", C3MadeA)
                    else:
                        totalShotsA += 1
                        C3countA += 1
                        #print("corner 3 missed")
                if abs(XcordA) < 22:
                    if float(madeShot) == 1:
                        totalShotsA += 1
                        TwoPointMadeA += 1
                        TwoPointCountA += 1
                        #print("2 point made", TwoPointMadeA)
                    else:
                        TwoPointCountA += 1
                        totalShotsA += 1
                        #print("2 point missed")

        #team b
        if B == team:
            if float(madeShot) == 1:
                totalMadeB += 1
            #store coordinates for team B
            XcordB = float(Xcord)
            YcordB = float(Ycord)
            #store coordinates into list
            Bx.append(XcordB)
            By.append(YcordB)
            #if its not a shot attempted below 7.8 feet
            if YcordB > 7.8:
                #checks if its a 3 or not only using y cord because it is going to be independent of x
                if YcordB > 23.75:
                    #keeps track of made shots in each zone
                    if float(madeShot) == 1:
                        totalShotsB+= 1
                        NC3countB += 1
                        NC3MadeB += 1
                        #print("Team B: non corner 3 made", NC3MadeB)
                    else:
                        totalShotsB += 1
                        NC3countB += 1
                        #print("Team B: non corner 3 missed")
                #check if 3 or not also using x because it is dependent on y
                if YcordB > 7.8 and XcordB > 23.75:
                    if float(madeShot) == 1:
                        totalShotsB += 1
                        NC3countB += 1
                        NC3MadeB += 1
                        #print("Team B: non corner 3 made", NC3MadeB)
                    else:
                        totalShotsB += 1
                        NC3countB += 1
                        #print("Team B: non corner 3 missed")
                if YcordB < 23.75:
                    if float(madeShot) == 1:
                        totalShotsB += 1
                        TwoPointCountB += 1
                        TwoPointMadeB += 1
                        #print("Team B: 2 point made", TwoPointMadeB)
                    else:
                        totalShotsB += 1
                        TwoPointCountB += 1
                        #print("Team B: 2 point attempt missed")
            #check for corner 3s
            if YcordB <= 7.8:
                #will be independent of y cord because its below 7.8
                if abs(XcordB) > 22:
                    if float(madeShot) == 1:
                        totalShotsB += 1
                        C3MadeB += 1
                        C3countB += 1
                        #print("Team B: corner 3 made", C3MadeB)
                    else:
                        totalShotsB += 1
                        C3countB += 1
                        #print("Team B: corner 3 missed")
                if abs(XcordB) < 22:
                    if float(madeShot) == 1:
                        totalShotsB += 1
                        TwoPointMadeB += 1
                        TwoPointCountB += 1
                        #print("Team B: 2 point made", TwoPointMadeB)
                    else:
                        TwoPointCountB += 1
                        totalShotsB += 1
                        #print("Team B: 2 point missed")
    
#team A shot distribution and eFG
    #Team A percentage for shots
    CornerShotA = float(C3countA) / float(totalShotsA)
    TwoPointShotA = float(TwoPointCountA) / float(totalShotsA)
    NonCornerShotA = float(NC3countA) / float(totalShotsA)

    #Team B percentage for shots
    CornerShotB = float(C3countB) / float(totalShotsB)
    TwoPointShotB = float(TwoPointCountA) / float(totalShotsB)
    NonCornerShotB = float(NC3countB) / float(totalShotsB) 

    #Team A eFG
    eFGcornerA = (float(C3MadeA) + (.5 * float(C3MadeA)))/ float(C3countA)
    eFGTwoPointA = float(TwoPointMadeA) / float(TwoPointCountA)
    eFGNCA = (float(NC3MadeA) + (.5 * float(NC3MadeA))) / float(NC3countA)
    #Team B eFG
    eFGcornerB = (float(C3MadeB) + (.5 * float(C3MadeB))) / float(C3countB)
    eFGTwoPointB = float(TwoPointMadeB) / float(TwoPointCountB)
    eFGNCB = (float(NC3MadeB) + (.5 * float(NC3MadeB))) / float(NC3countB)

    #print statement for team A
    print('Team A attempted ' + format(CornerShotA, '.3%') + ' of their shots on corner threes, ' +
    format(NonCornerShotA, '.3%') + ' of their shots on normal threes, and ' + format(TwoPointShotA, '.3%') + ' on two point shots.')

    print('Team A had an eFG of ' + format(eFGcornerA,'.3%') + ' from the corner on ' + str(C3countA) + ' attempt(s), they had an eFG of ' 
    + format(eFGNCA, '.3%') + ' on regular three pointers with ' + str(NC3countA) + ' attempt(s),')

    print( 'and they had an eFG of ' + format(eFGTwoPointA, '.3%') +
    ' on ' + str(TwoPointCountA) + ' attempt(s) on two pointers.' )
    print(' ')

    #print statement for team B
    print('Team B attempted ' + format(CornerShotB, '.3%') + ' of their shots on corner threes, ' +
    format(NonCornerShotB, '.3%') + ' of their shots on normal threes, and ' + format(TwoPointShotB, '.3%') + ' on two point shots.')

    print('Team B had an eFG of ' + format(eFGcornerB,'.3%') + ' from the corner on ' + str(C3countB) + ' attempt(s), they had an eFG of ' 
    + format(eFGNCB, '.3%') + ' on regular three pointers with ' + str(NC3countB) + ' attempt(s),')

    print( 'and they had an eFG of ' + format(eFGTwoPointB, '.3%') +
    ' on ' + str(TwoPointCountB) + ' attempt(s) on two pointers.' )
    


        
