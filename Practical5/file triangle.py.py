n = 1 # only one point on the top layer
sum = 0
while n < 11: # use a while lope to add 10 times
    sum = sum + n
    n = n+1 # Each layer has one fewer points than the last one
    print(sum)
