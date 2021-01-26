size=int(input("Enter the size of list: "))
a=[]
for i in range(size):
    num=int(input("Enter the Elements in list: "))
    a.append(num)
               
oddSum = 0
evenSum = 0

for i in a:
    if i%2==0:
        evenSum = evenSum + i
    else:
        oddSum += i

print("Even sum is: ",evenSum)
print("Odd  sum is: ",oddSum)
