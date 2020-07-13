def missing_number(x):
    n=len(x)
    total=(n+1)*(n+2)/2
    sum_off_x=sum(x)
    return total-sum_off_x

x=[1,2,3,5,6]
miss=missing_number(x)
print(miss)
