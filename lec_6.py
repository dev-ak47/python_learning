# import statistics as st

# A=[10,20,30,40,50]
# mean=st.mean(A)
# print(mean)
############################

# A=[10,20,30,40,50]
# freq=[1,2,4,5,6]

# Af=[A(i)*freq(i) for i in range(len(A))]
# mean=sum(Af)/sum(freq)
# print(mean)
############################
# intervals=[(10,20),(20,30),(30,40),(40,50)]
# freq=[5,8,6,7]
# # for x,y in intervals:
# #     Z.append((x+y)/2)
############################

# mid_pts= [(x+y)/2 for (x,y) in intervals]
# Af= [mid_pts[i]*freq[i] for i in range(len(intervals))]
# mean=sum(Af)/sum(freq)
# print(mean)

def find_mean(num,freq):
    total=sum(num)
    ftotal=sum(freq)
    count=len(num)
    fcount=len(freq)
    Af=[num(i)*freq(i) for i in range(len(num))]
    mean=sum(Af)/sum(fcount)
    return mean

A=[(10,20),(20,30),(30,40),(40,50)]
mean=find_mean(A)
print(mean)