# =============================================================================
# a=0
# for i in range(10):
#     a=a+i
#     print('First',i,'Numbers When added gives',a)
# print(a)
# =============================================================================
# =============================================================================
# a=int(input("Enter a Number for table you want to dipslay"))
# for i in range(10):
#       print(a,'X',i,'=', a*i)
# =============================================================================
# =============================================================================
# print('It is the time to start')
# n=1
# condition=1
# while condition==1:
#     print('Token number',n,' may please come in')
#     condition=int(input('Continue? yes/No'))
#     n=n+1
# =============================================================================
from statistics import mean
from scipy import stats
l=[1,2,7,9,5,11,44,55,70]
l.sort()
print(l)
#m=mean(l)
m=stats.trim_mean(l, 0.1)
print(m)