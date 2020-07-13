num=int(input())
while(num>1):
    if(num & 1):
        print(num,end=" ")
        num=(num*3)+1
        print(num,end=" ")

    else:
        num=num//2
        print(num,end=" ")

