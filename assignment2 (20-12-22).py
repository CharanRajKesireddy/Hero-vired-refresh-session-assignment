import pandas as pd
m=list(map(int,input().split()))
n=pd.Series(m)
print(n*n)