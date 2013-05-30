# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    
    total_viruses_d300 = simDelayTreat(300, numTrials)
    total_viruses_d150 = simDelayTreat(150, numTrials)
    total_viruses_d75 = simDelayTreat(75, numTrials)
    total_viruses_d0 = simDelayTreat(0, numTrials)
    pylab.figure()
    pylab.subplot(411)
    pylab.title(str(numTrials) + ' trials of ' + 'different timesteps delayed treatment')
    pylab.hist(total_viruses_d300, bins = 21)
    pylab.xlabel('delay 300 timesteps, Total Virus Population')
    pylab.ylabel('Num. of trials')
    #pylab.label('delay 300')
    pylab.subplot(412)
    pylab.xlabel('delay 150 timesteps, Total Virus Population')
    pylab.ylabel('Num. of trials')
    #pylab.label('delay 150')
    #pylab.legend()
    pylab.hist(total_viruses_d150, bins = 21)
    pylab.subplot(413)
    pylab.xlabel('delay 75 timesteps, Total Virus Population')
    pylab.ylabel('Num. of trials')
    #pylab.label('delay 150')
    #pylab.legend()
    pylab.hist(total_viruses_d75, bins = 21)
    pylab.subplot(414)
    pylab.xlabel('delay 0 timesteps, Total Virus Population')
    pylab.ylabel('Num. of trials')
    #pylab.label('delay 150')
    #pylab.legend()
    pylab.hist(total_viruses_d0, bins = 21)
    pylab.show()


def simDelayTreat(delay, numTrials):
    numViruses = 100
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    maxPop = 1000
    end_tot_vir = []
    for i in range(numTrials):
        initial_viruses = []
        for j in range(numViruses):
            initial_viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient1(initial_viruses, maxPop)
        drugResist = ['guttagonol']
        for k in range(delay+150):
            if k == delay:
                patient.addPrescription('guttagonol')
                #below is for non-compliant patient
                #if random.random() < 0.2:
                #    patient.removePrescription('guttagonol')
                                
            reside_viruses = patient.update()
        end_tot_vir.append(reside_viruses)
    return end_tot_vir


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    total_viruses_d300 = simDelayBetweenTreat(300, numTrials)
    print 'Simulation of 300 timesteps delay between drugs done!!'
    total_viruses_d150 = simDelayBetweenTreat(150, numTrials)
    print 'Simulation of 150 timesteps delay between drugs done!!'
    total_viruses_d75 = simDelayBetweenTreat(75, numTrials)
    print 'Simulation of 75 timesteps delay between drugs done!!'
    total_viruses_d0 = simDelayBetweenTreat(0, numTrials)
    print 'Simulation of 0 timesteps delay between drugs done!!'
    pylab.figure()
    pylab.subplot(411)
    pylab.title(str(numTrials) + ' trials of ' + 'different timesteps delayed between drugs')
    pylab.hist(total_viruses_d300, bins = 16)
    pylab.xlabel('delay 300 timesteps before using 2nd drug , Total Virus Population')
    pylab.ylabel('Num. of trials')
    pylab.xlim(0, 600)
    pylab.subplot(412)
    pylab.hist(total_viruses_d150, bins = 16)
    pylab.xlabel('delay 150 timesteps before using 2nd drug , Total Virus Population')
    pylab.ylabel('Num. of trials')
    pylab.xlim(0, 600)
    pylab.subplot(413)
    pylab.hist(total_viruses_d75, bins = 16)
    pylab.xlabel('delay 75 timesteps before using 2nd drug , Total Virus Population')
    pylab.ylabel('Num. of trials')
    pylab.xlim(0, 600)
    pylab.subplot(414)
    pylab.hist(total_viruses_d0, bins = 16)
    pylab.xlabel('delay 0 timesteps before using 2nd drug , Total Virus Population')
    pylab.ylabel('Num. of trials')
    pylab.xlim(0, 600)
    pylab.show()
 
    
def simDelayBetweenTreat(delay, numTrials):
    numViruses = 100
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    maxPop = 1000
    end_tot_vir = [0.0] * numTrials
    for i in range(numTrials):
        initial_viruses = [ResistantVirus(maxBirthProb, clearProb,
                                          resistances, mutProb)
                           for _ in range(numViruses)]
        patient = TreatedPatient1(initial_viruses, maxPop)
        drugResist = ['guttagonol', 'grimpex']
        for k in range(150+delay+150):
            if k >= 150:
                patient.addPrescription('guttagonol')
                #below is for non-compliant patient
                if random.random() < 0.2:
                    patient.removePrescription('guttagonol')
            if k >= 150+delay:
                patient.addPrescription('grimpex')
                #below is for non-compliant patient
                if random.random() < 0.2:
                    patient.removePrescription('grimpex')
                                
            reside_viruses = patient.update()
        end_tot_vir[i] += reside_viruses
    return end_tot_vir
