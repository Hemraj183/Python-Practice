size=int(input("Enter the size of list: "))
a=[]
for i in range(size):
    num=int(input("Enter the Elements in list: "))
    a.append(num)

max_=a[0]
min_=a[0]
for i in a:
    if i>max_:
        max_=i
    if i<min_:
        min_=i

print("Max is ",max_)
print("Min is ",min_)
