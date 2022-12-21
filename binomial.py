import math 

print ("To solve quadratic, INSERT:")
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))
D = ((b*b)-(4*a*c))
if D < 0:
        print("no solution")
elif(D == 0):
        print("1 Real Solution")
top = -b+math.sqrt(D)
overall = (top/a+a)
print (overall)
if(D > 0):
        print("2 Real solutions") 
top1 = -b+math.sqrt(D)
overall1 = (top1/a+a)
print (overall1)
top2 = -b-math.sqrt(D)
overall2 = (top2/a+a)
print (overall2)




