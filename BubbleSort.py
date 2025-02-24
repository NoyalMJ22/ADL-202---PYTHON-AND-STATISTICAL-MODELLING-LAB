def bubble_sort(a):
    n=len(a)
   
    for i in range(n):
        for j in  range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

b=[12,23,10,45,67,45]

c=bubble_sort(b)
print("Sorted List",c)
