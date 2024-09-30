import statistics as st

A=[10,20,30,40,50]
mean=st.mean(A)
print(mean)
###########################

A=[10,20,30,40,50]
freq=[1,2,4,5,6]

Af=[A[i]*freq[i] for i in range(len(A))]
mean=sum(Af)/sum(freq)
print(mean)
###########################
intervals=[(10,20),(20,30),(30,40),(40,50)]
freq=[5,8,6,7]
# for x,y in intervals:
#     Z.append((x+y)/2)

mid_pts= [(x+y)/2 for (x,y) in intervals]
Af= [mid_pts[i]*freq[i] for i in range(len(intervals))]
mean=sum(Af)/sum(freq)
print(mean)

###########################
def find_mean(intervals, freq):
    # Calculate midpoints for each interval
    mid_pts = [(x + y) / 2 for (x, y) in intervals]
    
    # Calculate Af = mid_pts[i] * freq[i]
    Af = [mid_pts[i] * freq[i] for i in range(len(mid_pts))]
    
    # Calculate the mean
    mean = sum(Af) / sum(freq)
    return mean

# Intervals and frequencies
intervals = [(10, 20), (20, 30), (30, 40), (40, 50)]
freq = [5, 8, 6, 7]

# Call the function
mean = find_mean(intervals, freq)
print(mean)

##########################
A=[1,2,4,3]
B=sorted(A)
n=len(A)
if n%2==0:
    median=(B[(n//2)-1] + B[(n//2)])/2
else:
    median=B[((n+1)//2)-1]

print("Median: ",median)

##########################
def find_median(num):
    n=len(num)
    if n%2==0:
     median=(B[(n//2)-1] + B[(n//2)])/2
    else:
     median=B[((n+1)//2)-1]
    return median

A=[1,2,4,3]
B=sorted(A)
n=len(A)
median=find_median(B)
print(median)

###########################
import statistics as sm

A=[10,30,20,40]
mean=sm.median(A)
print(mean)

###########################
intervals=[(10,20),(20,30),(30,40),(40,50)]
freq=[5,8,6,7]

idx = freq.index(max(freq)) # 1 is the index of max frequency which is 8

L,U=intervals[idx]
h= U-L
f0= freq[idx-1]
f1= freq[idx]
f2= freq[idx+1]

mode= L +((f1-f0)/(2*f1-f0-f2))*h
print("Mode:",mode)

############################
intervals=[(10,20),(20,30),(30,40),(40,50)]
freq=[5,8,6,7]

idx = freq.index(max(freq))

L,U=intervals[idx]
N= sum(freq)
CF= sum(freq[:idx])
f=freq[idx]
h=U-L

median= L + ((N/2-CF)/f)*h
print("Median: ",median)