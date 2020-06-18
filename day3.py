a=int(input("Input the starting number of the G.P. series."))
n=int(input("Input the number of items for the G.P. series."))
r=int(input("Input the common ratio of G.P. series:"))
s=0
print("The numbers for the G.P. series- ")
for i in range (n):
    s = s + a
    print(a,end=" ")
    a = a*r

print("\nThe Sum of the G.P. series.- ",s)
    
