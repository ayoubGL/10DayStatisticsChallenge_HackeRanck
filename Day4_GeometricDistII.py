# the negative binomial dist: Geometric Dist

# Task
# The probability that a machine produces a defective product is 1/3. What is the probability that the first defect is found during the 5th inspection?

x,p = list(map(int, input().split()))
n=int(input())

pro_def = (1 - (1/p))**(n-x) * (1/p)
print(round(pro_def,3))
