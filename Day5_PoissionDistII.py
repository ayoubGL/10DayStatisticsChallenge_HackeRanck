# In this day we will use the expected value of a poission random variable that is:    E[X] = lambda thus, E[x**2] = lambda**2

# Task :
# The manager of a industrial plant is planning to buy a machine of either type  A or B type

# . For each day’s operation:

#     The number of repairs, X , that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C_A = 160 + 40* X**2.
# The number of repairs,Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is
# C_B = 128 + 40 * Y**2
#     .

# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

# Answer

A_avg, B_avg = list(map(float, input().split())) # read the avg of poison random var

Expected_A_dailyCost = 160 + 40 * (A_avg + A_avg**2) # use the expected value of poission random var

Expected_B_dailyCost = 128 + 40 * (B_avg + B_avg **2)

print(round(Expected_A_dailyCost,3))
print(round(Expected_B_dailyCost,3))