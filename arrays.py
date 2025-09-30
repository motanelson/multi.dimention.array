print("\033c\033[43;30m\nboard\n")
def aarrays(values,c):
    b=[]
    for n in range(c):
        b=b+[values.copy()]
    return b
def arrays(arr,values):
    a=values
    b=[]
    c=[]
    if len(arr)>5:
        print("array to big")
        return b
    for n in range(arr[0]):
        b=b+[values]
    c=b.copy()
    for n in range(1,len(arr)):
        c=aarrays(c,arr[n])
    return c

aa=[2,2,2,2]
a=arrays(aa,0)

print(a)