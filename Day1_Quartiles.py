# The quatiles: Q_1, Q_2(median), Q_3, the quartiles helps us to construct the boxplot for our data, thus detective  the outliers :) :)

# we use the meadin function  from statistics model
from statistics import median


n = int(input())
x = sorted(list(map(int, input().split())))

print(int(median(x[:n//2])))      # Q_1
print(int(median(x)))             # Q_2
print(int(median(x[(n+1)//2:])))  # Q_3
