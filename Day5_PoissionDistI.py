from math import exp 

# the Poission distribution when:
# if we have an average of success in specific region "lambda"
# and we have specific number of scuccess in this specific region K
# them we easly apply this for our random var p(x) = (lambda ^ k) * exp(-lambda) / factorial(K)

#____________ Task _____________
# A random variable, X , follows Poisson distribution with mean of 2.5 . Find # the probability with which the random variable is equal to 5 .

def fact(k):
    if k == 0:
        return 1
    else:
        return k*fact(k-1)

lambda_ = float(input())
k = int(input())

poisson_dist =  (lambda_**k * math.exp(-lambda_)) / fact(k)
print(round(poisson_dist,3))