'''7. We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
'''
from sympy import symbols, Eq,solve
rab,chick = symbols('rabbits,chicken')
eq1=Eq(( rab + chick ),35)
eq2=Eq(( 4*rab + 2*chick ),94)
print(solve((eq1,eq2),(rab,chick)))