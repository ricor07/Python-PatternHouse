print("Enter the number of rows:")
n = int(input())
for i in range(0,n):
    for j in range(0,n-i):
        if((i+j)%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
    
    
# OUTPUT
# Enter the number of rows:
# 5
# 1 0 1 0 1 
# 0 1 0 1 
# 1 0 1 
# 0 1 
# 1 
