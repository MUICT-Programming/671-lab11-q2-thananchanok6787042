n = int(input())
list1=[]
list2= []
for i in range(n):
    x = int(input())
    list1.append(x)
for j in range(n):   
    y = int(input())
    list2.append(y)

def summation():
    updated_list =[]
    for char in range(n):
        updated_list.append(list1[char]+list2[char])
    return updated_list

def find_min_max():
    minn = min(summation())
    maxx = max(summation())
    return(minn,maxx)

print(summation())
print(find_min_max())        
