
def eval_function(function = '1',t='0',y='0',h='1'):
    '''This function simply takes the function and value of variables to solve them
    This function is will be called in components solution in All_components_rk4_2'''

    d = [i for i in function]
    k =''.join(d)
    return(eval(k))



'''Other types of  function variables identification/simplification available and we can use'''
#--------------------- type 2 ---------------

# from sympy import symbols, solve
#
# x = symbols('x')
# expr = x-4-2
#
#
# sol = solve(expr)
#
#
# sol

#--------------------- type 3 ---------------

# from sympy import symbols, Eq, solve
#
# y = symbols('y')
# eq1 = Eq(y + 3 + 8)
#
#
# sol = solve(eq1)
# sol
