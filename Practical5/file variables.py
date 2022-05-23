#desrib which year has the greastest number of new COVID-19
a = 19245301
b = 4218520
c = 271
d = b-c
e = a-b
if d>e: # determine which rate is great
    print("the rate of new case in 2020 is greater than in 2021")
elif d<e:
    print("the rate of new case in 2021 is greater than in 2020")
else:
    print("the rate of new case in 2020 is the same sa in 2021")


#w=x+y Boolean
x = 3>2
y = 1>2
w = x and y
print(x,"and",y,"is",w)
x = True
y = False
w = x and y
print(w)# W is False because Y is false
x = True
y = True
w = x and y
print(w)# W is true only when x and y are true
print(2)
x = ""
y = False
w = x and y
print(w)# When applying and, print the first null value or false value, print ""
x = "Wheat"
y = False
w = x and y
print(w) #When applying and, it prints the first null value or the value of false, in this case false
