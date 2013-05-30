def integrate(f, a, b, parts):
    spacing = float(b-a)/parts
    current = 0
    for i in range(parts):
        current += spacing * f(a+ i*spacing)
    return current

def successiveApproxIntegrate(f, a, b, epsilon):
    # Your Code Here
    iterate = True
    n = 0
    while iterate:
        n += 1
        '''
        width_n = float(b-a)/n
        area_n = 0
        for i in range(n):
            area_n += f(a + i*(b-a)/n) * width_n
        width_2n = float(b-a)/(2*n)
        area_an = 0
        for j in range (2*n):
            area_2n += f(a + j*float(b-a)/(2*n)) * width_2n
        '''
        partsN = 2**n
        partsN2 = 2**(n-1)
        areaN = integrate(f, a, b, partsN)
        areaN2 = integrate(f, a, b, partsN2)
        if areaN - areaN2 > 0:
            if areaN - areaN2 <= epsilon:
                iterate = False
        else:
            if areaN2 - areaN <= epsilon:
                iterate = False
    print 'N= ', 2**n
    print 'area= ', areaN
    print 'N/2 = ', 2**(n-1)
    print 'area_N/2= ', areaN2
    return areaN

def f(x):
    return x**2 

successiveApproxIntegrate(f, 0.0, 10.0, 0.01)
