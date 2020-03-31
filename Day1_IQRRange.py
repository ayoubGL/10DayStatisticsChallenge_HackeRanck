# after we have the quartiles, when can compute the interquartile (Q_3 - Q1) the range of our data


from  itertools import repeat
from statistics import median

N = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
S = []
for i,j in zip(X,F):
    S.extend(repeat(i,j))  # repeat create i j times 
S = sorted(S)

Q_1 = int(median(S[:N//2]))
Q_3 = int(median(S[-N//2:]))

print(Q_1, Q_3)
print(round((Q_3-Q_1),1))
