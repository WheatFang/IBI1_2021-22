#calculate the number of cuts required to make a slice for each member ofIBI 
n=1
p=(n*n+n+2)/2
while (p<64):
    n=n+1
    p=(n*n+n+2)/2
    print(n)
print("the number is", str(n))
