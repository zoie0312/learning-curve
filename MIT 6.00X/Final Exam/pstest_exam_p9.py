import random, time
def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    # Your Code Here
    geo_dis_not_even = 0
    for i in range(numTrials):
        student_scores = []
        student_race = []
        num_AF = 0
        num_SA = 0
        num_EU = 0
        num_AS = 0
        num_students = 1000
        t1 = time.time()
        for n in range(num_students):
            s = random.random()*100
            #print (n), ' ', (s)
            if n == 0:
                student_scores.append(s)
                student_race.append('AF')
            else:
                if s >= student_scores[0]:
                    student_scores.insert(0, s)
                    if n % 4 == 1:
                        student_race.insert(0, 'EU')
                    elif n % 4 == 2:
                        student_race.insert(0, 'SA')
                    elif n % 4 == 3:
                        student_race.insert(0, 'AS')
                    else:
                        student_race.insert(0, 'AF')
                        #print (student_race)
                        #print (student_scores)
                elif s < student_scores[-1]:
                    student_scores.append(s)
                    if n % 4 == 1:
                        student_race.append('EU')
                    elif n % 4 == 2:
                        student_race.append('SA')
                    elif n % 4 == 3:
                        student_race.append('AS')
                    else:
                        student_race.append('AF')
                        #print (student_race)
                        #print (student_scores)
                else:
                    for i in range(len(student_scores)-1):
                        if s >= student_scores[i+1] and s < student_scores[i]:
                            student_scores.insert(i+1, s)
                            if n % 4 == 1:
                                student_race.insert(i+1, 'EU')
                            elif n % 4 == 2:
                                student_race.insert(i+1, 'SA')
                            elif n % 4 == 3:
                                student_race.insert(i+1, 'AS')
                            else:
                                student_race.insert(i+1, 'AF')
                                #print (student_race)
                                #print (student_scores)
        t2 = time.time()
        #print 't1 = ', (t2 - t1)*1000, 'ms'
        #print (student_scores)
        #print (student_race)
        for j in range(100):
            if student_race[j] == 'AF':
                num_AF += 1
            elif student_race[j] == 'EU':
                num_EU += 1
            elif student_race[j] == 'SA':
                num_SA += 1
            else:
                num_AS += 1
            if num_AF >= 30 or num_EU >= 30 or num_SA >= 30 or num_AS >= 30:
                geo_dis_not_even += 1
                break
        #print 'African: ', num_AF
        #print 'European: ', num_EU
        #print 'South American: ', num_SA
        #print 'Asian: ', num_AS
        #print 't2 = ', (time.time()-t2)*1000, 'ms'
    print 'Probability of 30>/Top100 from same area =', float(geo_dis_not_even)/numTrials
    return float(geo_dis_not_even)/numTrials
                
    '''
            if r < 0.25:
                students.append('AF')
                num_AF += 1
            elif r < 0.5:
                students.append('SA')
                num_SA += 1
            elif r < 0.75:
                students.append('EU')
                num_EU += 1
            else:
                students.append('AS')
                num_AS += 1
            if n == 99:
                print 'Top 100:'
                print 'African: ', num_AF
                print 'European: ', num_EU
                print 'South American: ', num_SA
                print 'Asian: ', num_AS
        print 'Total 1000'
        print 'African: ', num_AF
        print 'European: ', num_EU
        print 'South American: ', num_SA
        print 'Asian: ', num_AS
   '''
