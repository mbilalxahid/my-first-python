from Rk4_solve import Rk4_solve

# import numpy as np
# import math


h = 0.2
t_0 = 0.0
t_f = 2.0
y_0 = 0.5

f_of_x = 'y-t*t+1'

step_size = int((t_f-t_0)/h)+1

sol = Rk4_solve(f_of_x, t_0,t_f, y_0, step_size, h)
sol.rk4()





