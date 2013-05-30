import pylab, numpy
def generateData():
    a = 1.0
    b = 1.0
    c = 1.0
    yVals = []
    xVals = range(-20, 20)
    for x in xVals:
        yVals.append(a*x**2 + b*x + c)
    return xVals, yVals

def findOrder(xVals, yVals, accuracy = 1.0e-1):
    X = pylab.array(xVals)
    Y = pylab.array(yVals)
    find = True
    n = 0
    while find:
        n += 1
        Z = pylab.polyfit(X, Y, n, None, True)
        if Z[1] <= accuracy:
            find = False
            print 'order ', n, 'is good enough'
    print (Z[0])
    return Z[0]

xData, yData = generateData()
findOrder(xData, yData, accuracy = 1.0e-1)
#print (Z)
#print (Z[1])
