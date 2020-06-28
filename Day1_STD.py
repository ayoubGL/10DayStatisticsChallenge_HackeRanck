# The awesome statistical measure, one of the importance variability's parameter : standart deviation

import math
N = int(input())
X = list(map(int, input().split()))
mean = sum(x for x in X) / len(X)
variance = sum((x - mean)**2 for x in X) / len(X) 
std = math.sqrt(variance)
print(round(std,1))


