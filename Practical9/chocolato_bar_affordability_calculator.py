#with the limited money, how many chocolate bar could we buy?
def buy_chocolate_bar(m,c):
    num_bars = m//c 
    change = m%c
    return num_bars, change
m = float(input("The total money that the use has is:"))
# The input is a string and needs to be converted to a number
c = float(input("The unit price of chocolate bar is:"))
answer = buy_chocolate_bar(m,c)
print("the man can buy",answer[0],"chocolate bars and have{:.3f}".format(answer[1]),"dollars left")
# In reality, the price of goods is often a decimal.
# Because of the way Python itself converts data types,
# we obtain a deimal with multiple decimal places.
# Thus we need to keep three decimal places in the final result
