# doing in a hard way

N = int(input()) # read from stdin
Numbers = []
Numbers = input().split()

# mean

mean = sum(Numbers) / N
print(mean)

sorted_list = sorted(Numbers)

# median
if N % 2 != 0:
	print(sorted_list[ N//2 ]
else :
    l = N//2
    meadian  = (sorted_list[l] + sorted_list[l-1]) / 2
    print(meadian)

# Mode
print(max(sorted(Numbers), key=Numbers.count))

