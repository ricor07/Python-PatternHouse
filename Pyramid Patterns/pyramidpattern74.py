height = int(input())

for i in range(0,height+1):

    for j in range(0,i):
        print(end=" ")

    for j in range(height,i,-1):
        
        if(i%2 == 0):
            print(height-j+1,end=" ")

        else:
            c = chr(height-j+65)
            print(c,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 5 
#  A B C D 
#   1 2 3 
#    A B 
#     1 
     
