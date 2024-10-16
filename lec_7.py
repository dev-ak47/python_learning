## Finf cumulative frequency

def find_cf(freq):
    cf=[0]*len(freq)  #cf=[0,0,0,0]
    cf[0]=freq[0]
    for i in range(1,len(freq)):
     cf[i]=cf[i-1]+freq[i]
    return cf

def find_med(intervals,freq):
   N=sum(freq)
   cf=find_cf(freq)
   for i,cf in enumerate(cf):
      if cf>=N/2:
         index=1
         break;


## enumerate
A=["Sonu","Shivani","Pankaj"]
B=[(i,j) for i,j in enumerate(A)]
print(B)