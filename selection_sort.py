#Selection Sort
a=[12,28,11,20,8,18]
for i in range(len(a)-1):
    min=i
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]
    print(a)
