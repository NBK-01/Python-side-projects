# Python Program to find the area of triangle

a = 8
b = 9
c = 5



#semi perimeter.
s = (a + b + c) / 2
print ("the three sides of the triangle are equal to 8,9,and 5, therefore:")
# area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
