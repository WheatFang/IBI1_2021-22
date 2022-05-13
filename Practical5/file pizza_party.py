#calculate the number of cuts required to make a slice for each member ofIBI 
n=1 #n is the number of times to cut pizza, at least once
p=(n*n+n+2)/2 # Cut n times, and you can get p pieces of pizza
while (p<64):#loop ends when the number of pizza pieces is greater than the total number of people
    n=n+1 # Otherwise n plus one 
    p=(n*n+n+2)/2
    print(n)
print("the number is", str(n))
