import re
def sqr(n):
    return 3*int(n)**2+5
s=input()

dig = re.findall("['\d']+",s)

a=[]
for i in range(len(dig)):
    a.append(sqr(dig[i]))

z=''

if '+' in s:
    z='+'
elif '-' in s:
    z='-'
elif '*' in s:
    z='*'
elif '/' in s:
    z='/'
print(a[0],z,a[1],'=',a[2])
