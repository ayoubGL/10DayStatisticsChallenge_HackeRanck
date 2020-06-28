# the Binomial Dist: one of the most used Dist when it come to the success and failure

# # Task ---
# The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e.,1.234  format).

import sys 
import math

b = [float(i) for i in sys.stdin.readline().split()]

def nCr(n,r):
    f = math.factorial
    return f(n)/( f(r) * f(n-r))

pb = b[0]/(b[0]+b[1])
pg = 1-pb

n = 6
p3b = 0 

for i in range(3,n+1):
    p3b += nCr(n,i) * (pb**i) * (pg**(n-i))

print(round(p3b,3))
