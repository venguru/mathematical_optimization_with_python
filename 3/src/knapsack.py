"""
3-1. ナップサック問題クラスの定義
"""

class KnapsackProblem(object):
    """ The difinition of KnapSackProblem """
    def __init__(self, name, capacity, items, costs, weights,
                 zeros=set(), ones=set()):
        self.name = name
        self.capacity = capacity
        self.items = items
        self.costs = costs
        self.weights = weights
        self.zeros = zeros
        self.ones = ones
        self.lb = -100
        self.ub = -100
        ratio = {j:costs[j]/weights[j] for j in items}
        self.sitemList = [k for k, v in 
            sorted(ratio.items(), key=lambda x:x[1], reverse=True)]
        self.xlb = {j:0 for j in self.items}
        self.xub = {j:0 for j in self.items}
        self.bi = None

    def getbounds(self):
        """ Calculate the upper and lower bounds. """
        for j in self.zeros:
            self.xlb[j] = self.xub[j] = 0
        for j in self.ones:
            self.xlb[j] = self.xub[j] = 1

        if self.capacity < sum(self.weights[j] for j in self.ones):
            self.lb = self.ub = -100
            return 0

        ritems = self.items - self.zeros - self.ones
        sitems = [j for j in self.sitemList if j in ritems]

        cap = self.capacity - sum(self.weights[j] for j in self.ones)
        for j in sitems:
            if self.weights[j] <= cap:
                cap -= self.weights[j]
                self.xlb[j] = self.xub[j] = 1
            else:
                self.xub[j] = cap /self.weights[j]
                self.bi = j
                break
        self.lb = sum(self.costs[j] * self.xlb[j] for j in self.items)
        self.ub = sum(self.costs[j] * self.xub[j] for j in self.items)


    def __str__(self):
        """ KnapSackProblemの情報を印字 """
        return('Name = '+self.name+', capacity = '+str(self.capacity)+',\n'
               'items = '+str(self.items)+',\n'+
               'costs = '+str(self.costs)+',\n'+
               'weights = '+str(self.weights)+',\n'+
               'zeros = '+str(self.zeroz)+', ones = '+str(self.ones)+',\n'+
               'lb = '+str(self.lb)+', ub = '+str(self.ub)+',\n'+
               'sitemList = '+str(self.sitemList)+',\n'+
               'xlb = '+str(self.xlb)+',\n'+'xub = '+str(self.xub)+',\n'+
               'bi = '+str(self.bi)+'\n')
