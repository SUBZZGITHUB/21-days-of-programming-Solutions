m=int(input("enter no. of rows"))
# Outer loop
for i in range(65,65+m):
    m=m-1
    # Inner loop 1 
    for j in range(m,1,-1):
        print(" ",end="")
    # Inner loop 2
    for k in range(65,i+1):
        print(chr(k),end="")
    # Inner loop 3
    for j in range(i-1,64,-1):
        print(chr(j),end="")
    print()
