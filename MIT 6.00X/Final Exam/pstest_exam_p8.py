import pylab, numpy
def generateData():
    a = 1.03
    b = 0.9
    c = 23.45
    yVals = []
    xVals = range(-5, 5)
    for x in xVals:
        yVals.append(a*x**2 + b*x + c)
    return xVals, yVals

def findOrder(xVals, yVals, accuracy = 1.0e-1):
    X = pylab.array(xVals)
    Y = pylab.array(yVals)
    find = True
    n = 0
    while find:
        #n += 1
        Z = pylab.polyfit(xVals, yVals, n, None, True)
        '''
        est = 0.0
        estVal = []
        for x in xVals:
            for i in range(len(Z[0])):
                est += Z[0][i] * (x**(len(Z[0])-i-1))
            estVal.append(est)
        error = 0.0
        for j in range(len(yVals)):
            error += (estVal[j] - yVals[j]) ** 2
        if error <= accuracy:
            find = False
            print 'order ', n, 'is good enough'
        '''               
        if Z[1] <= accuracy:
            find = False
            print 'order ', n, 'is good enough'
        n += 1
    print (Z[0])
    return Z[0]

xData, yData = generateData()
findOrder(xData, yData, accuracy = 1.0e-1)
#findOrder([0, 0, 0, 0, 0], [3, 3, 3, 3, 3], accuracy = 1.0e-1)
#print (Z)
#print (Z[1])
