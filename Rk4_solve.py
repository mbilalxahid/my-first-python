
import numpy as np
# import math

from All_components_rk4_2 import All_components_rk4

class Rk4_solve:
    '''This function simply takes the function and value of variables and interact with file 2 and 1 to solve them'''

    def __init__(self,function = 0,t_0=0,t_f = 1,y_0 = 0,step_size = 1, h=0):
        self.function = function
        self.y_0 = y_0
        self.t_0 = t_0
        self.t_f =t_f
        self.step_size = step_size
        self.h = h

    # def rk4(self):
    #     t_0 =self.t_0
    #     t_f = self.t_f
    #     step_size = self.step_size
    #     y_0 = self.y_0
    #     h =self.h
    #     t_periods = np.linspace(t_0, t_f, step_size)

        for i in range(len(t_periods) - 1):
            t = float(t_periods[i])
            self.t = t
            print(self.t + h)
            y_up = All_components_rk4(self.function, self.t, self.y_0, self.h )
            # d = All_functions(self.function, self.t, self.y_0, self.h )
            # self.d = d.k4()
            # print(self.d)
            self.y_0 = y_up.y_update()
            print(self.y_0)



