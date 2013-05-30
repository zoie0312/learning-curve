class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __str__(self):
        return str(self.name)

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    if newFrob.myName >= atMe.myName:
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            insert(atMe.getAfter(), newFrob)
    else:
        print('test1')
        if atMe.getBefore() == None:
            print('test2')
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            insert(atMe.getBefore(), newFrob)

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

#insert(eric, andrew)
#insert(eric, ruth)
#insert(eric, fred)
#insert(ruth, martha)
