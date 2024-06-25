# Import packages.
import cvxpy as cp
import numpy as np

# Parameters for first problem
s1 = 100
s2 = 200
s3 = 300
c1 = 50
c2 = 55
c3 = 75


# Define and solve the CVXPY problem.
# define the number of variables, in this case we have three x's for the three factories
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()
# define the constraints
constraints = [x1*c1+x2*c2+x3*c3 <= 3000000, x1 >=0, x2 >=0, x3>=0]

# define the objective function
objective = cp.Maximize(x1*(s1-c1)+x2*(s2-c2)+x3*(s3-c3))

# define the problem
problem = cp.Problem(objective, constraints)
# solve the problem
problem.solve()

# Print result.
print("\nFor the first problem:")
print("\nThe maximum profit is", problem.value)
print("The values of x1, x2, x3 are")
print(x1.value)
print(x2.value)
print(x3.value)


# ==========================================================================================

# Parameters for second problem
s1 = 50
s2 = 201
s3 = 200
c1 = 52.4
c2 = 55
c3 = 75


# Define and solve the CVXPY problem.
# define the number of variables, in this case we have three x's for the three factories
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()
# define the constraints
constraints = [x1*c1+x2*c2+x3*c3 <= 3000000, x1 >=0, x2 >=0, x3>=0]

# define the objective function
objective = cp.Maximize(x1*(s1-c1)+x2*(s2-c2)+x3*(s3-c3))

# define the problem
problem = cp.Problem(objective, constraints)
# solve the problem
problem.solve()

# Print result.
print("\nFor the second problem:")
print("\nThe maximum profit is", problem.value)
print("The values of x1, x2, x3 are")
print(x1.value)
print(x2.value)
print(x3.value)
