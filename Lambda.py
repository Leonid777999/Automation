#LAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDA
# 1.
l_list = [1,2,3,4,5]
o=6
multi_list = list(map(lambda n:n*o, l_list))
print(multi_list)

# 2.
odd_list = list(map(lambda p:p%2==0,l_list))
print(odd_list)

# 3.
import datetime
today = datetime.datetime.today()
year = lambda x : x.year
month = lambda y : y.month
day = lambda z: z.day

print(year(today))
print(month(today))
print(day(today))

# 4.
double_list =list(map(lambda x: x*2,l_list))
print(double_list)

# 5.
filter_list = list(filter(lambda p:p%2==0,l_list))
print(filter_list)