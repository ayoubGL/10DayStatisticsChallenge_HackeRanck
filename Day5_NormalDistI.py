#Task
# In a certain plant, the time taken to assemble a car is a random variable, X , having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:

# 1 Less than 19.5 hours?
# 2 Between 20 and 22 hours?

import math

u,s = list(map(int, input().split()))
x = int(input())
a,b = list(map(int, input().split()))

cdf = lambda x: 0.5 + 0.5* math.erf((x-u)/(s * math.sqrt(2)) )

print(round(cdf(x),3))
print(round(cdf(b)-cdf(a),3))