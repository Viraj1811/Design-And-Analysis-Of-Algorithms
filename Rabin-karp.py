string="abababcd"
pattern="abcd"
m=len(pattern)
n=len(string)
b=256
for i in range(0,len(pattern)):
    sump=sump+ascii(pattern[i])*b**(m-i-1)
    sumT=0
    for j in range(0,len(string)):
        sumT=sumT+ascii(string[j])*b**(n-j-1)
        if(sumT==sump):
            print("pattern found at index")
            for j in range(m,n):
                sumT=sumT-b*ascii(string[j-m]*b*(m-1)*b)+ascii(string[j+m])
                if(sumT==sump):
                    print("pattern found at index",j-m+1)