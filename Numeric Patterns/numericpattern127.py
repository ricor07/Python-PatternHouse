print("Enter the no of rows: ")
n = int(input())
for i in range(n):
    count = i
    for j in range(n):
        print(n-count, end=" ")
        if(n-count<5):
            count-=1
    print()
    
    
# Enter the no of rows: 
# 5
# 5 5 5 5 5 
# 4 5 5 5 5 
# 3 4 5 5 5 
# 2 3 4 5 5 
# 1 2 3 4 5 
