

from variables_identification_1 import eval_function




class All_components_rk4:
    '''This class consists of methods simply evaluates the function and Component of RK4 when called in
    This function is will be called in Rk4_solve in file 3'''

    def __init__(self,function = 0,t = 0,y_0 = 0, h=0):
        self.function = function
        self.y = y_0
        self.t =t
        self.h = h

    def k1(self):
        k1 = self.h*eval_function(self.function,self.t,self.y)
        self.k1 = k1
        return k1

    def k2(self):
        k1 = self.k1()
        k2 = self.h*eval_function(self.function,(self.t+self.h/2),(self.y+(self.k1/2)))
        self.k2 = k2
        return k2

    def k3(self):
        k2 = self.k2()
        k3 = self.h*eval_function(self.function,(self.t+self.h/2),(self.y+(self.k2/2)))
        self.k3 = k3
        return k3

    def k4(self):
        k3 = self.k3()
        k4 = self.h*eval_function(self.function,(self.t+self.h),(self.y+(self.k3)))
        self.k4 = k4
        return k4

    def y_update(self):
        k4 = self.k4()
        y_update = self.y + (self.k1 + 2*self.k2 + 2*self.k3 + self.k4)/6
        self.y_update = y_update
        return y_update

    def t_update(self):
        t_update = self.t + self.h
        self.t_update = t_update
        return  t_update





