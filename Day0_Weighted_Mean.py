
# let's compute the weighted mean of the gieven input
# compute the mean based on object's frequency

N = int(input())
X = list(map(int(), input().split()))
W = list(map(int(), input().split()))

n_w = sum((x*x) for x in X for y in W)
s_w = sum(w for w in W)

weighted_mean = n_w / s_w
print(weighted_mean)
