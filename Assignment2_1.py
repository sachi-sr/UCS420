roll_no=input("Enter your roll number:")
L=[]
for digit in roll_no:
  L.append(int(digit)*10)

print("L=",L)

L.append(50)
("After append:",L)
L.insert(2,30)
print("After insert: ",L)

L.remove(50)
print("After remove:",L)
L.pop(2)
print("After pop: ",L)

L.sort()
print("Ascended",L)
L.sort(reverse=True)
print("Descended",L)

print("First 3",L[:3],"\nLast 3",L[-3:0])
total=sum(L)
average=total/len(L)

print(average)
Listt=[]
for x in L:
  if x>average:
    Listt.append(x)
print("Element greater than average",Listt)