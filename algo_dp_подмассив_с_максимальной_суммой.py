# Нахождение подмассива с максимальной суммой
# Алгоритм Кадане
a=list(map(int,input().split()))
cur_sum=[0]*(len(a))
dp=[0]*(len(a))
dp[0]=a[0]
cur_sum[0]=a[0]
for i in range(1,len(a)):
    cur_sum[i]=max(a[i],cur_sum[i-1]+a[i])
    dp[i]=max(cur_sum[i],dp[i-1])
print(dp[-1])