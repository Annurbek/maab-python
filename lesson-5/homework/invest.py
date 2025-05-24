#2-problem
def invest(amount, rate, years):
    for i in range(1,int(years)+1):
        amount=amount*(1+rate)
        print("year",i,": ",round(amount,2))
amount, rate, years=map(float,input().split())
invest(amount,rate,years)
