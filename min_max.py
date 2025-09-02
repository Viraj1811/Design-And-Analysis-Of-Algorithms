def minmax(arr):
    if len(arr)==1:
        return arr[0],arr[0]
    mid=int(len(arr)/2)
    min1,max1=minmax(arr[:mid])
    lmin,lmax=minmax(arr[:mid])
    rmin,rmax=minmax(arr[mid:])
    return min(lmin,rmin),max(lmax,rmax)

arr=[5,6,10,3,1,8,12]
print(minmax(arr))