
import pandas as pd
a=list(map(int,input("a=").split()))
b=list(map(int,input("b=").split()))
c=pd.Series(a)
d=pd.Series(b)
# print(c,d)
e=input("Enter the type of operation: ")
if e=="+":
    print(c+d)
elif e=="-":
    print(c-d)
elif e=="*":
    print(c*d)
elif e=="/":
    print(c/d)
elif e=="%":
    print(c%d)
else:
    print("Invalid operator")